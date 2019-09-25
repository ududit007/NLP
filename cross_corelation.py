import numpy as np
#import librosa
import logging
from scipy.io import wavfile



rate2,test = wavfile.read('bird.wav')

#indices
testStart  = 6000;
testEnd    = 200000;

refStart   = testStart + 11000;
refEnd     = refStart + 2000 - 1;

testSig=test[testStart:testEnd]
refSig=test[refStart:refEnd]

refStartRel=refStart-testStart+1
refEndRel=refEnd-testStart+1

no_samples_test=testSig.shape[0]
no_samples_ref=refSig.shape[0]

xcorr=np.zeros((no_samples_test-no_samples_ref+1,1))
xcorr_norr=np.zeros((no_samples_test-no_samples_ref+1,1))


refSig_norm= np.linalg.norm(refSig)
#print(xcorr.shape[1])
for i in range(1,xcorr.shape[0]):
    testSig_samples=testSig[i:(i+no_samples_ref)]
    xcorr[i]=np.sum(np.multiply(testSig_samples,refSig))
#    norrFilt=(filt-np.mean(filt))/(np.std(filt))
    linalgnorm=np.linalg.norm(testSig_samples)
    xcorr_norr[i]=xcorr[i]/np.multiply(refSig_norm,linalgnorm)

xcorr_max_id=np.max(np.abs(xcorr_norr))

print(xcorr_max_id * 1000)
print('%')
