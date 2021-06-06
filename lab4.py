import numpy as np
import pandas as pd
import os
import os.path
import time

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
        print ("\n\n\nFile exists")    
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
    # print(i, wordfreq[i])
    spam_count+=1

print("\n\n\n\n\n\n\n NOT SPAM \n\n\n\n\n\n\n")

for i in wordfreq2:
    # print(i, wordfreq2[i])
    not_spam_count+=1


#---------------------- Initialization for checking a single file. Checking lexemes and their counts -----------------------#

def SpamCheck(a):
    fileWords = {}
    fileWordsCount = 0

    index = a
    isSpam = False


    if isSpam:
        checkFilePath = "Spam/" + str(index) + "_spam.txt"
    if not isSpam:
        checkFilePath = "Not_spam/" + str(index) + "_ne_spam.txt"

    if os.path.isfile(checkFilePath):
        # print("File exists")
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
        # print("\n\n\n\n\n\n")

        for i in fileWords:
            # print(i, fileWords[i])
            fileWordsCount+=1

        print("=================================================================\n\n\n")
        print("Checking file :", checkFilePath, "\n\n")
        print("Number of words in specified file is ", fileWordsCount)



        #-------------------------------- TASK 3 & 4. Check spamicity for words inside single file --------------------------------#


        # print("\n\nFile ", checkFilePath, " was checked")
        spamProbability = {}


        # print("\n\nLEXEME SPAM/NOT SPAM OCCURENCE: \n\n")

        # print("-------------------------------------------------------------------")
        # print ("{:<15} {:<20} {:<20} {:<20}".format("LEXEME", "SPAM OCCURENCE", "NOT SPAM OCCURENCE", "SPAM PROBABILITY"))

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
                    # print ("{:<15} {:<20} {:<20} {:<20}".format(k, wordfreq[k], wordfreq2[k], round(spam_probability, 4)))
                    spam_probability_sum += spam_probability
                    spamProbability[k] = round(spam_probability, 4)
                        

                # print("Probability is: ", probability, "\n") 
                # overlapping_count+=1



        spam_mean = spam_probability_sum / fileWordsCount   # mean value of spam probabilities for single file
        # print("\n\n#-- Mean value of all probabilities from this file is : ", round(spam_mean, 4), " --#")


        #-------------------------------- TASK 5. Find remoted lexemes. // Lexemes that are farthest away from the mean probability --------------------------------#

        remoted_lexemes = {}



        # print("\n\n#-- Remoted probabilities from mean probability for this file are:  --#")

        N = 8   # number of chosen remoted lexemes

        for i in range(N):
            for k in spamProbability:
                # print(spamProbability[k])
                min_probability = min(spamProbability, key=spamProbability.get)  #word
                max_probability = max(spamProbability, key=spamProbability.get)  #word
                # print("MIN PROBABILITY", spamProbability[min_probability])
                # print("MAX PROBABILITY", spamProbability[max_probability])

                min_probability_float = spamProbability[min_probability]
                max_probability_float = spamProbability[max_probability]

            if max_probability_float - spam_mean > spam_mean - min_probability_float:
                remoted_lexemes[max_probability] = max_probability_float
                spamProbability.pop(max_probability)

            if max_probability_float - spam_mean < spam_mean - min_probability_float:
                remoted_lexemes[min_probability] = min_probability_float
                spamProbability.pop(min_probability)


        # for i in range(N):
            
        remotedLoopCount = 0
        for i in remoted_lexemes:
            remotedLoopCount+=1
            # print("{:<10} {:<15} {:<15}".format(remotedLoopCount, i, remoted_lexemes[i]))



        #-------------------------------- TASK 6. Calculating file spamicity value --------------------------------#

        # TOP of equation

        remoted_lexemes_probs_multiplied = 1    # initial value for top part of the equation required for task 6

        for i in remoted_lexemes:
            remoted_lexemes_probs_multiplied *= remoted_lexemes[i]

        # print("\n\nMultiplication of remoted lexemes: ", round(remoted_lexemes_probs_multiplied, 4))


        # BOTTOM-RIGHT of equation

        remoted_lexemes_substractOne = 1

        for i in remoted_lexemes:
            remoted_lexemes_substractOne *= (1 - remoted_lexemes[i])

        # print("\n\nSubstraction part of equation: ", round(remoted_lexemes_substractOne, 4))


        # SPAMICITY PROBABILITY of a file. Equation for task 6

        spamicityProbabilityOfFile = remoted_lexemes_probs_multiplied / (remoted_lexemes_probs_multiplied + remoted_lexemes_substractOne)   # actual equation for task 6

        print("\n\nSPAMICITY PROBABILITY of selected file ",checkFilePath, " : ", round(spamicityProbabilityOfFile, 4))

        if spamicityProbabilityOfFile > 0.5:
            print("\nIt is likely that selected file is SPAM")
        else:
            print("\nIt is likely that selected file is NOT SPAM")
        
        print("\n\n\n")
        

        #print("\n\n\n=================================================================\n\n\n")

    # else:
    #     print ("File doesn't exist", index)


    


for i in range(5000):
    SpamCheck(i)
    # time.sleep(0.5)

print("\n\n\n\nFound: ")
print(spam_count, " Spam lexemes")
print(not_spam_count, " Not Spam lexemes")
