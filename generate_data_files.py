# Generate some sample data files for mapreduce performance tests

import random

FILE_COUNT = 10
LINE_PER_FILE = 1000
MAX_RAND_INT = 10000
FILE_DIR = 'data/'

for i in xrange(0, FILE_COUNT):
  file_name = '%s%s.txt' % (FILE_DIR, i)
  print 'Writing file %s' % file_name
  with open(file_name, 'w') as outfile:
    for line_number in xrange(0, LINE_PER_FILE):
      outfile.write('%s\n' % random.randint(1, MAX_RAND_INT))

print 'Done'
