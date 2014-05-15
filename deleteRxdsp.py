#!/usr/bin/env python
import sys, os, subprocess

deleteFile = open('/daq/processed/data_files/DeleteFiles.txt','r')
dataDir = '/daq/processed/data_files/'
keepHours = range(24)
remoteDir = 'aurora@157.132.24.200:/mnt/data/rxdsp'
for line in deleteFile:
	split = line.split()
	ymd = split[0].split('-')
	year = int(ymd[0])
	month = int(ymd[1])
	day = int(ymd[2])

	hours = [int(x) for x in split[1].split(',')]

	#For every hour
	for hour in hours:
		#build the filename
		filename = dataDir + 'qtest-%04i%02i%02i-%02i????????.data'%(year, month, day, hour)
		print "deleting {0}".format(filename)
		try:
			subprocess.call(['rm {0}'.format(filename)],shell=True,cwd=dataDir)
		except:
			print "Error: Cannot remove {0}\nFile not found".format(filename)
	[keepHours.remove(hour) for hour in hours]

	#Make all files you want to save immutable
	for hour in keepHours:
		
		#Create the filename
		filename = dataDir + 'qtest-%04i%02i%02i-%02i????????.data'%(year, month, day, hour)
		print "Saving {0}".format(filename)
	
		try:
			#Make any file you want to save immutable
			subprocess.call(['chattr +i {0}'.format(filename)],shell=True,cwd=dataDir)
		except:
			print	"Error: Can save {0}.\nFile not found".format(filename)

	#Copy all files you want to save to the remote directory
	for hour in keepHours:
		#Create the filename
		filename = dataDir + 'qtest-%04i%02i%02i-%02i*.data'%(year, month, day, hour)

		try:
			subprocess.call(['scp {0} {1}'.format(filename,remoteDir)],shell=True,cwd=dataDir)
		except:
			continue


