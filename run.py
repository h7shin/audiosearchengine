from haystackmapper import haystackmapper 
from haystackreducer import haystackreducer
from haystack import haystack
from needlestorage import needlestorage
from wavsound import wavsound
from multiprocessing import Pool, Process, Manager
from calltomapper import calltomapper
from calltoreducer import calltoreducer
from operator import itemgetter
import time
import os

def run(query, sample_length, samples, rootdir, max_split):
    
    """ run runs the repository search taking three user inputs, the query wav file,
   sample_length, and number of partition samples"""
    
    
    #Instantiate Wavsound objects from the wav files
    
    t_wavsounds = {}
    query_wavsound = wavsound(query)    
    
    # repository Structure
    
    haystackss = []   # split repository into list of smaller repository
    key_names = []

    # repository Spliting Parameters (1 to number of repository entries)
    
    db_size_per_split = 100
    
    for i in range(max_split):
        haystackss.append([])    
    
    # Read Files in the DB
    
    counter = 0
    for subdir, __, files in os.walk(rootdir):
        for file in files:
            key_names.append(subdir+"/"+file)
            split_db_key = min(max_split, int(counter / db_size_per_split))
            t_wavsounds[subdir+"/"+file] = wavsound(subdir+"/"+file)
            haystackss[split_db_key].append(haystack(subdir+"/"+file,t_wavsounds[subdir+"/"+file].get_data()[::16]))
            counter += 1
            
    query_needle_factory = needlestorage(query_wavsound,sample_length,int(samples))
    
    # Get segments of the query data as needles
    needles = query_needle_factory.get_needles()
    #print("...", len(needles), "needles")
    query_needle_factory.clear_needles()
    
    # MAP --------------------------------------------------
    
    # Manager to keep track of all map results
    manager = Manager()
    
    # Map processes emit key-value pairs to emissions
    return_emissions = manager.list()    
    
    # Job is a list of processes
    jobs = []
    
    # Process number
    pnum = 0
            
    #Distribute processes using multiprocessor
    len_needles = len(needles)
    for needle in needles:
        for haystacks in haystackss:
            if haystacks != []:
                #print(len_needles)
                p = Process(target=calltomapper, args=(haystacks,needle,pnum,len_needles*len(haystackss),return_emissions))
                jobs.append(p)
                p.start()
                pnum += 1
    
    for proc in jobs:
        proc.join() 
        
    # SHUFFLE ------------------------------------------------
    
    # Job is a list of processes
    jobs = []     
    
    # Manager to keep track of all map results
    manager_2 = Manager()    
    result_dict = manager_2.dict()
        
    for key in key_names:
        key_list = [1 for x in return_emissions if x[0] == key]
        #print (key, key_list)
        q = Process(target=calltoreducer, args=(key_list, key, result_dict))
        jobs.append(q)
        q.start()
        
    for proc in jobs:
        proc.join()         
            
    # REDUCE ---------------------------------------------------
    
    result_lst = []
    
    if len(result_dict.items()) != 0:
        for key, value in sorted(result_dict.items(), key=lambda pair: pair[1], reverse=True):
            if value > 0:
                result_lst.append([str(key), str((int(value)/len(needles)*100))])
            
    needles = []
    return result_lst
