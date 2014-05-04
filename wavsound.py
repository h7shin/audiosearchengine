import wave, struct

class wavsound:
    
    """wavsound object collects data from a wav file and stores it
    as a list of integers """
    
    def __init__(self, wav_file):
        self.data = []# set it as a local variable
        if wav_file == '':
             return
        print(wav_file)
        waveFile = wave.open(wav_file, 'r')
        length = waveFile.getnframes()
        for i in range(0,length):
            waveData = waveFile.readframes(1)
            data = struct.unpack("<h", waveData)
            self.data.append(int(data[0]))
            
    # return data    
    def get_data(self):
        return self.data
    
    # set data from a list of int
    def set_data(self, data):
        self.data = data  
    
    # copy data from other wavsound
    def copy_from(self, other_wavsound: 'wavsound'):
        self.data = other_wavsound.get_data()    
    
    # Get a small chunk of wavsound
    def get_chunk (self, section_no, num_chunk):
        new_wavsound = wavsound('')
        data = self.get_data()
        #print(len(self.get_data()))
        length = int(len(self.get_data())/num_chunk)
        #print(length)
        new_wavsound.set_data(data[(length*section_no):(length*(section_no+1))])
        return new_wavsound
    def __repr__(self):
        strr = ''
        for i in self.data:
            strr = strr + " " + str(i)
        return strr
    