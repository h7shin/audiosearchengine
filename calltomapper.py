
def calltomapper(haystackmap, needle, processnumber, totalprocesses, return_emissions):
    
    """ calltomapper is a target function of a process from interface
    which in turn calls the method haystackmap.mapper with argument needle """
    
    print("Scanning .wav file ", str("{0:.2f}".format(int(processnumber)/int(totalprocesses)*100)),"%")
    return_emissions[processnumber] = haystackmap.mapper(needle)