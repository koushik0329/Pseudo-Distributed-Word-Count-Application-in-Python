# Implement a master process that coordinates the word count aggregation. The master process should:
#  - Launch the worker process (described above) to process small data.
#  - Collect word count results from all worker nodes. (Note: You need to wait until all the processes are complete before collecting results from worker nodes)
#  - Aggregate the word counts into a global word count dictionary. (Note: Processes are isolated from each other. So, you need to find a way to support the inter-process communication.)

import multiprocessing
import os

def getFileNames(folder_name="smalls"):
  if not os.path.exists(folder_name) or not os.path.isdir(folder_name):
    return []

  file_names = os.listdir(folder_name)
  return file_names

def getFreqCount(filepath, countDict):
  paragraph = open(filepath).read()
  tokens = paragraph.split()
  for token in tokens:
    token = token.lower().strip('.,!?()[]{}":;')

    if not token: continue

    countDict[token] = countDict.get(token, 0) + 1


folderpath = "smalls/"
filenames = getFileNames()
filepaths = [folderpath + filename for filename in filenames]

if __name__ == "__main__":
  with multiprocessing.Manager() as manager:

    freqResult = manager.dict()
    pool = multiprocessing.Pool(processes=len(filenames))
    args = [(filepath, freqResult) for filepath in filepaths]
    pool.starmap(getFreqCount, args)
    pool.close()
    pool.join()

    for key in sorted(freqResult.keys(), key=lambda x: -freqResult[x]):
      print(f"{key} : {freqResult[key]}")

