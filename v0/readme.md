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
