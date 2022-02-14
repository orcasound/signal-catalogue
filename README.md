# signal-catalogue
A place to build and store humpback and orca signal catalogues (aka catalogs)

## Goals

1. Specify a directory of audio files, each a FLAC file containing a single example of a signal.
2. Pre-process the raw audio to optimize the spectrogram for human listeners.
3. Generate a spectrogram of each FLAC file.
4. Convert each signal clip to an audio format optimal for browser-base playback.
5. Display the spectrograms with signal labels in a HTML5-based user interface that allows playback via the audio element.

## Architecture

Version 1:

* Simple flat HTML site that can be generated locally and viewed/used in your favorite browser
* index.html with single example of each signal
* Individual pages with unique URLs for each signal type?
* Where to store and whether to display "extra" examples of each signal (limit how many?), and/or "dirty" examples (e.g. with low SNR or variable/aberrant versions?)

### Future questions:

* How to deploy to a web domain like humpbackcat.net (and code/architectural implications --> containerization)
