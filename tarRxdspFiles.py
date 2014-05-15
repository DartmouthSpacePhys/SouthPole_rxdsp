#!/usr/bin/env python
import sys, os, subprocess,glob,datetime

workDir = '/daq/processed/daily_graydata_files/'

#Get the current date
now = datetime.datetime.now()

#Loop over the past two days
for i in range(5):
	
	searchDate = now - datetime.timedelta(days=i)

	timeString = searchDate.strftime("%Y%m%d")
	#Identify all days that match
	searchString = workDir + 'qtest-{0}*master*.fft'.format(timeString)
	print "searching for {0}".format(searchString)
	#print "searching for {0}".format(searchString)
	allFiles = glob.glob(searchString)

	#If we have no files, go to the next day
	if len(allFiles) == 0:
		print "Now files found"
		continue
	print "files found!"
	#Make a directory
	dirName = workDir + 'qtest-{0}_GraydataFiles'.format(timeString)
	print "making {0} workDir + 'qtest-{0}_GraydataFiles".format(timeString)
	subprocess.call(['mkdir {0}'.format(dirName)],shell=True,cwd=workDir)

	#Move all the files in that directory
	for infile in allFiles:
		subprocess.call(['mv {0} {1}'.format(infile, dirName)],shell=True,cwd=workDir)
	
	#Tar the directory
	tarName = workDir + "RxDSP_" + timeString + '.tar.gz'
	subprocess.call(['/bin/tar -zcvf {0} {1}'.format(tarName,dirName)],shell=True,cwd=workDir)



