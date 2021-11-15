#!usr/bin/env Python3
'''
    A Python Script to play a mad libs game and append the output to the same file.

'''
import re

f = open("mad_libs.text", "r")
fo = open("mad_libs.text", "a")


for item in f.readlines():
    
    pattern = r"(?<=\()\w+,*\s*\w*\s*\w*(?=\))"
    part_of_body = re.findall(pattern, item)
    word_of_body = []
    replace_item = item
    for word in part_of_body:
        word_of_body.append(input(f"Enter a word for {word} "))
   
    
    for word, part in zip(word_of_body, part_of_body):
        pattern = r"\(" + part + "\)"
        replace_item = re.sub(pattern, word, replace_item)

    fo.write(replace_item)
f.close()
