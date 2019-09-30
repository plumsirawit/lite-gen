# Command line application to generate testcases
import argparse
import os
import zipfile
import shutil

parser = argparse.ArgumentParser(description='Generate some testcases', formatter_class=argparse.RawDescriptionHelpFormatter, epilog='''
Detailed Usage:

Solution File: sol.py, the file which contains the solution
Generator File: gen.py, the file to generate input from parameters (read from stdin, output to stdout)
Configuration File: conf.cfg, the file containing the data which will be sent to gen.py
    For N testcases, there should be N lines in the file, each line will be read by gen.py as input
''')
args = parser.parse_args()

# Procedure:
# 1. Read and parse config into list of inputs
# 2. Write the input to a temporary file, then redirect it into gen.py and retrieve the output as x.in
# 3. Redirect the x.in from 2. to sol.py as input and retrieve the output as the x.sol
# 4. Repeat 2-3 for all x (all inputs)
# 5. Move the x.in and x.sol to the (new) result folder
# 6. Zip the result folder

# 1.
conf = open('conf.cfg','r')
inps = conf.read().strip().split('\n')
n = len(inps) # Number of test cases
for i in range(n):
	# x is i+1
	# 2.
	inpf = open('tmpf','w')
	inpf.write(inps[i])
	inpf.write('\n')
	inpf.close()
	os.system('python gen.py < tmpf > ' + str(i+1) + '.in')
	
	# 3.
	os.system('python sol.py < ' + str(i+1) + '.in > ' + str(i+1) + '.sol')

# 5.
os.mkdir('result')
for i in range(n):
	os.rename(str(i+1) + '.in', 'result/' + str(i+1) + '.in')
	os.rename(str(i+1) + '.sol', 'result/' + str(i+1) + '.sol')

# 6.
# ziph is zipfile handle
ziph = zipfile.ZipFile('result.zip', 'w', zipfile.ZIP_DEFLATED)
path = 'result/'
for root, dirs, files in os.walk(path):
	for file in files:
		ziph.write(os.path.join(root, file))
ziph.close()

# 7. (Optional) Clean up
shutil.rmtree('result')
os.remove('tmpf')