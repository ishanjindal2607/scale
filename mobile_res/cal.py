import sys
import csv
import os
print(sys.argv[1])
with open(sys.argv[1] + "/mobilenet_detail.csv", mode = 'r') as file:
	reader = csv.DictReader(file)
	print("conv layer    dram_ifmap   dram_ofmap   dram_filter    sram_read    sram_write")
	for row in reader:
		print("{}{}{}{}{}{}\n".format(row['Layer'],row["\tDRAM_IFMAP_bytes"],row["\tDRAM_OFMAP_bytes"],row["\tDRAM_Filter_bytes"],row["\tSRAM_read_bytes"],row["\tSRAM_write_bytes"]))
