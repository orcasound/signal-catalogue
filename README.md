# signal-catalogue
A place to build and store humpback and orca signal catalogues 

## Goals

1. Specify a directory of audio files, each a FLAC file containing a single example of a signal.
2. Pre-process the raw audio to optimize the spectrogram for human listeners.
3. Generate a spectrogram of each FLAC file.
4. Convert each signal clip to an audio format optimal for browser-base playback.
5. Display the spectrograms with signal labels in a HTML5-based user interface that allows playback via the audio element.

## Architecture

###Future questions:

* How to deploy to a web domain like humpbackcat.net (and code/architectural implications --> containerization)
