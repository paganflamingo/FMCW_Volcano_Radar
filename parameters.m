%% Find chirp period

c = 3e8;
t50k = 2*50e3 /c;
T_chirp = 2*t50k;

%% Find chirp rate

bw_sig = 1e6
bw_chirp = bw_sig *16;
chirp_rate = bw_chirp / T_chirp;

% Find bins
clock = 50e6;
bw_fpga = 0.5*clock;

bins = 2^14;
f_bin = bw_fpga / bins;

d_bin = c*f_bin/(2*chirp_rate);
display('distance per bin is:'); display(d_bin);

%% Compare to ensure everything works

if (bw_sig > bw_fpga)
    display('chirp bandwidth too high');
end

f_min = 2*5e3 *chirp_rate/c;
f_max = 2*7.5e4 * chirp_rate/c;

if (f_max<bw_fpga)
    display(1)
end
