#!/usr/bin/env python

import subprocess
RemoteDir = 'aurora@157.132.41.82:/daq/processed/data_files/'
workDir = '/media/Xi_backup/sp/rxdsp/'
subprocess.call(['scp {0} {1}'.format(workDir + 'DeleteFiles.txt',RemoteDir)],shell=True,cwd=workDir)
