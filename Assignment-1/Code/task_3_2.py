#Generate a final word count report containing the total count of each word across all small text files. Take a screenshot of the final output and paste it into the report. 

# import multiprocessing
import os

from utils import getSmallFilePaths
from utils import smallfiles_basepath


def updateFreqCount(filepath, countDict):
    paragraph = open(filepath).read()
    tokens = paragraph.split()
    for token in tokens:
        token = token.lower().strip('.,!?()[]{}":;')

        if not token: continue

        countDict[token] = countDict.get(token, 0) + 1


freqResult = dict()
filepaths = getSmallFilePaths(smallfiles_basepath)
[updateFreqCount(filepath, freqResult) for filepath in filepaths]

for key in sorted(freqResult.keys(), key=lambda x: -freqResult[x]):
    print(f"{key} : {freqResult[key]}")
