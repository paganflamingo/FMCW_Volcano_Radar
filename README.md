# FMCW_Volcano_Radar
## Introduction
2018-2019 Barrett Honors Thesis for [Andrew Xi](andrew.xi@asu.edu) and [Matthew Lee](matthewlee@asu.edu)

This repository contains the MATLAB and Python code used for the volcanic ash radar. The radar is built using a
Collaboration for Astronomy Signal Processing and Electronics Research ([CASPER](https://casper.berkeley.edu/wiki/Main_Page)) field-programmable gate array
(FPGA) named the Reconfigurable Open Architecture Computing Hardware 2 (ROACH2).

This project is directed by [Dr. Christopher Groppi](cgroppi@asu.edu) with the School of Earth and Space Exploration ([SESE](https://sese.asu.edu/)) with the assistance of [Dr. Philip Mauskopf](philip.mauskopf@asu.edu), also of SESE. It is also directly aided by [Samuel Gordon](sbg2133@gmail.com) and [Adrian Sinclair](aksincla@asu.edu).

## Files
[parameters.m](https://github.com/powerfulmandrew/FMCW_Volcano_Radar/blob/master/parameters.m) contains the calculations used to define the parameters of the radar.

[waveform.m](https://github.com/powerfulmandrew/FMCW_Volcano_Radar/blob/master/waveform.m) contains the code used to generate the chirp waveform vectors.

[chirpwaveform.dat](https://github.com/powerfulmandrew/FMCW_Volcano_Radar/blob/master/chirpwaveform.dat) contains the two signal vectors in a MATLAB .dat file format. This can be used to directly load the data into MATLAB without having to regenerate the data.
