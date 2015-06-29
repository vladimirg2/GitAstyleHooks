# GitAstyleHooks
A few hooks to make Artistic Style part of git. Prevent un-styled files from beeing commited, etc. 

To install the pre-commit hook, execute the following command in the root directory of the repo:

ln -s ../../pre-commit.py .git/hooks/pre-commit

To install the update (server-side) hook:

ln -s ../../update.py .git/hooks/update





For both hooks, edit the path to to the 'defaultOptions.txt' file, to be valid on your machine. 

 

