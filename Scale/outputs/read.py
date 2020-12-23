import json
import sys
with open(sys.argv[1] + "/energy_results.json", mode = 'r') as file1:
	fileee = json.load(file1)
for row in fileee:
	print(row)
	print("\n")
