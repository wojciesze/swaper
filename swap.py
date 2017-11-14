#!/usr/bin/env python3


import sys, os, re


rev_mode = 0
if len(sys.argv) > 1 and sys.argv[1] == '-r':
	rev_mode = 1
	sys.argv.pop(0)


if len(sys.argv) < 3:
	print('Usage: {} [-r] <file> <number>'.format(sys.argv[0]))
	sys.exit(0)


file = sys.argv[1]
num = sys.argv[2]

if not os.path.isfile(file):
	print('No such file: {}'.format(file))
	sys.exit(1)


if not re.search('^\d+$', num):
	print('Invalid num: {}'.format(num))
	sys.exit(1)


num = int(num)
file_size = os.stat(file).st_size
out_file = '{}.out'.format(file)
cut = file_size - num
if rev_mode:
	cut = num
else:
	cut = file_size - num
	

if num > file_size or num < 2:
	print('num should be greater than 2 and less than file size!')
	sys.exit(1)
	

if not os.access(file, os.R_OK):
	print('File cannot be read!')
	sys.exit(1)


if not os.access(file, os.W_OK):
	print('permission deny for output file: {}'.format(out_file))
	sys.exit(1)

with open(file, 'rb') as f:
	buf = f.read()

with open(out_file, 'wb') as f:
	f.write(buf[cut:])
	f.write(buf[0:cut])
