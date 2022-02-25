#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import matplotlib.pyplot as plt
import librosa
import librosa.display
import IPython.display as ipd


# In[3]:


audio_fpath = "/Users/emilyvierling/Orcasound/Audio/"
wave_fpath = "/Users/emilyvierling/Orcasound/Wave_nocb/"
spec_fpath = "/Users/emilyvierling/Orcasound/Linear Specs_nocb/"
logspec_fpath = "/Users/emilyvierling/Orcasound/Log Specs_nocb/"
audio_clips = os.listdir(audio_fpath)
print("No. of .wav files in audio folder = ",len(audio_clips))


# In[4]:


n = 0
x, sr = librosa.load(audio_fpath+audio_clips[n], sr=44100)
spec_title = audio_clips[n].split(".")[0]
print(type(x), type(sr))
print(x.shape, sr)


# In[5]:


plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
plt.title(spec_title, fontsize = 20)
plt.ylabel("Amplitude (µPa)")
plt.xlabel("Time (s)")
plt.savefig(wave_fpath+"{}.jpg".format(spec_title))
plt.savefig(wave_fpath+"{}.png".format(spec_title))


# In[6]:


X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr,cmap='magma', x_axis='time', y_axis='hz')
plt.title(spec_title, fontsize =20)
plt.ylabel ("Frequency (Hz)")
plt.xlabel ("Time (s)")
plt.ylim(0, 6000)
plt.savefig(spec_fpath+"Linear Frequency Scaling {}.png".format(spec_title))
plt.savefig(spec_fpath+"Linear Frequency Scaling {}.jpg".format(spec_title))


# In[7]:


fig = plt.figure(figsize=(14, 5))
ax = fig.add_subplot(111)
ax.axes.get_xaxis().set_visible(True)
ax.axes.get_yaxis().set_visible(True)
ax.set_frame_on(True)
librosa.display.specshow(Xdb, sr=sr, cmap='magma', x_axis='time', y_axis='log')
plt.ylim(0, 6000)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Frequency (Hz)")
ax.set_title(spec_title + " Logarithmic Frequency Scaling", fontsize = 20)
plt.savefig(logspec_fpath+"Logarithmic Frequency Scaling {}.png".format(spec_title))
plt.savefig(logspec_fpath+"Logarithmic Frequency Scaling {}.jpg".format(spec_title))


# In[ ]:




