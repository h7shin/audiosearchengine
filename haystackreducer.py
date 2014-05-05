from haystack import haystack

def haystackreducer(concatenated_emissions, key_names):
    """
        haystackreducer is a class responsible for reducing emissions
        from multiple map processes. It tallies the number of matches
        from key-value pairs emitted from each mapper
    """  
    
    join = {}
    for key in key_names:
        join[key] = len([1 for x in concatenated_emissions if x[0] == key]) 
    return join
    