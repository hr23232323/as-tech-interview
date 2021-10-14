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

def word_count(input_file):
    # cache
    word_count = {}
    
    # Stream input
    for block in read(input_file):
        block = process_text(block)
        wc = Counter(block.split())
        for w, c in wc.items():
            if w in word_count:
                word_count[w] += c
            else:
                word_count[w] = c
                
    return word_count

# helper to process/clean text.
def process_text(word_block):
    word_block = word_block.lower()
    return re.sub('[^\w]', ' ', word_block)
    
    
#print(re.sub("[^\w]", ' ', "this is a string.[123]"))

    
#print(word_count(input_file))
#print(Counter("this is a a A sentence".split()))

#print({'key1': 'value1'}.update({'key2': 'value2'}))

#print(get_word_count_from_block("this is a a A sentence"))

