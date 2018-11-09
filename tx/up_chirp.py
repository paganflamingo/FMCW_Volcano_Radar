## Waveform Generator - Andrew Xi, Matthew Lee - ASU

import numpy as np
import matplotlib.lines
import matplotlib.pyplot as plt

## Parameters
# Here we define relevant parameters. Not all will be used in the design.

clk_dac = 50e6                        	# The ROACH will be clocked at 50 MHz
bw_dac = clk_dac / 2
bw_signal = 1e6                        	# The pre-multiplication signal will have a bandwidth of 1 MHz
bw_chirp = 16 * bw_signal
pi = np.pi
## Find chirp period

d = 50e3                               	# The maximum expected object distance will be 50 km
c = 3e8                                	# Speed of light
dt = 2*d / c
T = 2*dt                               	# The theoretical period will be double the time delay between signal transmission and reception

## Find chirp rate

a = bw_chirp / T

## Find FFT parameters

bins = 2 ** 14
f_bin = bw_dac / bins                 	# Frequency range of each bin
d_bin = c*f_bin / (2*a)                	# Distance represented by each bin

## Signal frequency

t_clk = 1/clk_dac                     	# Clock period

#t = 0:t_clk/2:T                        
t = np.arange(0,T,t_clk/2)		# Create an array from 0 s to chirp period

#s = 0:(1e6)/(clk_dac*T)/2:1e6         	
s = np.linspace(0,1e6,len(t))		# Create vector from 0 MHz to 1 MHz with same length as t
s += 1e6                             	# Shift frequencies to 10 MHz to 11 MHz

## Define chirp

w = 2*pi*s                             	# Frequency of chirp in rad/s
chirp = np.sin(w*t)                      	# Chirp signal as amplitude vs time


## Uncomment the below to view the plots of a single chirp

'''
fig = plt.figure()
plot1 = fig.add_subplot(2,1,1)
line1, = plot1.plot(t, np.zeros(len(t)), '#FF4500', alpha = 0.8)
line1.set_marker('.')
plt.grid()
line1.set_ydata(chirp)
fig.canvas.draw()

#not sure how to have the plots out
plt.subplot(2,1,1)
plt.plot(t,chirp,'-')
plt.xlim([0,T])
plt.title('Signal')
plt.ylabel('Amplitude')
plt.xlabel('Time (s)')
subplot(2,1,2)
plt.plot(t,s,'r-')
plt.xlim([0,T])
plt.title('Frequency')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
'''

## Split into even and odd vectors

S0 = chirp[1:65536:2]			#From chirp, slice odd index by starting from index of 1
S1 = chirp[0:65536:2]			#Slice even index, starting index of 2, since we have extra even index

# Uncomment the below to view the size of each vector

# print(len(S0))
# print(len(S1))

## Calculate period of chirp

n_datapoints = len(S0)
T_chirp = 2 * n_datapoints / clk_dac

T_return = T * 1.25
