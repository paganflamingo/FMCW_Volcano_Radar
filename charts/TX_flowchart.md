```mermaid
graph LR

	Oscope(Oscilloscope)
	PowerSplitter(2 Way Power Splitter)
	SigGen(Signal Generator)
	DAC(DAC)
	ADC(ADC)
	FPGA(Memory)


	subgraph ROACH
		subgraph DAC/ADC
			DAC
			ADC
		end
		subgraph FPGA
			FPGA
		end
	end
	
	SigGen == Clock ==> PowerSplitter
	PowerSplitter == Clock ==> DAC
	PowerSplitter == Clock ==> ADC
	DAC == Clock ==> FPGA
	FPGA == Signal ==> DAC
	DAC == Signal ==> Oscope
```
