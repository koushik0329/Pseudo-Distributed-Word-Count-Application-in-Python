# Implement a word count program using Python's `threading` module. Each thread should perform the following steps:
#  - Read a small text file.
#  - Tokenize the text into words.
#  - Count the occurrences of each word.
#  - Return a dictionary of word counts for that small text file
import threading

from utils import getSmallFilePaths

def getFreqCount(paragraph, thread_name=None):
    countDict = dict()
    tokens = paragraph.split()

    for token in tokens:
        token = token.lower().strip('.,!?()[]{}":;')

        if not token:
            continue

        countDict[token] = countDict.get(token, 0) + 1

    if thread_name is None:
        return countDict

    thread_result = {"thread_name": thread_name, "thread_result": countDict}
    print(thread_result)


filepaths = getSmallFilePaths()
threads = []
for index, filepath in enumerate(filepaths, start=1):
    para = open(filepath).read()

    thread_name = f"thread {index}"
    thread = threading.Thread(target=getFreqCount, args=[para, thread_name])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("threads execution completed.")
