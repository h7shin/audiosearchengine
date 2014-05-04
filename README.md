audiosearchengine
=================

Search for audio .wav files based on percent match in the audio file database

Place query wav file in the top level directory where interfacePython3Plus.py is stored.
Run search by running interfacePython3Plus.py. You can also add .wav files to the
db directory (database). 

Please note that the algorithm is designed for Python Version 3.X.X. (interfacePython3Plus.py).
Although, a separate interface file for Python Version 2.X.X. (interface.py) was made
it cannot be guaranteed that all of the modules and built-in functions compatible with Version 3.X.X
will behave exactly as intended in the older version of Python.

If possible, run interfacePython3Plus.py with python3 command.

Example:

	.WAV Search Engine Version 1 (For Python Ver. 3+) 
	Submit .wav file to search against database (Example: button.wav): button.wav
	
	**Higher number of partitions increases false positive rates, 
	while lower number of partitions increases false negative rates
	
	Set number of partitions of the query from 1 to 2862: 2000
	Set number of samples (n) of partitions from 1 to 2000 (T = O(n)): 20
	Process .wav file  0.00 %
	Process .wav file  5.00 %
	Process .wav file  10.00 %
	Process .wav file  15.00 %
	Process .wav file  20.00 %
	Process .wav file  25.00 %
	Process .wav file  30.00 %
	Process .wav file  35.00 %
	Process .wav file  40.00 %
	Process .wav file  45.00 %
	Process .wav file  50.00 %
	Process .wav file  55.00 %
	Process .wav file  60.00 %
	Process .wav file  65.00 %
	Process .wav file  70.00 %
	Process .wav file  75.00 %
	Process .wav file  80.00 %
	Process .wav file  85.00 %
	Process .wav file  90.00 %
	Process .wav file  95.00 %
	Search Result:
	db/button.wav :               100.00 % match
	db/buttonresampled.wav :      100.00 % match
	db/clonebutton.wav :          100.00 % match
	db/clonebutton_cut.wav :      95.00 % match
	db/buttonframeshift.wav :     100.00 % match
	5.360306978225708 seconds
