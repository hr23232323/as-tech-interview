import requests
import io
from collections import Counter
import re

# Read the data from S3.
FILE_URL = 'https://s3.amazonaws.com/abnormalsecurity-public/phishing_interview.txt'
with requests.Session() as s:
    download = s.get(FILE_URL)
    decoded_file = download.content.decode('utf-8')

input_file = io.StringIO(decoded_file)    

def read(file):
    block_size = 512
    while True:
        chunk = file.read(block_size)
        if not chunk:
            break
        yield chunk

# Helpful SO article: https://stackoverflow.com/questions/22170095/get-words-from-large-file-using-low-memory-in-python
def buffered_read(file):
    buffer = ''
    block_size = 512
    while True:
        chunk = file.read(block_size)
        if not chunk:
            break
        words = re.split("\W+", buffer + chunk)
        buffer = words.pop()  # partial word at end of chunk or empty
        for word in words:
            yield word

    if buffer:
        yield buffer

def word_count(input_file):
    # cache
    word_count = {}
    
    # Stream input
    for block in buffered_read(input_file):
        block = process_text(block)
        wc = Counter(block.split())
        for w, c in wc.items():
            if w in word_count:
                word_count[w] += c
            else:
                word_count[w] = c
                
    return word_count

# helper to process/clean text.
# This can be expanded to clean up input data as required. 
def process_text(word_block):
    word_block = word_block.lower()
    return re.sub('[^\w]', ' ', word_block)

