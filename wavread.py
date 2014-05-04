from wavsound import wavsound

"""wavread is a testing module to test the functionality of wavsound"""

button_wavsound = wavsound('db/button.wav')
print(button_wavsound)

beep_wavsound = wavsound('db/buttonresampled.wav')
print(beep_wavsound)
print (len(button_wavsound.get_data()))
print (len(beep_wavsound.get_data()),len(button_wavsound.get_data()))
print(button_wavsound.get_chunk(0,100))