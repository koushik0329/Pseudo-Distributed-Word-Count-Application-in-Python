# Implement a Python script to split the text file into multiple (at least two) small text files. 
# Each small text file should have exactly one paragraph. 
# Name each small text file with a unique name.

import multiprocessing
import uuid

large_file_name = "large.txt"
paragraphs = open(large_file_name).read()
paragraphs = paragraphs.split("\n\n")


# smalls folder must exist before executing this script.
def paragraph_into_file(paragraph, destination="smalls/"):
    filename = destination + uuid.uuid4().hex
    print(paragraph, file=open(filename, "w"))


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=len(paragraphs))
    pool.map(paragraph_into_file, paragraphs)
    pool.close()
    pool.join()
