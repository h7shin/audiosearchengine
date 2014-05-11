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
    partition = input("Set number of partitions of the query from 1 to " + str(int(len(query_wavsound.get_data())/3))+": ")
    samples   = input("Set number of samples (n) of partitions from 1 to " + partition + ": ")
    
    # Database look up directory
    
    rootdir    = input("Enter database directory to search (if unsure type 'db') : ")
    max_split = int(input("Set maximum allowable number of split databases : "))
    
    output = run(query, partition, samples, rootdir, max_split)
    print(output)