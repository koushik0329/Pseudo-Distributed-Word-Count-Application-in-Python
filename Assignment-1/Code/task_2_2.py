# Modify the program to be able to run on multiple processes, where each process can be created using the Python “multiprocessing” module. 
# Each process should run more than one thread in parallel. 
# Each process also needs to aggregate the dictionary returned by all its threads.

import multiprocessing
import threading
from utils import getSmallFilePaths


def getFreqCount(filepath, freqRef, lock):
    if freqRef is not None:
        result = freqRef
    else:
        result = dict()

    def addToken(token):
        getCleanToken = lambda token: token.lower().strip('.,!?()[]{}":;')

        ctoken = getCleanToken(token)
        if not ctoken:
            return

        lock.acquire()
        # print(f"ACQUIRED : {threading.current_thread().name}")
        result[ctoken] = result.get(ctoken, 0) + 1
        # print(f"RELEASED : {threading.current_thread().name}")
        lock.release()

    paragraph = open(filepath).read()
    tokens = paragraph.split()
    [addToken(token) for token in tokens]
    print(result)
    return result


smallfilepaths = getSmallFilePaths()

batch_size = 2
batch = list()
batches = list()
for filepath in smallfilepaths:
    batch.append(filepath)

    if len(batch) < batch_size:
        continue
    batches.append(batch.copy())
    batch.clear()


def processFor(batch):
    lock = threading.Lock()
    processDict = dict()
    threads = []
    for index, filepath in enumerate(batch):
        thread = threading.Thread(
            target=getFreqCount,
            args=(filepath, processDict, lock),
            name=f"thread {index} {filepath[::-1][:4]}",
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(processDict, end="\n ----- \n")
    return processDict


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=len(batches))
    pool.map(processFor, batches)
