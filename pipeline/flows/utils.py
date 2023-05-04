import os

def createIfNotExist(path: str):  
    if not os.path.exists(path):
        os.makedirs(path)