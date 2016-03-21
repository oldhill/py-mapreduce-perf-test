# Multi-threaded (subject to GIL) sum of factorials

import math
import threading

INPUT_FILE_COUNT = 10
INPUT_FILE_DIR = 'data/'

INTERMEDIATE_RESULTS_PATH = 'results/thread'
REDUCED_OUTPUT_FILE = 'results/multithread.txt'


def main():
  # Create and launch threads
  threads = []
  for i in xrange(0, INPUT_FILE_COUNT):
    threads.append(threading.Thread(target=read_and_process, args=(i,)))
  for t in threads:
    t.start()

  # Wait for all threads to complete execution
  for t in threads:
    t.join()
  print 'OK all threads are done'

  # Reduce results of each thread into final answer
  total = 0
  for i in xrange(0, INPUT_FILE_COUNT):
    file_name = '%s%s.txt' % (INTERMEDIATE_RESULTS_PATH, i)
    print 'Reading intermediate results file %s' % file_name
    with open(file_name, 'r') as infile:
      for l in infile:
        total += int(l)

  # Write reduced output file
  with open(REDUCED_OUTPUT_FILE, 'w') as outfile:
    outfile.write('%s\n' % total)
  print 'Done'


def read_and_process(n):
  file_name = '%s%s.txt' % (INPUT_FILE_DIR, n)
  print 'Reading and processing file %s' % file_name
  total = 0
  with open(file_name, 'r') as infile:
    for l in infile:
      total += math.factorial(int(l))
  with open('%s%s.txt' % (INTERMEDIATE_RESULTS_PATH, n), 'w') as outfile:
    outfile.write('%s\n' % total)
  print 'Thread %s just finished' % n


if __name__ == '__main__':
  main()
