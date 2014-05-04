from haystackmapper import haystackmapper 
from haystackreducer import haystackreducer
from haystack import haystack
from needlestorage import needlestorage
from wavsound import wavsound
from multiprocessing import Pool, Process, Manager
from calltomapper import calltomapper
import time

""" dbtest is a simulation module to measure time complexity of 
database search applied to a virtual database"""

if __name__ == '__main__': 
    button_wavsound = wavsound('button.wav')
    
    haystacks = []   # Database Structure

    db_size = 10     # Set Database Size
    
    for i in range(db_size):
        haystacks.append(haystack(i,button_wavsound.get_data()))
    
    haystacks.append(haystack("7",[1, 2, 3, 4, 5]))
        
    button_needle_factory = needlefactory(button_wavsound,1000,50)
    emissions = []
    
    haystackmap = haystackmapper(haystacks)
    
    print("USING MAP PROCESS and Manager")
    needles = button_needle_factory.get_needles()
    manager = Manager()
    return_emissions = manager.dict()    
    jobs = []
    pnum = 0
    
    print ("Number of Needles: ",len(needles))
    start_time = time.time()
    
    for needle in needles:
        p = Process(target=calltomapper, args=(haystackmap,needle,pnum,return_emissions))
        jobs.append(p)
        p.start()
        pnum += 1
    
    for proc in jobs:
        proc.join() 
    
    emissions_list = sum(return_emissions.values(),[])
    print("Reduce Result:")    
    print(haystackreducer(emissions_list ))        
    print("Done")
    timelapse_parallel = time.time() - start_time
    
    
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
   
    print("Long Way")
    start_long_time = time.time()
    haystackmap.clear_emission()
    i = 10000
    while i > 0:
        needle = button_needle_factory.pop_unused_needle()
        if (needle == []):
            break
        emissions = emissions + haystackmap.mapper(needle)
        i -= 1
        print("Total So Far: ",len(emissions))
    
    print("Final:",haystackreducer(emissions))
    timelapse_serial = time.time() - start_long_time
    print (db_size + 1, timelapse_parallel, timelapse_serial)
    
    with open('output.txt', 'a') as outputfile:
        outputfile.write(str(db_size + 1) +' '+str(timelapse_parallel) +' '+str(timelapse_serial) + '\n')    