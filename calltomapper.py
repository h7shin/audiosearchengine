from haystackmap import mapper

def calltomapper(haystacks, needle, processnumber, totalprocesses, return_emissions):
    
    """ calltomapper is a target function of a process from interface
    which in turn calls the method haystackmap.mapper with argument needle """
    
    print("Finished with process ", processnumber, " word(sample) size of ",len(needle))
  
    return_emissions += mapper(haystacks, needle)