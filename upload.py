import casperfpga
fpga = casperfpga.KatcpFpga('192.168.40.67')
fpga.upload_to_ram_and_program('/path/to/file.fpg')
fpga.listdev()
