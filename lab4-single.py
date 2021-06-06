# import lab4
from lab4 import index

import numpy as np
import pandas as pd
import os
import os.path
import sys

# # Single file // str(i)
# singleWord = {}
# fileNumber = sys.argv[1]

# def single(fileNumber):
#     # print("-----------------------------------------------------------------------")
#     filenameS = "Spam/" + str(fileNumber) + "_spam.txt"
#     if os.path.isfile(filenameS):
#         # print ("File " + fileNumber + "_spam exists")    
#         fp = open(filenameS, errors="ignore")
#         data = fp.read()
#         single_words = data.split()
#         fp.close()

#         unwanted_chars = ".,-_"
            
#         for single_word in single_words:
#             word = single_word.strip(unwanted_chars)
#             if word not in singleWord:
#                 singleWord[word] = 0 
#             singleWord[word] += 1 
#             # print(single_word, singleWord[word])



#     else:
#         # print ("File doesn't exist", fileNumber)

    
    
#     # print("-----------------------------------------------------------------------")

# single(fileNumber)
