
class haystack:
    
    """ haystack represents a single entry in the database 
    it contains a sequence of integers """
    
    name=''

    def __init__(self,name,data):
        self.name=name
        self.data=data
        self.length = len(data)
        
    def get_data(self):
        return self.data

    def get_name(self):
        return self.name
    
    def get_length(self):
        return self.length