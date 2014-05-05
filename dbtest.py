from haystackmap import mapper
from haystackreducer import haystackreducer
from haystack import haystack
from needlestorage import needlestorage
from wavsound import wavsound
from multiprocessing import Pool, Process, Manager
from calltomapper import calltomapper
import time
import profile
import re

""" dbtest is a simulation module to measure time complexity of 
database search applied to a virtual database"""

def test(): 
    button_wavsound = wavsound('button.wav')
    
    haystackss = []   # split database into list of smaller database
    keynames = []
    db_size = 300     # Set Database Size
    num_split_db = 2  # Set number of split databases
    size_split_db = int(db_size/num_split_db)
    
    for i in range(num_split_db):
        haystackss.append([])
    
    counter = 0
    for i in range(db_size):
        split_db_key = int(counter / size_split_db)
        keynames.append(i)
        haystackss[split_db_key].append(haystack(i,button_wavsound.get_data()))
        counter+=1
    
    
    #haystacks.append(haystack("7",[1, 2, 3, 4, 5]))
        
    button_needle_factory = needlestorage(button_wavsound,1000,50)
    emissions = []
    

    print("USING MAP PROCESS and Manager")
    
    needles = button_needle_factory.get_needles()
    print(needles[0])
    
    manager = Manager()
    return_emissions = manager.dict()    
    jobs = []
    pnum = 0
    
    # number of needles not size of each needle
    len_needles = len(needles)
    print ("Number of Needles: ",len_needles) 
    start_time = time.time()
    

    
    for needle in needles:
        for haystacks in haystackss:   
            p = Process(target=calltomapper, args=(haystacks,needle,pnum,len_needles*num_split_db,return_emissions))
            jobs.append(p)
            p.start()
            pnum += 1    
    print(time.time() - start_time)
    
    for proc in jobs:
        proc.join() # wait for each process to end completely
        
    print(time.time() - start_time)
    emissions_list = sum(return_emissions.values(),[])
    print("Reduce Result:")    
    print(haystackreducer(emissions_list,keynames))        
    print("Done")
    print(time.time() - start_time)
    
    
    """
    This is a pool implementation of parallel processing, it has been 
    commented out as it was slower than the Process method
    
    print(button_wavsound)
    print("Utilizing MapReduce Pattern")
    
    pool = Pool(2) # if it is a quad-core machine it can be set to 4
    print(button_needle_factory.get_needles())
    emissions = pool.map(haystackmap.mapper, button_needle_factory.get_needles())
    print(emissions) 
    print(haystackreducer(sum(emissions,[])))    
    
    emissions = []
    """
    
    """ The algorithm below is a serial method, no optimization """
    """
    print("Long Way")
    start_long_time = time.time()
    #haystackmap.clear_emission()
    
    i = 10000 # cautionary protection from accidental infinite loop
    
    while i > 0:
        needle = button_needle_factory.pop_unused_needle()
        if (needle == []):
            break
        emissions += mapper(haystacks,needle)
        i -= 1
        print("Total So Far: ",len(emissions))
    
    print("Final:",haystackreducer(emissions, keynames))
    timelapse_serial = time.time() - start_long_time
    print (db_size + 1, timelapse_parallel, timelapse_serial)
    
    with open('output.txt', 'a') as outputfile:
        outputfile.write(str(db_size + 1) +' '+str(timelapse_parallel) +' '+str(timelapse_serial) + '\n')    
    """
if __name__ == '__main__': 
    test()
    profile.run('re.compile("mapper")')