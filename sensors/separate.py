#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import csv

data = {}
keys = []

if len(sys.argv) < 4:
    print("Arguments must be: 'input file' 'output file' 'start date timestamp (unix)' '*show plot (true | false)' ")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
start_date = int(sys.argv[3])

if len(sys.argv) == 5:
  show_plot = sys.argv[4].lower() == "true"
else:
  show_plot = False

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

if show_plot:
  plot_keys = []
  plot_keys.append(keys[1])
  plot_keys.append(keys[2])
  plot_keys.append(keys[3])
  plot_keys.append(keys[5])
  plot_keys.append(keys[6])
  plot_keys.append(keys[8])
  plot_keys.append(keys[9])

  for key in plot_keys:
    plt.plot(data[keys[0]], data[key], label=key)

  plt.legend(loc="upper left")

  plt.grid(True)

data.pop("VL-RL Diff [K]")

with open(output_file, "w") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(data.keys())
   writer.writerows(zip(*data.values()))
   print("file {0} generated".format(output_file))

plt.show()