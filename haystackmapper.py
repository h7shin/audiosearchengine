from haystack import haystack


class haystackmapper:
    
    """
    haystackmapper is a class responsible for map process, 
    it emits key-value pair if a needle can be found in the haystack
    (key: haystack name, value: 1 represents a match)
    """
    
    emission = []
    def __init__ (self, haystacks):
        self.haystacks = haystacks
    def mapper (self, needle):
        len_needle = len(needle)
        emission = []
        for haystack in self.haystacks:
            len_haystack = haystack.get_length()
            data = haystack.get_data()
            for i in range(len_haystack):
                 
                #get subsequence length
                len_sub = min(len_needle, (len_haystack - i)) 
                
                subsequence = data[i:i + len_needle]
                nomatch = 0
                """ 
                Uncomment this for debugging:                 
                #difference = []
                """
                
                if len_sub <= 1:
                    nomatch = 1
                    break
                for i in range(len_sub): # len_sub <= len_needle
                    """ 
                    Uncomment this for debugging: 
                    if abs(needle[i]) > 100 :
                        difference.append(abs(subsequence[i] - needle[i])/needle[i] )
                    else:
                        difference.append(0)
                    """
                    if abs(needle[i]) > 100 and abs(subsequence[i] - needle[i]) > abs(0.05*needle[i]): 
                        # allow slight variation
                        nomatch = 1
                        break
                
                if nomatch == 0:
                    
                    """ 
                    Uncomment this section for deubgging to show comparison
                    print(needle)
                    print(subsequence)
                    print(difference)
                    print(haystack.get_name(),nomatch)
                    """
                    
                    emission.append([haystack.get_name(), 1])
                    break
                else:
                    pass
        
        return emission

