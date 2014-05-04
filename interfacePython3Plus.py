from haystackmapper import haystackmapper 
from haystackreducer import haystackreducer
from haystack import haystack
from needlefactory import needlefactory
from wavsound import wavsound
from multiprocessing import Pool, Process, Manager
from calltomapper import calltomapper
import time
import os

def run():
    
    """ run runs the database search taking three user inputs, the query wav file,
    number of partitions, and number of partition samples"""
    
    good_file = 0
    
    while (good_file == 0):
        query     = input("Submit .wav file to search against database (Example: button.wav): ")
        if (os.path.isfile(query)):
            good_file = 1
            
    #Instantiate Wavsound objects from the wav files
    t_wavsounds = {}
    query_wavsound = wavsound(query)    
    print("\n**Higher number of partitions increases false positive rates, \nwhile lower number of partitions increases false negative rates\n")
    partition = input("Set number of partitions of the query from 1 to " + str(int(len(query_wavsound.get_data())/3))+": ")
    samples   = input("Set number of samples of partitions from 1 to " + partition + " (Recommend < 50): ")
    
    # Database Structure
    haystacks = []
    
    # Database look up directory
    rootdir    = 'db'
    
    
    
    for subdir, __, files in os.walk(rootdir):
        for file in files:
            # for debug print (subdir+"/"+file)
            t_wavsounds[subdir+"/"+file] = wavsound(subdir+"/"+file)
            # for debug print(t_wavsounds[subdir+"/"+file])
            haystacks.append(haystack(subdir+"/"+file,t_wavsounds[subdir+"/"+file].get_data()))
            
    query_needle_factory = needlefactory(query_wavsound,int(partition),int(samples))
    
    
    haystackmap = haystackmapper(haystacks)
    
    needles = query_needle_factory.get_needles()
    manager = Manager()
    
    # Map processes emit key-value pairs to emissions
    return_emissions = manager.dict()    
    
    # Job is a list of processes
    jobs = []
    
    # Process number
    pnum = 0
    
    print ("Number of Needles: ",len(needles))
    
    # Database query time
    start_time = time.time()
    
    #Distribute processes using multiprocessor
    for needle in needles:
        p = Process(target=calltomapper, args=(haystackmap,needle,pnum,len(needles),return_emissions))
        jobs.append(p)
        p.start()
        pnum += 1
    
    for proc in jobs:
        proc.join() 
    
    # flatten return_emissions into a list
    emissions_list = sum(return_emissions.values(),[])
    
    print("Search Result:")    

    result_dict = haystackreducer(emissions_list)
    
    # Tabulate % match (wav files with 0% match are excluded from the result)
    for key in result_dict:
        print(str(key),": ",(25-len(str(key)))*" ",str("{0:.2f}".format(int(result_dict[key])/len(needles)*100)),"% match")
    
    # Show search time
    timelapse_parallel = time.time() - start_time   
    print(timelapse_parallel, "seconds")
    
if __name__ == '__main__': 
    print (".WAV Search Engine Version 1 (For Python Ver. 3+) ")
    run()