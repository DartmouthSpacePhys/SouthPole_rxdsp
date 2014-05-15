#!/usr/bin/env python

import sys, subprocess, glob

DataDir = '/daq/processed/daily_graydata_files/'
TransferredDir = '/daq/processed/daily_graydata_files/Sent/'
RemoteDir = 'canopus@aristotle.dartmouth.edu:/media/Xi_backup/sp/rxdsp/'

#Iterate over a list of files in DataDir that end in ps
for PsFile in glob.glob(DataDir + '*.gz'):
	#try to scp the file
	ret = subprocess.check_call(['scp {0} {1}'.format(PsFile,RemoteDir)],cwd=DataDir,shell=True)

	#If we're successful, move the file to the transferred directory
	if (ret == 0):
		subprocess.call(['mv {0} {1}'.format(PsFile,TransferredDir)],shell=True,cwd=DataDir)
	else:
		continue
		
