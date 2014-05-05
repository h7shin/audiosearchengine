from haystackmapper import haystackmapper 
from haystackreducer import haystackreducer
from haystack import haystack
from needlestorage import needlestorage
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
    samples   = input("Set number of samples (n) of partitions from 1 to " + partition + ": ")
    
    # Database look up directory
    rootdir    = 'db'
    
    # Database Structure
    haystackss = []   # split database into list of smaller database
    key_names = []

    # Database Spliting Parameters (1 to number of database entries)
    db_size_per_split = 100
    max_split = int(input("Set maximum number of split databases :"))
    
    for i in range(max_split):
        haystackss.append([])    
    
    # Read Files
    counter = 0
    for subdir, __, files in os.walk(rootdir):
        for file in files:
            key_names.append(subdir+"/"+file)
            split_db_key = min(max_split, int(counter / db_size_per_split))
            t_wavsounds[subdir+"/"+file] = wavsound(subdir+"/"+file)
            haystackss[split_db_key].append(haystack(subdir+"/"+file,t_wavsounds[subdir+"/"+file].get_data()))
            counter += 1
            
    query_needle_factory = needlestorage(query_wavsound,int(partition),int(samples))
    
    # Get segments of the query data as needles
    needles = query_needle_factory.get_needles()
    
    # Manager to keep track of all map results
    manager = Manager()
    
    # Map processes emit key-value pairs to emissions
    return_emissions = manager.dict()    
    
    # Job is a list of processes
    jobs = []
    
    # Process number
    pnum = 0
        
    # Database query time
    start_time = time.time()
    
    #Distribute processes using multiprocessor
    len_needles = len(needles)
    for needle in needles:
        for haystacks in haystackss:
            if haystacks != []:
                p = Process(target=calltomapper, args=(haystacks,needle,pnum,len_needles*len(haystackss),return_emissions))
                jobs.append(p)
                p.start()
                pnum += 1
    
    for proc in jobs:
        proc.join() 
    
    # flatten return_emissions into a list
    emissions_list = sum(return_emissions.values(),[])
    
    print("Search Result:")    

    result_dict = haystackreducer(emissions_list, key_names)
    
    # Tabulate % match (wav files with 0% match are excluded from the result)
    for key in result_dict:
        if result_dict[key] > 0:
            print(str(key),": ",(25-len(str(key)))*" ",str((int(result_dict[key])/len(needles)*100)),"% match")
    
    # Show search time
    timelapse_parallel = time.time() - start_time   
    print(timelapse_parallel, "seconds")
    
if __name__ == '__main__': 
    print (".WAV Search Engine Version 1 (For Python Ver. 3+) ")
    run()