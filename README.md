# FMCW_Volcano_Radar
2018-2019 Barrett Honors Thesis for [Andrew Xi](mailto:andrew.xi@asu.edu) and [Matthew Lee](mailto:matthewlee@asu.edu) ([GitHub](https://github.com/Thisismatt)), both electrical engineering students of the [School of Electrical, Energy, and Energy Engineering (ECEE)](https://ecee.engineering.asu.edu/) at [Arizona State University (ASU)](https://asu.edu)

## Introduction

This repository contains the MATLAB and Python code used for the volcanic ash radar. The radar is built using a
[Collaboration for Astronomy Signal Processing and Electronics Research (CASPER)](https://casper.berkeley.edu/wiki/Main_Page) field-programmable gate array
(FPGA) named the [Reconfigurable Open Architecture Computing Hardware 2 (ROACH2)](https://casper.berkeley.edu/wiki/ROACH2).

This project is directed by [Dr. Christopher Groppi](mailto:cgroppi@asu.edu) with the [School of Earth and Space Exploration (SESE)](https://sese.asu.edu/) with the assistance of [Dr. Philip Mauskopf](mailto:philip.mauskopf@asu.edu), also of SESE. It is also directly aided by [Samuel Gordon](mailto:sbg2133@gmail.com) and [Adrian Sinclair](mailto:aksincla@asu.edu).

## Files

### Thesis

[Thesis.pdf](Thesis.pdf) is the completed and submitted Barrett Undergraduate Honors Thesis for Spring 2019, titled **Frequency--Modulated Continuous--Wave Millimeter--Band Radar for Volcanic Ash Detection**.

[Thesis.zip](Thesis.zip) is the complete _LaTeX_ repository used to generate the PDF.

### General

[parameters.m](parameters.m) contains the calculations used to define the parameters of the radar.

[upload.py](upload.py) contains a basic Python script used for uploading compiled .fpg files to the RAM of the ROACH2.

### [V0](v0)

This folder contains previous progress of the radar.

### [V1](v1)

This folder contains previous progress of the radar.

### [V2](v2)

This folder contains current progress of the radar, including the bitstream for direct uploading to the FPGA.

[trans_spec_v2.fpg](v1/trans_spec_v2.fpg) is the .fpg bitstream file for uploading to the ROACH2 board. It contains the completed 10-11.5 MHz chirp waveform.

