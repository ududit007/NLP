import sys
from Amplitude_time import *

if len(sys.argv)>1:
	audio_data=read_audio(sys.argv[1])
else:
	audio_data=read_audio()

