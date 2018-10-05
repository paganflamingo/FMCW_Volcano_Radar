# FMCW_Volcano_Radar
2018-2019 Barrett Honors Thesis for [Andrew Xi](mailto:andrew.xi@asu.edu) and [Matthew Lee](mailto:matthewlee@asu.edu) ([GitHub](https://github.com/Thisismatt)), both students of the School of Electrical, Energy, and Energy Engineering ([ECEE](https://ecee.engineering.asu.edu/)) at Arizona State University ([ASU](https://asu.edu))

## Introduction

This repository contains the MATLAB and Python code used for the volcanic ash radar. The radar is built using a
Collaboration for Astronomy Signal Processing and Electronics Research ([CASPER](https://casper.berkeley.edu/wiki/Main_Page)) field-programmable gate array
(FPGA) named the Reconfigurable Open Architecture Computing Hardware 2 ([ROACH2](https://casper.berkeley.edu/wiki/ROACH2)).

This project is directed by [Dr. Christopher Groppi](mailto:cgroppi@asu.edu) with the School of Earth and Space Exploration ([SESE](https://sese.asu.edu/)) with the assistance of [Dr. Philip Mauskopf](mailto:philip.mauskopf@asu.edu), also of SESE. It is also directly aided by [Samuel Gordon](mailto:sbg2133@gmail.com) and [Adrian Sinclair](mailto:aksincla@asu.edu).

## Files
[parameters.m](parameters.m) contains the calculations used to define the parameters of the radar.

[waveform.m](tx/waveform.m) contains the code used to generate the chirp waveform vectors. The waveform has a sawtooth frequency vs time shape.

[chirpwaveform.dat](tx/chirpwaveform.dat) contains the two signal vectors in a MATLAB .dat file format. This can be used to directly load the data into MATLAB without having to regenerate the data. To load in MATLAB, use

```matlab
chirp = load('chirpwaveform.dat');
S0 = chirp(:,1);
S1 = chirp(:,2);
S0 = transpose(S0);
S1 = transpose(S1);
% S0 and S1 now contain the signal vectors to be uploaded into ROM0 and ROM1, respectively
```

[upload.py](upload.py) contains a basic Python script used for uploading compiled .fpg files to the RAM of the ROACH2.

## Updates

[transmitter_writeup.md](tx/transmitter_writeup.md), completed on 10/4/2018, contains a description of the heretofore completed work.

