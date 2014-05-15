SouthPole_rxdsp
===============

Python scripts and QuickUSB drivers (qusb_acq, qusb_fft, etc.)

(04/28/2014)
The contents of this repository are:

1. pippin_ggse.tar.gz
   --this is the /usr/ggse/ directory on pippin, including rxdsp_acq_2.0.py
2. qusb_pippin.tar.gz
   --this is the /usr/src/qusb_acq/ directory on Pippin, which includes (most importantly)
      the program qusb_acq as well as source code
3. QuickUsbLinux_v2.15.0-Prerelease_110721.tar.gz
   --This is the version of the QuickUSB drivers obtained by Matt (and Micah) for which they
      had to sign a nondisclosure agreement some time ago. They are known to work with the
      programs above, so they are here despite being possibly outdated.
4. QuickUsbLibrary_v2.15.2_Linux.tar.gz
   --These are the most recent drivers that I (Spencer Hatch) obtained from Bitwise Systems
      in April 2014.
5. tarRxdspFiles.py: puts all of the graydata files into a directory and compresses that
directory. It runs once per day on the remote computer.
6. scp_tar_files.py: copies the compressed files to aristotle. Because the satellite windows
vary from day to day, the script executes once per hour on the remote computer.
7. 

##Instructions for Data Management
1. To manage the data, log onto aristotle and navigate to
/media/Xi_backup/sp/rxdsp
2. New data shows up as a compressed directory with the following filename
YYYYMMDD.tar.gz. Decompress the directory and find the graydata files (files that end with .fft).
3. To delete files from the remote computer, open DeleteFiles.txt
4. To add a file to be deleted, use the following form
YYYY-MM-DD hh1,hh2,hh3,hh4...

where hh1, hh2, ... are the two-digit integer hours you want to delete. Make sure the list of hours
is comma-delimited with no spaces. For example, if you wanted to delete from 0-3:59 on 4 May 2014, add the 
following line
2014-05-04 00,01,02,03




