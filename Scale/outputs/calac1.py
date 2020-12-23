import sys
import csv
import os
import json
print(sys.argv[1])
energy = {}
with open("data.csv") as file:
	reader = csv.DictReader(file)
	for row in reader:
		energy[row['name']] = int(row['energy'])
print(energy)
list1 = []
total = 0
with open(sys.argv[1] + "/mobilenet_detail.csv", mode = 'r') as file1, open(sys.argv[1] + "/mobilenet_cycles.csv", mode = 'r') as file2 :
	reader1 = csv.DictReader(file1)
	reader2 = csv.DictReader(file2)
	total = 0
	for row, row1 in zip(reader1,reader2):
		print(row1.keys())
		layer = {}
		layer_total = 0
		layer["name"] = row1['Layer']
		layer["dram_ifmap"] = energy['dram_ifmap'] * int(row["\tDRAM_IFMAP_bytes"])
		layer["dram_ofmap"] = energy['dram_ofmap'] * int(row["\tDRAM_OFMAP_bytes"]) 
		layer["dram_filter"] = energy['dram_filter'] * int(row["\tDRAM_Filter_bytes"])
		layer["sram_read"] =  energy['sram_read'] * int(row["\tSRAM_read_bytes"])
		layer["sram_write"] = energy['sram_write'] * int(row["\tSRAM_write_bytes"])
		layer["MACs"] =       energy['MAC'] * int(row1[" MACs"])
		layer_total = energy['dram_ifmap'] * int(row["\tDRAM_IFMAP_bytes"]) + energy['dram_ofmap'] * int(row["\tDRAM_OFMAP_bytes"]) + energy['dram_filter'] * int(row["\tDRAM_Filter_bytes"]) + energy['sram_read'] * int(row["\tSRAM_read_bytes"]) + energy['sram_write'] * int(row["\tSRAM_write_bytes"]) + energy['MAC'] * int(row1[" MACs"])
		layer["total"] = layer_total
		total = total  + layer_total
		list1.append(layer)
final = {}
final["final_total"] = total
list1.append(final)
with open(sys.argv[1] +  "/energy_results.json", 'w') as f:
	json.dump(list1, f)
print(total)
