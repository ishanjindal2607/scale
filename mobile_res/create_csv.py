import csv 
  
field_names = ['name', 'energy'] 
  
values = [ 
{'name' : 'MAC' , 'energy' : 1}, 
{'name' : 'dram_ifmap', 'energy' :  1}, 
{'name' : 'dram_ofmap', 'energy': 1}, 
{'name' : 'dram_filter', 'energy': 1}, 
{'name' : 'sram_read', 'energy': 1}, 
{'name' : 'sram_write', 'energy' : 1}
] 
  
with open('data.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    writer.writeheader() 
    writer.writerows(values)
