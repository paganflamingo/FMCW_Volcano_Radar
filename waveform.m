%% Waveform Generator - Andrew Xi, Matthew Lee - ASU

%% Initialize

clear all;
clc;

%% Define Parameters

% Here we define relevant parameters. Not all will be used in the design.

clk_dac = 50e6;                         % The ROACH will be clocked at 50 MHz
bw_dac = clk_dac / 2;
bw_signal = 1e6;                        % The pre-multiplication signal will have a bandwidth of 1 MHz
bw_chirp = 16 * bw_signal;

%% Find chirp period

d = 50e3;                               % The maximum expected object distance will be 50 km
c = 3e8;                                % Speed of light
dt = 2*d / c;
T = 2*dt;                               % The theoretical period will be double the time delay between signal transmission and reception

%% Find chirp rate

a = bw_chirp / T;

%% Find FFT parameters

bins = 2 ^ 14;
f_bin = bw_dac / bins;                  % Frequency range of each bin
d_bin = c*f_bin / (2*a);                % Distance represented by each bin

%% Signal frequency

t_clk = 1/clk_dac;                      % Clock period
t = 0:t_clk/2:T;                        % Create vector from 0 s to chirp period
s = 0:(1e6)/(clk_dac*T)/2:1e6;          % Create vector from 0 MHz to 1 MHz with same length as t
s = 10e6+s;                             % Shift frequencies to 10 MHz to 11 MHz

%% Define chirp

w = 2*pi*s;                             % Frequency of chirp in rad/s
chirp = sin(w.*t);                      % Chirp signal as amplitude vs time

% Uncomment the below to view the plots of a single chirp

% subplot(2,1,1);
% plot(t,chirp,'-');
% xlim([0,T]);
% title('Signal');
% ylabel('Amplitude');
% xlabel('Time (s)');
%
% subplot(2,1,2);
% plot(t,s,'r-');
% xlim([0,T]);
% title('Frequency');
% ylabel('Frequency (Hz)');
% xlabel('Time (s)');

%% Load chirp

% Uncomment and run this section only if chirpwaveform.dat is already
% downloaded and present in current path

% wave = load('chirpwaveform.dat');
% S0 = wave(:,1);
% S1 = wave(:,2);
% S0 = transpose(S0);
% S1 = transpose(S1);
% clear wave;
% 
% t0 = t(1:2:65536);
% t1 = t(2:2:65536);
% plot(t0,S0,'o',t1,S1,'o',t,chirp,'-');
% xlim([0,1e-6]);

%% Split into even and odd vectors

S0 = chirp(1:2:65536);
S1 = chirp(2:2:65536);

% Uncomment the below to check if vector lengths match

% if (size(S0) == size(S1))
%     display('vector lengths match');
% else
%     display('vector lengths do not match');
% end

%% Combine signal into one file

% Uncomment the below to save file as .dat

% s0 = transpose(S0);
% s1 = transpose(S1);
% signal = [s0(:) s1(:)];                 % Concatenate signal vectors into matrix
% 
% save('path\to\MATLAB\chirpwaveform.dat','signal','-ascii');

%% Calculate period of chirp

s0_size = size(S0);
n_datapoints = s0_size(2);
T_chirp = 2 * n_datapoints / clk_dac;

T_return = T * 1.25;
