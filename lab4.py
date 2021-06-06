import numpy as np
import pandas as pd
import os
import os.path

# print(os.listdir("./Spam"))

import sys

wordfreq = {}   # word frequency dict for spam

wordfreq2 = {}  # word frequency dict for not spam

# counts
spam_count = 0
not_spam_count = 0
overlapping_count = 0

# SPAM
for i in range(5000):
    filenameS = "Spam/" + str(i) + "_spam.txt"
    if os.path.isfile(filenameS):
        print ("File exists")    
        fp = open(filenameS, errors="ignore")
        data = fp.read()
        spam_words = data.split()
        fp.close()

        unwanted_chars = ".,-_"
        
        for spam_word in spam_words:
            word = spam_word.strip(unwanted_chars)
            if word not in wordfreq:
                wordfreq[word] = 0 
            wordfreq[word] += 1        

    else:
        print ("File doesn't exist", i)

# NOT SPAM
for i in range(5000):
    filenameNS = "Not_spam/" + str(i) + "_ne_spam.txt"
    if os.path.isfile(filenameNS):
        print("File exists")
        fp2 = open(filenameNS, errors="ignore")
        data2 = fp2.read()
        ns_words = data2.split()
        fp2.close()

        unwanted_chars = ".,-_"

        for ns_word in ns_words:
            word2 = ns_word.strip(unwanted_chars)
            if word2 not in wordfreq2:
                wordfreq2[word2] = 0
            wordfreq2[word2] += 1

    else:
        print ("File doesn't exist", i)


print("\n\n\n\n\n\n\n SPAM \n\n\n\n\n\n\n")

for i in wordfreq:
    print(i, wordfreq[i])
    spam_count+=1

print("\n\n\n\n\n\n\n NOT SPAM \n\n\n\n\n\n\n")

for i in wordfreq2:
    print(i, wordfreq2[i])
    not_spam_count+=1


#---------------------------------------------#

fileWords = {}
fileWordsCount = 0

index = 10
isSpam = False

if isSpam:
    checkFilePath = "Spam/" + str(index) + "_spam.txt"
if not isSpam:
    checkFilePath = "Not_spam/" + str(index) + "_ne_spam.txt"

if os.path.isfile(checkFilePath):
    print("File exists")
    fp3 = open(checkFilePath, errors="ignore")
    data3 = fp3.read()
    check_words = data3.split()
    fp3.close()

    unwanted_chars = ".,-_"

    for check_word in check_words:
        word3 = check_word.strip(unwanted_chars)
        if word3 not in fileWords:
            fileWords[word3] = 0
        fileWords[word3] += 1

else:
    print ("File doesn't exist", index)


print("\n\n\n\n\n\n")

for i in fileWords:
    print(i, fileWords[i])
    fileWordsCount+=1


print("\n\nNumber of words in specified file is ", fileWordsCount)



#---------------------------------------------#


print("\n\nFile ", checkFilePath, " was checked")
spamProbability = {}


print("\n\nLEXEME SPAM/NOT SPAM OCCURENCE: \n\n")

print("-------------------------------------------------------------------")
print ("{:<15} {:<20} {:<20} {:<20}".format("LEXEME", "SPAM OCCURENCE", "NOT SPAM OCCURENCE", "SPAM PROBABILITY"))
spam_probability_sum = 0
for k in wordfreq:
    if k not in wordfreq2:
        wordfreq2[k] = 0
    if k in wordfreq2:
        p_l_spam = wordfreq[k] / spam_count
        p_l_ham = wordfreq2[k] / not_spam_count

        if p_l_spam == 0:
            spam_probability = 0.01
            
        elif p_l_ham == 0:
            spam_probability = 0.99

        else:
            spam_probability = (p_l_spam)/(p_l_spam + p_l_ham)                        

        if k in fileWords:
            print ("{:<15} {:<20} {:<20} {:<20}".format(k, wordfreq[k], wordfreq2[k], round(spam_probability, 4)))
            spam_probability_sum += spam_probability
                

        # print("Probability is: ", probability, "\n") 
        # overlapping_count+=1



spam_mean = spam_probability_sum / fileWordsCount

print("\n\nMean value of all probabilities for this file is: ", round(spam_mean, 4))



print("\n\n\n\nFound: ")
print(spam_count, " Spam lexemes")
print(not_spam_count, " Not Spam lexemes")
