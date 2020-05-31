import docx2txt
import re
import os
import shutil

def read_document(inputFile):
    doc = docx2txt.process(inputFile)
    
    return doc

def remove_unused_symbols(inputWord):
    symbolsArr = re.compile('[!@#$%^&*(),.?":{}|<>]+')

    if (symbolsArr.search(inputWord) == None):
        return inputWord
    else:
        return ""

def read_all_document(dir):
    return os.listdir(dir)

def rm_dir(dir):
    shutil.rmtree(dir)