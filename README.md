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

		.WAV Search Engine Version 1 (For Python Ver. 3+) <br>
		Submit .wav file to search against database (Example: button.wav): button.wav <br>
		button.wav <br> <br>

		**Higher number of partitions increases false positive rates,  <br>
		while lower number of partitions increases false negative rates <br> <br>

		Set number of partitions of the query from 1 to 2862: 1000 <br>
		Set number of samples of partitions from 1 to 1000 (Recommend < 50): 50 <br>
    Scanning .wav file  0.00 % <br>
    Scanning .wav file  2.00 % <br>
    Scanning .wav file  4.00 % <br>
    Scanning .wav file  6.00 % <br>
    Scanning .wav file  8.00 % <br>
    Scanning .wav file  10.00 % <br>
    Scanning .wav file  12.00 % <br>
    Scanning .wav file  14.00 % <br>
    Scanning .wav file  16.00 % <br>
    Scanning .wav file  18.00 % <br>
    Scanning .wav file  20.00 % <br>
    Scanning .wav file  22.00 % <br>
    Scanning .wav file  24.00 % <br>
    Scanning .wav file  26.00 % <br>
    Scanning .wav file  28.00 % <br>
    Scanning .wav file  30.00 % <br>
    Scanning .wav file  32.00 % <br>
    Scanning .wav file  34.00 % <br>
    Scanning .wav file  36.00 % <br>
    Scanning .wav file  38.00 % <br>
    Scanning .wav file  40.00 % <br>
    Scanning .wav file  42.00 % <br>
    Scanning .wav file  44.00 % <br>
    Scanning .wav file  46.00 % <br>
    Scanning .wav file  48.00 % <br>
    Scanning .wav file  50.00 % <br>
    Scanning .wav file  52.00 % <br>
    Scanning .wav file  54.00 % <br>
    Scanning .wav file  56.00 % <br>
    Scanning .wav file  58.00 % <br>
    Scanning .wav file  60.00 % <br>
    Scanning .wav file  62.00 % <br>
    Scanning .wav file  64.00 % <br>
    Scanning .wav file  66.00 % <br>
    Scanning .wav file  68.00 % <br>
    Scanning .wav file  70.00 % <br>
    Scanning .wav file  72.00 % <br>
    Scanning .wav file  74.00 % <br>
    Scanning .wav file  76.00 % <br>
    Scanning .wav file  78.00 % <br>
    Scanning .wav file  80.00 % <br>
    Scanning .wav file  82.00 % <br>
    Scanning .wav file  84.00 % <br>
    Scanning .wav file  86.00 % <br>
    Scanning .wav file  88.00 % <br>
    Scanning .wav file  90.00 % <br>
    Scanning .wav file  92.00 % <br>
    Scanning .wav file  94.00 % <br>
    Scanning .wav file  96.00 % <br>
    Scanning .wav file  98.00 % <br>
    db/beep-03.wav <br>
    db/beep-06.wav <br>
    db/beep-07.wav <br>
    db/beep-08b.wav <br>
    db/beep-10.wav <br>
    db/button.wav <br>
    db/buttonframeshift.wav <br>
    db/buttonresampled.wav <br>
    db/clonebutton.wav <br>
    db/clonebutton_cut.wav <br>
    Number of Needles:  50 <br>
    Search Result: <br>
    db/beep-10.wav :              2.00 % match <br>
    db/buttonframeshift.wav :     100.00 % match <br>
    db/beep-03.wav :              2.00 % match <br>
    db/button.wav :               100.00 % match <br>
    db/buttonresampled.wav :      100.00 % match <br>
    db/beep-06.wav :              2.00 % match <br>
    db/beep-08b.wav :             2.00 % match <br>
    db/beep-07.wav :              2.00 % match <br>
    db/clonebutton.wav :          100.00 % match <br>
    db/clonebutton_cut.wav :      98.00 % match <br>
    11.972685098648071 seconds
