import argparse
import os

from mega import Mega
import requests

parser = argparse.ArgumentParser()
parser.add_argument('identifier',
                    type=str,
                    help="the identifier based on the action (either a file path or a paste ID)")

parser.add_argument('-as', '--as-name',
                    type=str,
                    help="file name to save as")

parser.add_argument('-u', '--upload',
                    help="upload a file to mega",
                    action="store_true")

parser.add_argument('-p', '--paste',
                    help="upload text from a pstebin paste to mega",
                    action='store_true')
args = parser.parse_args()

mega = Mega()
global MEGA
MEGA = mega.login(email="g.aditya2048@gmail.com", password="wr3ckSh1p")

def mega_upload_file(file_path, dest_filename=None):
    if dest_filename is None:
        dest_filename = os.path.split(file_path)[-1]
    try:
        MEGA.upload(filename=file_path, dest_filename=dest_filename)
    except FileNotFoundError:
        print(f"meg: [upload] invalid file path: '{file_path}'")

def mega_upload_paste(paste_id, filename):
    if filename is None:
        raise ValueError
    paste_text = requests.get(f"http://pastebin.com/raw/{paste_id}").text
    with open(filename, 'w', encoding='utf-8') as temp_file:
        temp_file.write(paste_text)
    MEGA.upload(filename=filename, dest_filename=filename)
    os.remove(filename)

if args.upload:
    mega_upload_file(args.identifier, args.as_name)

if args.paste:
    try:
        mega_upload_paste(args.identifier, args.as_name)
    except ValueError:
        print("meg: [paste] filename cannot be None (use -as to add a file name)")
