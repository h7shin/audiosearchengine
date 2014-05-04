from haystack import haystack

class haystackmapper:
    
    """
    haystackmapper is a class responsible for map process, 
    it emits key-value pair if a needle can be found in the haystack
    (key: haystack name, value: 1 represents a match)
    """
    
    emission = []
    def __init__ (self, haystacks: 'list of haystack'):
        self.haystacks = haystacks
    def mapper (self, needle):
        emission = []
        for haystack in self.haystacks:
            for i in range(len(haystack.get_data())):
                data = haystack.get_data()
                subsequence = data[i:i + len(needle)]
                nomatch = 0
                difference = []
                if len(subsequence) == 1:
                    nomatch = 1
                    break
                for i in range(min(len(subsequence),len(needle))):
                    if abs(needle[i]) > 100 :
                        difference.append(abs(subsequence[i] - needle[i])/needle[i] )
                    else:
                        difference.append(0)
                    if abs(needle[i]) > 100 and abs(subsequence[i] - needle[i])/abs(needle[i]) > 0.05: 
                        # allow slight variation
                        nomatch = 1
                        break
                
                if nomatch == 0:
                    
                    """ 
                    Uncomment this section to show alignmnet
                    print(needle)
                    print(subsequence)
                    print(difference)
                    print(haystack.get_name(),nomatch)
                    """
                    
                    emission.append([haystack.get_name(), 1])
                    break
                else:
                    pass
        self.emission = self.emission + emission
        # if debug print("Number of Emissions:",len(self.emission))
        
        return emission
    def mapper_queue (self, needle, queue):
        queue.puts(self.mapper(needle))
    def get_emission(self):
        return self.emission
    def clear_emission (self):
        self.emission = []
