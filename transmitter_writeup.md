# Transmitter
This write–up concerns the current progress on the transmitter portion of the radar.

## 1. Components
The setup used the following components:

|Name|Quantity|
|:---|---:|
|ROACH2|1|
|Signal Generator|1|
|High Speed Oscilloscope|1|
|Power Splitter (1/2)|1|
|Music Board DAC/ADC|1|

## 2. Setup
The compiled bitstream was uploaded using iPython:
```python
import casperfpga					#import casperfpga library
fpga = casperfpga.KatcpFpga('192.168.40.67')		#connect to ROACH2 using IP
fpga.upload_to_ram_and_program('/path/to/file.fpg')	#upload to RAM
fpga.listdev()						#list available variables

fpga.write_int('dac_reset',1)				#reset (1 is press, 0 is release)
fpga.write_int('dac_reset',0)

fpga.write_int('start_dac',0)
fpga.write_int('start_dac',1)				#enable DAC
```

The signal generator parameters were calculated using a desired 0 dBm clock signal. Based on the 50 ohm impedance, this yielded the following parameters

|Parameter||
|:---|---:|
|Voltage|600 mVpp*|
|Frequency|20kHz|

<sub>*The voltage here was double the normal expected voltage due to us using a 1/2 power splitter. In addition, we used 1.2 Vpp in our signal generator due to the fact that its output was half of the expected value.</sub>

The signal generator output was connected to the power splitter, which was connected to the clock input of the DAC/ADC board. The output of the DAC side was connected directly to the oscilloscope.

## 3. Waveform
The output waveform uploaded was a simple sine wave.
![Sine Waveform](https://i.imgur.com/a4cmzpB.jpg)

## 4. Next Steps
We need to change the waveform on the ROM to the chirp generated in MATLAB. However, currently the .slx design does not compile when using a MATLAB vector handle, and we may need to directly use the expression that generates the vector instead.

In addition, we need to create another waveform which does not have a sawtooth frequency characteristic, but rather a "hill" which consists of the sawtooth for one period and then the same chirp backwards for the consecutive period.
