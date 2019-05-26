from bs4 import BeautifulSoup
import re
import cld2
import sys

def split_func2(a):
    split_a = re.split('; |, |\. |\n|! |:',a)
    return split_a

def clean_wolof_cld(file_dir):
    with open(file_dir) as file:
        data = file.read()
    soup = BeautifulSoup(data, features="lxml")
    text = soup.get_text()
    alltext = text.split('\n')
    lines = [t for t in alltext if t is not '']

    wolof_utterance = []
    for item in lines:
        isReliable, textBytesFound, details = cld2.detect(item)
        if details[0][0] == 'Unknown':
            wolof_utterance.append(item.lstrip())

    c = []
    for item in wolof_utterance:
        c.append(split_func2(item))
    space = ['', ' ']
    utterance_all = [item for sublist in c for item in sublist if item not in space]
    utterance_rm_digits = [re.sub(r"\b\d+\b", " ", item) for item in utterance_all]
    utterance_rm_punc = [re.sub(r'[^\w\s]', '', item) for item in utterance_rm_digits]
    utterance_rm_nspace = [' '.join(item.split()) for item in utterance_rm_punc]
    utterance = [item for item in utterance_rm_nspace if len(item.split()) > 1]

    wolof_utterance2 = []
    for item in utterance:
        isReliable, textBytesFound, details = cld2.detect(item)
        if details[0][0] == 'Unknown':
            wolof_utterance2.append(item.lstrip())

    return wolof_utterance2

file_name = sys.argv[1]
if __name__ == '__main__':
    wiki000 = clean_wolof_cld(file_name)
    for item in wiki000:
        print(item)
      
