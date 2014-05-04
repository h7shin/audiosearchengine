from haystackmapper import haystackmapper 
from haystackreducer import haystackreducer
from haystack import haystack
from multiprocessing import Pool, Process,  Manager
from simplfunction import simplefunction
from calltomapper import calltomapper

if __name__ == '__main__':  
    
    """Map reduce test is a simple testing module to check functionality
    of map-reduce implementation"""
    
    haystacks = []
    haystacks.append(haystack("0",[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    haystacks.append(haystack("1",[3, 2, 2, 3, 4, 3, 6, 7, 8, 9]))
    haystacks.append(haystack("2",[1, 6, -1, 0, 4, 0, 6, 7, 8, 9]))
    haystacks.append(haystack("3",[3, 3, 3]))
    
    haystackmap = haystackmapper(haystacks)
    
    emissions= []
    
    print("USING MAP POOL") 
    pool = Pool(2) # if it is a quad-core machine it can be set to 4
    emissions = pool.map(haystackmap.mapper, [[2],[3]])
    print(emissions) 
    print(haystackreducer(sum(emissions,[])))
    emissions= []
    
    print("USING MAP PROCESS 1 ")
    p = Process(target=simplefunction, args=(1,2))
    p.start()
    p = Process(target=simplefunction, args=(1,3))
    p.start()
    p = Process(target=simplefunction, args=(1,4))
    p.start()
    p.join()
    
    print("USING MAP PROCESS and Manager")
    needles = [2, 3]
    manager = Manager()
    return_emissions = manager.dict()    
    jobs = []
    pnum = 0
    for needle in needles:#distributive not iteration
        p = Process(target=calltomapper, args=(haystackmap,[needle],pnum,return_emissions))
        jobs.append(p)
        p.start()
        pnum += 1
    
    for proc in jobs:
        proc.join()   
    
    emissions_list = sum(return_emissions.values(),[])
    print(haystackreducer(emissions_list ))
    
    
    print("USING MAP PROCESS 3")
    for needle in [[2],[3]]:
        Process(target=haystackmap.mapper, args=(needle,)).start()
    print(haystackmap.get_emission())
    haystackmap.clear_emission()
    
    
    print("Long Way")  
    
    needles = [2, 3]
    haystackmap = haystackmapper(haystacks)
    for needle in needles:#distributive not iteration
        #print (needle)
        emissions = emissions + haystackmap.mapper([ needle ])
    print(haystackreducer(emissions))