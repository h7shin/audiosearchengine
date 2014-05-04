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
        emission = []
        len_needle = len(needle)
        for haystack in self.haystacks:
            for i in range(haystack.get_length()):
                data = haystack.get_data()
                
                #get subsequence length
                len_sub = min(len_needle, (haystack.get_length() - i)) 
                
                subsequence = data[i:i + len_needle]
                nomatch = 0
                #difference = []
                if len_sub <= 1:
                    nomatch = 1
                    break
                for i in range(min(len_sub,len_needle)):
                    if abs(needle[i]) > 100 :
                        pass
                        # Uncomment this: difference.append(abs(subsequence[i] - needle[i])/needle[i] )
                    else:
                        pass
                        # Uncomment this: difference.append(0)
                    if abs(needle[i]) > 100 and abs((subsequence[i] - needle[i])/(needle[i])) > 0.05: 
                        # allow slight variation
                        nomatch = 1
                        break
                
                if nomatch == 0:
                    
                    """ 
                    Uncomment this section to show comparison
                    print(needle)
                    print(subsequence)
                    print(difference)
                    print(haystack.get_name(),nomatch)
                    """
                    
                    emission.append([haystack.get_name(), 1])
                    break
                else:
                    pass
        # self.emission = self.emission + emission
        # if debug print("Number of Emissions:",len(self.emission))
        
        return emission
    def mapper_queue (self, needle, queue):
        queue.puts(self.mapper(needle))
    def get_emission(self):
        return self.emission
