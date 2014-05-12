from haystack import haystack

def haystackreducer(emissions):
    """
        haystackreducer is a class responsible for reducing emissions
        from multiple map processes. It tallies the number of matches
        from key-value pairs emitted from each mapper
    """  
    return len(emissions) 
    