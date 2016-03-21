# Serial sum of factorials

import math

INPUT_FILE_COUNT = 10
INPUT_FILE_DIR = 'data/'
OUTPUT_FILE = 'results/serial.txt'

total = 0
for i in xrange(0, INPUT_FILE_COUNT):
  file_name = '%s%s.txt' % (INPUT_FILE_DIR, i)
  print 'Reading and processing file %s' % file_name
  with open(file_name, 'r') as infile:
    for l in infile:
      total += math.factorial(int(l))

with open(OUTPUT_FILE, 'w') as outfile:
  outfile.write('%s\n' % total)

print 'Done'
