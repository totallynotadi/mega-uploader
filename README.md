
# meg

a command-line tool to securely upload local files and pastebin pastes to your mega account, without having to sign in anywhere
 
use it to securely upload any files from public computers to your mega cloud drive
* just pull the exe from github and use the appropriate commands to upload your files to your mega account, without having to sign in to your accounts on other computers

* also supports uploading text from pastebin - \
create a new paste from https://pastebin.com and copy the paste ID for your paste form the url bar and use meg to upload that as a text file 

## Setup
option to either use the python file if having access to a python installation locally, or directly using the pre-compiled executable

- using the python script - \
make sure to install all the dependancies by executing ```pip install -r requirements.txt``` after getting the requirements.txt file from the repo. \
use meg.py to run all the commands

- using the pre-compiled executable - \
just download the executable from the repo and use it from a terminal in the same directory

## Usage
- Uploading a local file - \
use \
```meg [-u | --upload] <filepath> ``` to upload a file to mega \
and,  
```meg [-u | --upload] <filepath> -as <destination_filename>``` \
to rename the file on the could drive \
example usage - \
```meg --upload test.txt -as test_upload.txt```

- uploading text from a pastebin paste as a file - \
use the  
```meg [-p | --paste] <paste_ID> -as <destination_filename>```
action where the paste ID is the string you get at the end of a url when looking a paste on pastebin.com as shown here\
![the paste ID is present at the end of the page url](url_sample.png) \
you'll also need to give a file name to save as on the cloud drive

## Planned Features
- providing a better interface to one's mega cloud drive utilizing more from what the api wrapper provides. \
could end up being a cli client for mega ;)
- looking at other cloud drive providers like dropbox and stuff :P


credits - @odwyersoftware for giving us a superb wrapper around the mega api!
