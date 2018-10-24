import matplotlib, time, struct
import numpy as np
import shutil
np.set_printoptions(threshold=np.nan)
matplotlib.use("TkAgg")
import matplotlib.lines
import matplotlib.pyplot as plt
import casperfpga 
#from myQdr import Qdr as myQdr
import types
import logging
import glob  
import os
import sys
#import valon_synth9
from scipy import signal
import scipy.fftpack
#import pygetdata as gd
#from sean_psd import amplitude_and_power_spectrum as sean_psd

regs = np.loadtxt("/media/mauskopf/~EVIDENCE~/spectrometer/firmware_registers.txt", dtype = "str")

def plotADC():
	# Plots the ADC timestream
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

def plotFFT():
	fft_len = 1024
	fig = plt.figure()
	plot1 = fig.add_subplot(111)
	line1, = plot1.plot(np.arange(0,1024,1), np.zeros(fft_len), '#FF4500', alpha = 0.8)
	line1.set_marker('.')
	#line2, = plot1.plot(np.arange(1,1024,2), np.zeros(fft_len/2), 'purple', alpha = 0.8)
	#line2.set_marker('.')
	plt.grid()
	plt.ylim(-10, 5000)
	plt.tight_layout()
	count = 0 
	stop = 1.0e6
	while(count < stop):
		fpga.write_int(regs[np.where(regs == 'fft_snap_ctrl_reg')[0][0]][1],0)
		fpga.write_int(regs[np.where(regs == 'fft_snap_ctrl_reg')[0][0]][1],1)
		fft_snap = (np.fromstring(fpga.read(regs[np.where(regs == 'fft_snap_bram_reg')[0][0]][1],(2**9)*8),dtype='>i2')).astype('float')
		I0 = fft_snap[0::4]
		Q0 = fft_snap[1::4]
		I1 = fft_snap[2::4]
		Q1 = fft_snap[3::4]
		mag0 = np.sqrt(I0**2 + Q0**2)
		#mag0 = 20*np.log10(mag0)
		mag1 = np.sqrt(I1**2 + Q1**2)
		mags = np.hstack(zip(mag0, mag1))
		#mag1 = 20*np.log10(mag1)
		fft_mags = np.hstack(zip(mag0,mag1))
		line1.set_ydata(fft_mags)
		#line2.set_ydata(mag1)
		fig.canvas.draw()
		count += 1
	return


fpga = casperfpga.KatcpFpga('192.168.40.70')
fpga.upload_to_ram_and_program('/media/mauskopf/~EVIDENCE~/spectrometer/trans_spec_v0.fpg')

fpga.write_int('dac_reset',1)
fpga.write_int('dac_reset',0)
fpga.write_int('start_dac',0)
fpga.write_int('start_dac',1)
fpga.write_int(regs[np.where(regs == 'fft_shift_reg')[0][0]][1], 2**9 -1)

plt.ion()

plotFFT()

