from run import *

if __name__ == '__main__': 
    print (".WAV Search Engine Version 1 (For Python Ver. 3+) ")
    
    good_file = 0
    
    while (good_file == 0):
        query     = input("Submit .wav file to search against database (Example: button.wav): ")
        if (os.path.isfile(query)):
            good_file = 1    
        query_wavsound = wavsound(query)    
                
    print("\n**Higher number of partitions increases false positive rates, \nwhile lower number of partitions increases false negative rates\n")
    samplelength = input("Set word size (sample length) (5 ~ 100) : ");
    partition = str(int(len(query_wavsound.get_data())/float(samplelength)))
    samples   = input("Set number of samples (n) of partitions from 1 to " + partition + ": ")
    
    # Database look up directory
    
    dbdir    = input("Enter database directory to search (example: 'db') : ")
    max_split = int(input("Set maximum allowable number of split databases : "))
    
    # Database query time
    start_time = time.time()        
            
    result_lst = run(query, str(partition), samples, dbdir, max_split)
            
    # output
    output = "Search Result: \n" 
            
    # Tabulate % match (wav files with 0% match are excluded from the result)
    for pair in result_lst:
        output += pair[0] + " : " + (40-len(pair[0]))*" " + pair[1] + "% match" + "\n"
                        
        # Show search time
        timelapse_parallel = time.time() - start_time   
        output = output + str(timelapse_parallel) + "seconds"
    print(output)