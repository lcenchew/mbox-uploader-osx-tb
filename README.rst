Thunderbird|GMail mbox uploader for OS X
========================================

Imports Thunderbird mbox file e-mails to GMail


Setup
-----
1. Extract files from archive
2. Change to folder containing extracted archive
3. Run the following command from the terminal prompt:

python setup.py install --user

4. Run the following command from the terminal prompt to process a mail migration:

./mbox-uploader-osx-tb.py


Usage
-----

There are two command line switches:

- --reauth : forces reauthentication<br />
- --redoall: forces reimporting of all messages in MBOX

