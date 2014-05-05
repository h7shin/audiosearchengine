audiosearchengine
=================

Search for audio .wav files based on percent match in the audio file database

Place query wav file in the top level directory where interfacePython3Plus.py is stored.
Run search by running interfacePython3Plus.py. You can also add .wav files to the
db directory (database). 

Please note that the algorithm is designed for Python Version 3.X.X. (interfacePython3Plus.py).

If possible, run interfacePython3Plus.py with python3 command.

Example:

	.WAV Search Engine Version 1 (For Python Ver. 3+) 
	Submit .wav file to search against database (Example: button.wav): button.wav

	**Higher number of partitions increases false positive rates, 
	while lower number of partitions increases false negative rates

	Set number of partitions of the query from 1 to 2862: 2000
	Set number of samples (n) of partitions from 1 to 2000: 20
	Set maximum number of split databases :2
	Finished with process  0  of  40
	Finished with process  1  of  40
	Finished with process  2  of  40
	Finished with process  3  of  40
	Finished with process  4  of  40
	Finished with process  5  of  40
	Finished with process  6  of  40
	Finished with process  7  of  40
	Finished with process  8  of  40
	Finished with process  9  of  40
	Finished with process  10  of  40
	Finished with process  11  of  40
	Finished with process  12  of  40
	Finished with process  13  of  40
	Finished with process  14  of  40
	Finished with process  15  of  40
	Finished with process  16  of  40
	Finished with process  17  of  40
	Finished with process  18  of  40
	Finished with process  19  of  40
	Search Result:
	db/clonebutton_cut.wav :      95.0 % match
	db/buttonframeshift.wav :     100.0 % match
	db/clonebutton.wav :          100.0 % match
	db/button.wav :               100.0 % match
	db/buttonresampled.wav :      100.0 % match
	4.69403600692749 seconds

The above program is run under SONY VAIO VPCE Model Ci5 4GB RAM 2.27GHz Dual Core Procesor
