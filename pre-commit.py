#!/usr/bin/python

#Git pre-commit hook to reject any unstyled commit.

import os
import stat
import re

TEMPDIR='.scratchSpace8975309753075375349894'
    

def main():            
    os.system('mkdir -p %s' % TEMPDIR)
    os.system('git checkout-index --prefix=%s/ -af' % TEMPDIR)
    fileList = os.popen('git diff --cached --name-only --diff-filter=ACM', 'r') 

    abortCommit = False
    
    for fileName in fileList:
        fileName = str.strip(fileName)
        if fileName.endswith('.h') or fileName.endswith('.cpp') or fileName.endswith('.c'):
            astyleOutput = os.popen('astyle --options=defaultOptions.txt %s/' % TEMPDIR + fileName, 'r')
            for lines in astyleOutput:
                if lines.find('Formatted') >= 0:
                    print 'Invalid Style Format within file: %s\n' % fileName
                    abortCommit = True

    os.system('rm -rf %s' % TEMPDIR)                
    if abortCommit:
        print "Aborting commit!\nStyle and re-add files.\n"
        exit(1)
    exit(0)




if __name__ == "__main__":
    main()
