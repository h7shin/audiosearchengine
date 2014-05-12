audiosearchengine
=================

Requirements

	*Python Ver. 3.X.X
	*python-tk package for GUI application
	*X11 (for Cygwin) or XQuartz installed (for Mac) when using GUI application
	*WAV audio file (.wav) format: signed mono 16 bit PCM
		Use .wav converters online, and if neccessary re-sample the audio files
		using Audacity Opensource Software 
		For UNIX users, you may also use SoX to add .wav header to raw bit stream data

Do you have any screenshots?
	
	screenshot.png is available in img directory

What does your program do?

	Suppose a student has a recorded section of some audio file, but
	he/she cannot remember the song name or the ring-tone name. He/she can search
	for similar audio files in the database with the best waveform alignments. 
	
	You can adjust the level of stringency to balance the speed and quality of
	the search.
	
	The algorithm implements a Map-Reduce pattern with multiple map processes
	that run in parallel.

Python Libraries Used

	tkinter (for GUI)
	multiprocessing

How to use

	You can run either interfaceCLI.py and interfaceGUI.py. interfaceCLI.py is for
	command line use and interfaceGUI.py is for GUI. On the GUI application,
	you can also compare the two waveforms.

	Place query wav file in the top level directory where interfaceCLI.py is stored.
	Run search by running interfaceCLI.py. You can also add .wav files to the
	db directory (database). 

	Please note that the algorithm is designed for Python Version 3.X.X. (interfaceCLI.py).
	If possible, run interfaceCLI.py with python3.

