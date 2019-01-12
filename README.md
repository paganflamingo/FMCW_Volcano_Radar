# FMCW_Volcano_Radar
2018-2019 Barrett Honors Thesis for [Andrew Xi](mailto:andrew.xi@asu.edu) and [Matthew Lee](mailto:matthewlee@asu.edu) ([GitHub](https://github.com/Thisismatt)), both electrical engineering students of the School of Electrical, Energy, and Energy Engineering ([ECEE](https://ecee.engineering.asu.edu/)) at Arizona State University ([ASU](https://asu.edu))

## Introduction

This repository contains the MATLAB and Python code used for the volcanic ash radar. The radar is built using a
Collaboration for Astronomy Signal Processing and Electronics Research ([CASPER](https://casper.berkeley.edu/wiki/Main_Page)) field-programmable gate array
(FPGA) named the Reconfigurable Open Architecture Computing Hardware 2 ([ROACH2](https://casper.berkeley.edu/wiki/ROACH2)).

This project is directed by [Dr. Christopher Groppi](mailto:cgroppi@asu.edu) with the School of Earth and Space Exploration ([SESE](https://sese.asu.edu/)) with the assistance of [Dr. Philip Mauskopf](mailto:philip.mauskopf@asu.edu), also of SESE. It is also directly aided by [Samuel Gordon](mailto:sbg2133@gmail.com) and [Adrian Sinclair](mailto:aksincla@asu.edu).

## Files

### General

[parameters.m](parameters.m) contains the calculations used to define the parameters of the radar.

[upload.py](upload.py) contains a basic Python script used for uploading compiled .fpg files to the RAM of the ROACH2.

[trans_spec_v0.fpg](trans_spec_v0.fpg) is the compiled design for uploading to the ROACH2 FPGA.

### Transmitter files

[transmitter_writeup.md](v0/tx/transmitter_writeup.md), completed on 10/4/2018, contains a description of the current progress on the transmitter.

[waveform.m](v0/tx/waveform.m) contains the code used to generate the chirp waveform vectors. The waveform has a sawtooth frequency vs time shape.

[up_chirp.py](v0/tx/up_chirp.py) creates the same waveform as [waveform.m](v0/tx/waveform.m) in Python script.

[updown_chirp.py](v0/tx/updown_chirp.py) creates a mirrored version of the waveform in [updown_chirp.py](v0/tx/updown_chirp.py).

[chirpwaveform.dat](v0/tx/chirpwaveform.dat) contains the two signal vectors in a MATLAB .dat file format. This can be used to directly load the data into MATLAB without having to regenerate the data. To load in MATLAB, use

```matlab
chirp = load('chirpwaveform.dat');
S0 = chirp(:,1);
S1 = chirp(:,2);
S0 = transpose(S0);
S1 = transpose(S1);
% S0 and S1 now contain the signal vectors to be uploaded into ROM0 and ROM1, respectively
```

### Receiver files

[spectrometer_writeup.md](v0/spectrometer/spectrometer_writeup.md), completed on 11/2/2018, contains a description of the heretofore completed work.

[firmware_registers.txt](v0/spectrometer/firmware_registers.txt) contains the definition of certain variable handles for the Python function scripts.

[spec_plot.py](v0/spectrometer/spec_plot.py) is the Python script for uploading the design to the ROACH2 as well as plotting the FFT. To run, download all three receiver files, then change the paths in [spec_plot.py](v0/spectrometer/spec_plot.py) to find the files, then use

```python
run /path/to/spec_plot.py
```

[dynamic_plot.py](v0/spectrometer/dynamic_plot.py) is the Python script to read and plot the spectrum of the input signal. It is different from [spec_plot.py](v0/spectrometer/spec_plot.py) in that this script will have parameters for the functions such as plotFFT and plotADC. The same approach is used to run this script.

```python
run /path/to/dynamic_plot.py
```
