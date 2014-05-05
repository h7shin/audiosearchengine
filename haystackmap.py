def highmatch(haystack,needle):
    len_haystack = haystack.get_length()
    data = haystack.get_data()
    len_needle = len(needle)
    for i in range(len_haystack):
                 
        #get subsequence length
        len_sub = min(len_needle, (len_haystack - i)) 
                
        subsequence = data[i:i + len_needle]
        nomatch = 0
        
        #Uncomment this for debugging:                 
        difference = []
        
        #print(len_sub)
        if len_sub <= 1:
            return False
        
        nomatch = 0
        for i in range(len_sub): # len_sub <= len_needle
            
            """#Uncomment this for debugging: 
            if abs(needle[i]) > 100 :
               difference.append(abs(subsequence[i] - needle[i])/needle[i])
            else:
                difference.append(0)
            print(difference)"""
            
            if abs(needle[i]) > 100 and abs(subsequence[i] - needle[i]) > abs(0.05*needle[i]): 
                # 1. allow slight variation
                nomatch = 1
                break
        if (nomatch == 0):
            return True
    return False

def mapper (haystacks, needle):
    return [[haystack.get_name(), 1] for haystack in haystacks if highmatch(haystack,needle)]
    
    
