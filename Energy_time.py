from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# read audio samples
# input_data = read("organfinale.wav")
# audio = input_data[1]
# plot the first 1024 samples

def calc_energy(audio):
	plt.plot(audio[1**5:1024])
	# label the axes
	plt.ylabel("Energy")
	plt.xlabel("Time")
	# set the title  
	plt.title("Sample Wav")
	# display the plot
	plt.show()

