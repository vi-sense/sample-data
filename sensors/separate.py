#!/usr/bin/env python3
import sys
import os
import matplotlib.pyplot as plt
import csv

data = {}
keys = []
directory = "sample_model/"

sys.argv.append("raw/sensordata_oct_2019.csv")
sys.argv.append("1569888000")
sys.argv.append("true")

if len(sys.argv) < 3:
    print("Arguments must be: 'input file' 'start date timestamp (unix)' '*show plot (true | false)' ")
    sys.exit()

input_file = sys.argv[1]
start_date = int(sys.argv[2])

if len(sys.argv) == 4:
  show_plot = sys.argv[3].lower() == "true"
else:
  show_plot = False

if not os.path.exists(directory):
    os.makedirs(directory)

with open(input_file) as f:
  last = start_date - 1200 # minus 20 min
  for i, line in enumerate(f):
    s = line.split(',')

    if len(s) == 10:
      if i == 0:
        for c in s:
          data[c.replace('\n','')] = []
        
        keys = list(data.keys())
      else:
        time = start_date + float(s[0])

        if time - last > 300:
          data[keys[0]].append(int(time))

          for i, key in enumerate(keys[1:]):
            data[key].append(float(s[i+1]))

          last = time

plot_keys = []
plot_keys.append(keys[1])
plot_keys.append(keys[2])
plot_keys.append(keys[3])
plot_keys.append(keys[5])
plot_keys.append(keys[6])
plot_keys.append(keys[7])
plot_keys.append(keys[8])
plot_keys.append(keys[9])

for key in plot_keys:
  plt.plot(data[keys[0]], data[key], label=key)
  with open(directory + key.split('[')[0].replace(' ', '_').lower() + ".csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['date', 'value'])
    writer.writerows(zip(*[data[keys[0]], data[key]]))
    print("file {0} generated".format(outfile.name))


plt.legend(loc="upper left")

plt.grid(True)

data.pop(keys[4])

if show_plot:
  plt.show()