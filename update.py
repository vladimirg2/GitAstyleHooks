#!/usr/bin/python

#Git update hook to reject any push with unstyled files.

##############################################################
# THIS IS A WORK IN PROGRESS! It's 1 AM, I NEED SLEEP!
##############################################################

import os
import stat
import re
import sys
import subprocess
import shlex

TEMPDIR='.updateScratchSpace8975309753075375349894'

#The update hook recieves #refname sha1-old sha1-new as arguments:   

def main():  
    print 'Number of arguments:', len(sys.argv), 'arguments.' 
    print 'Argument List:', str(sys.argv)

    branch = sys.argv[1]
    old_commit = sys.argv[2]
    new_commit = sys.argv[3]

    print "Moving '%s' from %s to %s" % (branch, old_commit, new_commit)


    os.system('mkdir -p %s' % TEMPDIR)
    #Building command line in parts because the parses seems to freak out if it is one line.
    commandString = "git archive "
    commandString += new_commit + " | " 
    commandString += "tar -x -C  " + TEMPDIR
    print "commandString: " + commandString 
    
    os.system(commandString)
    os.chdir(TEMPDIR)
    
    commandString = "ls -l "#W.I.P: find every .c and .cpp file | to astyle check astyle's output. 
    print "commandString = " + commandString
    proc1 = subprocess.Popen(shlex.split(commandString), stdout=subprocess.PIPE)
    fileList,err=proc1.communicate()
    print (fileList)
    print (err)

    os.system('rm -rf %s' % TEMPDIR) 

    exit(1)#W.I.P.


if __name__ == "__main__":
    main()

