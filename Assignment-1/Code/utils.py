import os

smallfiles_basepath = "smalls/"

def getSmallFileNames(smallfiles_basepath=smallfiles_basepath):
    if not os.path.exists(smallfiles_basepath):
        return []
    if not os.path.isdir(smallfiles_basepath):
        return []
    return os.listdir(smallfiles_basepath)


def getSmallFilePaths(smallfiles_basepath=smallfiles_basepath):
    smallfile_names = getSmallFileNames()
    smallfilepaths = [smallfiles_basepath + filename for filename in smallfile_names]
    return smallfilepaths
