#!/usr/bin/python

#Git update hook to reject any push with unstyled files.
#Written for Python 2.7.6


##############################################################
# THIS IS A WORK IN PROGRESS! It's 1 AM, I NEED SLEEP!
##############################################################

import os
import stat
import re
import sys
import subprocess
import shlex

TEMPDIR='.updateScratchSpace8909830803489f890293'

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
     
    
    os.system(commandString)
    os.chdir(TEMPDIR)

    proc1 = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    fullPath,err = proc1.communicate()

    commandString = "ls "#W.I.P: find . -name .c and .cpp file | to astyle check astyle's output. 
            
    
    proc1 = subprocess.Popen(shlex.split(commandString), stdout=subprocess.PIPE)
    rawOutput,err=proc1.communicate()
    fileList = rawOutput.splitlines()
    abortCommit = False
    
    for fileName in fileList:
        fileName = str.strip(fileName)
        if fileName.endswith('.h') or fileName.endswith('.cpp') or fileName.endswith('.c'):
            commandString = 'astyle --options=/home/vld/StylingOptionsFIleLocation/defaultOptions.txt %s/' % fullPath.rstrip('\n') 
            commandString += fileName
            
            proc2 = subprocess.Popen(shlex.split(commandString), stdout=subprocess.PIPE)
            astyleOutput,err = proc2.communicate();
            parsedOutput = astyleOutput.splitlines()
            for lines in parsedOutput:
                if lines.find('Formatted') >= 0:
                    print 'Invalid Style Format within file: %s\n' % fileName
                    abortCommit = True

    os.system('rm -rf %s' % TEMPDIR)                
    if abortCommit:
        print "Aborting commit!\nStyle then push again.\n"
        exit(1)
    exit(1)#Should be 0 once development and testing is done. 



if __name__ == "__main__":
    main()

