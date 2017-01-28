import time
import random


def maxSubarrayEnum(seq):
    subArray = []
    maxSubArray = []
    maxSum = 0
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            del subArray[:]
            sum = 0
            for k in range(i, (j + 1)):
                subArray.append(seq[k])
                sum += seq[k]
                if sum > maxSum:
                    maxSum = sum
                    del maxSubArray[:]
                    maxSubArray = list(subArray)
    return (maxSubArray, maxSum)

def bettMaxSubarrayEnum(seq):
    subArray = []
    maxSubArray = []
    maxSum = 0
    for i in range(len(seq)):
        del subArray[:]
        sum = 0
        for j in range(i, len(seq)):
            subArray.append(seq[j])
            sum += seq[j]
            if sum > maxSum:
                maxSum = sum
                del maxSubArray[:]
                maxSubArray = list(subArray)
    return (maxSubArray, maxSum)
'''
with open('MSS_TestProblems.txt') as f:
    for line in f:
        parts = line.split(' ')
        numbers = [int(P) for P in parts]
        tStart = time.time()
        maxSA = maxSubarrayEnum(numbers)
        tStop = time.time()
        print("Time:", tStop - tStart)
        print(maxSA)
    
with open('MSS_TestProblems.txt') as f:
    for line in f:
        parts = line.split(' ')
        numbers = [int(P) for P in parts]
        tStart = time.time()
        bettMSA = bettMaxSubarrayEnum(numbers)
        tStop = time.time()
        print("Time:", tStop - tStart)
        print(bettMSA)
'''

# randNumLst =[]
# userInput = int(input("How many inputs?"))
# for i in range(10):
#     del randNumLst[:]
#     for j in range(userInput):
#         randNum = random.randrange(-100, 100)
#         randNumLst.append(randNum)
#     '''
#     tStart = time.time()
#     maxSA = maxSubarrayEnum(randNumLst)
#     tStop = time.time()
#     print("Time Alg1:", tStop - tStart)
#     '''
#     #print(maxSA)
#     tStart = time.time()
#     bettMSA = bettMaxSubarrayEnum(randNumLst)
#     tStop = time.time()
#     print("Time Alg2:", tStop - tStart)
#     #print(bettMSA)
#
#
