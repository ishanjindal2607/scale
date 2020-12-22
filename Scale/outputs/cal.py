import sys
import csv
import os
print(sys.argv[1])
energy = {}
with open("data.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		energy[row['name']] = int(row['energy'])
print(energy)
cycle_counts = {}
total = 0
with open(sys.argv[1] + "/mobilenet_detail.csv", mode = 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		cycle_counts[row['Layer']] = energy['dram_ifmap'] * int(row["\tDRAM_IFMAP_bytes"]) + energy['dram_ofmap'] * int(row["\tDRAM_OFMAP_bytes"]) + energy['dram_filter'] * int(row["\tDRAM_Filter_bytes"]) + energy['sram_read'] * int(row["\tSRAM_read_bytes"]) + energy['sram_write'] * int(row["\tSRAM_write_bytes"])
with open(sys.argv[1] + "/mobilenet_cycles.csv", mode = 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		cycle_counts[row['Layer']] = cycle_counts[row['Layer']]  + energy['MAC'] * int(row["MACs"])
		total = total + cycle_counts[row['Layer']]
print(cycle_counts)
print(total)
