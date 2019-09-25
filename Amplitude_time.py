import sys
import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
def read_audio(filename="aa.wav"):
	input_data = read('aa.wav')
	audio = input_data[1]
	print(input_data)
	data=np.array(input_data)
	# plot the first 1024 samples
	plt.plot(audio[0:1024])
	# label the axes
	plt.ylabel("Amplitude")
	plt.xlabel("Time")
	# set the title  
	plt.title("Sample Wav")
	# display the plot
	plt.show()
	data=data[:,0]
	return data



