import matplotlib, time, struct
import numpy as np
import shutil
np.set_printoptions(threshold=np.nan)
matplotlib.use("TkAgg")
import matplotlib.lines
import matplotlib.pyplot as plt
import casperfpga 
import types
import logging
import glob  
import os
import sys
from scipy import signal
import scipy.fftpack

#Read names of registers from pre-defined txt file
regs = np.loadtxt("/home/andysey/Desktop/firmware_registers.txt", dtype = "str")

# Plots the ADC timestream
def plotADC():
	#Set up a window for plots	
	fig = plt.figure(figsize=(10.24,7.68))
	plot1 = fig.add_subplot(211)
	line1, = plot1.plot(np.arange(0,2048), np.zeros(2048), 'r-', linewidth = 2)
	plot1.set_title('I', size = 20)
	plot1.set_ylabel('mV', size = 20)
	plt.xlim(0,1024)
	plt.ylim(-600,600)
	plt.yticks(np.arange(-600, 600, 100))
	plt.grid()
	plot2 = fig.add_subplot(212)
	line2, = plot2.plot(np.arange(0,2048), np.zeros(2048), 'b-', linewidth = 2)
	plot2.set_title('Q', size = 20)
	plot2.set_ylabel('mV', size = 20)
	plt.xlim(0,1024)
	plt.ylim(-600,600)
	plt.yticks(np.arange(-600, 600, 100))
	plt.grid()
	plt.tight_layout()
	plt.show(block = False)
	
	count = 0
	stop = 1.0e8
	while count < stop:    
		
		time.sleep(0.1)
		fpga.write_int(regs[np.where(regs == 'adc_snap_ctrl_reg')[0][0]][1],0)
		time.sleep(0.1)
		fpga.write_int(regs[np.where(regs == 'adc_snap_ctrl_reg')[0][0]][1],1)
		time.sleep(0.1)
		fpga.write_int(regs[np.where(regs == 'adc_snap_ctrl_reg')[0][0]][1],0)    
		time.sleep(0.1)
		fpga.write_int(regs[np.where(regs == 'adc_snap_trig_reg')[0][0]][1],1)    
		time.sleep(0.1)
		fpga.write_int(regs[np.where(regs == 'adc_snap_trig_reg')[0][0]][1],0)
		time.sleep(0.1)

		adc = (np.fromstring(fpga.read(regs[np.where(regs == 'adc_snap_bram_reg')[0][0]][1],(2**10)*8),dtype='>h')).astype('float')
		adc /= (2**15)
		adc *= 550.

		I = np.hstack(zip(adc[0::4],adc[2::4]))
		Q = np.hstack(zip(adc[1::4],adc[3::4]))
		
		#Ipp = np.abs(np.max(I) - np.min(I)) 
		#Qpp = np.abs(np.max(Q) - np.min(Q))
		#print Ipp, Qpp
		
		line1.set_ydata(I)
		line2.set_ydata(Q)
		fig.canvas.draw()
		count += 1
	return

	#I suppose the number of bins is this fft_len, and the closest number to 5k we can get with powers of 2 is 4096, which is an initial length of the function
def plotFFT(fft_len=2**12, stop = 1e6):
	
	#Set up a window for plots	
	fig = plt.figure()
	plot1 = fig.add_subplot(111)
	line1, = plot1.plot(np.arange(0,1024,1), np.zeros(fft_len), '#FF4500', alpha = 0.8)
	line1.set_marker('.')
	line2, = plot1.plot(np.arange(1,1024,2), np.zeros(fft_len/2), 'purple', alpha = 0.8)
	line2.set_marker('.')
	plt.grid()
	plt.ylim(-10, 5000)
	plt.tight_layout()
	
	#runs for the desired number of bins
	count = 0 
	while(count < stop): 
		
		#Read data from register
		fpga.write_int(regs[np.where(regs == 'fft_snap_ctrl_reg')[0][0]][1],0)
		fpga.write_int(regs[np.where(regs == 'fft_snap_ctrl_reg')[0][0]][1],1)
		fft_snap = (np.fromstring(fpga.read(regs[np.where(regs == 'fft_snap_bram_reg')[0][0]][1],(2**9)*8),dtype='>i2')).astype('float')
		I0 = fft_snap[0::4]
		Q0 = fft_snap[1::4]
		I1 = fft_snap[2::4]
		Q1 = fft_snap[3::4]
		
		#From complex data, grab the amplitude
		mag0 = np.sqrt(I0**2 + Q0**2)
		mag0dB = 20*np.log10(mag0) #on dB scale
		mag1 = np.sqrt(I1**2 + Q1**2)
		mag1dB = 20*np.log10(mag1) #on dB scale
		
		#Stack mag1 on top of mag2 into one vector mag
		mags = np.hstack(zip(mag0, mag1)) 
		fft_mags = np.hstack(zip(mag0dB,mag1dB)) 
		
		line1.set_ydata(mags)
		line2.set_ydata(fft_mags)

		fig.canvas.draw()
		count += 1
	return

#Build a connection to the Board with its IP Address; Make sure the board is turned on
fpga = casperfpga.KatcpFpga('192.168.40.67')

#Upload the compiled fpg file  
fpga.upload_to_ram_and_program('/home/andysey/mlib_devel/test1_stablev6_spec/bit_files/test1_stablev6_spec_2018_Oct_16_1754.fpg')

#Initialize the registers
fpga.write_int('dac_reset',1)
fpga.write_int('dac_reset',0)
fpga.write_int('start_dac',0)
fpga.write_int('start_dac',1)

#Not sure what this does 
fpga.write_int(regs[np.where(regs == 'fft_shift_reg')[0][0]][1], 2**9 -1)

#Stablize the plots by ignoring divison by 0
plt.ion()

#Plot the fft of what is in the register
plotFFT()

