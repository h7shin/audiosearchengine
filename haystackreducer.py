from haystack import haystack

def haystackreducer(concatenated_emissions):
    """
        haystackreducer is a class responsible for reducing emissions
        from multiple map processes. It tallies the number of matches
        from key-value pairs emitted from each mapper
    """  
    
    join = {}
    for key_value_pair in concatenated_emissions:
        if key_value_pair[0] in join:
            join[key_value_pair[0]] = join[key_value_pair[0]] + key_value_pair[1]
        else:
            join[key_value_pair[0]] = key_value_pair[1]
        #print(join)
    return join
    