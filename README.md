# FMCW_Volcano_Radar
2018-2019 Barrett Honors Thesis for [Andrew Xi](https://isearch.asu.edu/profile/1787656) (<andrew.xi@asu.edu>) and [Matthew Lee](https://isearch.asu.edu/profile/2859444) ([GitHub](https://github.com/Thisismatt)) (<matthewlee@asu.edu>), both students of the School of Electrical, Energy, and Energy Engineering ([ECEE](https://ecee.engineering.asu.edu/)) at Arizona State University ([ASU](https://asu.edu))

## Introduction

This repository contains the MATLAB and Python code used for the volcanic ash radar. The radar is built using a
Collaboration for Astronomy Signal Processing and Electronics Research ([CASPER](https://casper.berkeley.edu/wiki/Main_Page)) field-programmable gate array
(FPGA) named the Reconfigurable Open Architecture Computing Hardware 2 ([ROACH2](https://casper.berkeley.edu/wiki/ROACH2)).

This project is directed by [Dr. Christopher Groppi](https://isearch.asu.edu/profile/1399420) (<cgroppi@asu.edu>) with the School of Earth and Space Exploration ([SESE](https://sese.asu.edu/)) with the assistance of [Dr. Philip Mauskopf](https://isearch.asu.edu/profile/1863516) (<philip.mauskopf@asu.edu>), also of SESE. It is also directly aided by [Samuel Gordon](https://isearch.asu.edu/profile/2331576) and [Adrian Sinclair](https://isearch.asu.edu/profile/1536050).

## Files
[parameters.m](parameters.m) contains the calculations used to define the parameters of the radar.

[waveform.m](waveform.m) contains the code used to generate the chirp waveform vectors.

[chirpwaveform.dat](chirpwaveform.dat) contains the two signal vectors in a MATLAB .dat file format. This can be used to directly load the data into MATLAB without having to regenerate the data. To load in MATLAB, use

```matlab
chirp = load('chirpwaveform.dat');
S0 = chirp(:,1);
S1 = chirp(:,2);
```
