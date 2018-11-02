# Spectrometer
This write–up concerns the current progress on the spectrometer portion of the radar.

## 1. Components
The setup used the following components:

|Name|Quantity|
|:---|---:|
|ROACH2|1|
|Signal Generator|2|
|Power Splitter (1/2)|1|
|Music Board DAC/ADC|1|

## 2. Setup
The compiled bitstream was uploaded using iPython and running [spec_plot.py](spectrometer/spec_plot.py):
```python
run /path/to/spec_plot.py
```

The clock signal generator parameters used 0 dBm clock signal at 20kHz.

The input signal generator used a variable frequency and a 1 V<sub>pp</sub> amplitude.

The input signal was connected to one input port on the ADC portion of the DAC/ADC board. The clock signal setup was identical to that from the transmitter.

## 3. Plot
The resultant FFT plot contained 2 peaks, for the positive and negative frequency of the input signal.
![Sine Waveform](https://i.imgur.com/LSk9laW.png)

## 4. Next Steps
We need to change the size of the FFT from 1024 bins to 16384. We also need to find a way to make the FFT adjustable without the need to recompile.
