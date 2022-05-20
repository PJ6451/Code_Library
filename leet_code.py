import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # Write your code here
    n = len(arr[0])
    hourglass = []
    for i in range(n-2):
        for j in range(len(arr)-2):
            frsum = arr[j][i]+arr[j][i+1]+arr[j][i+2]
            srsum = arr[j+1][i+1]
            trsum = arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
            hgsum = frsum + srsum + trsum
            hourglass.append(hgsum)
    return max(hourglass)

def stop_words(text, k):
    # Write your code here
    words = text.split(' ')
    stpwords = []
    for item in words:
        if words.count(item) == k:
            if item not in stpwords:
                stpwords.append(item)
    return stpwords

def divisibleSumPairs(n, k, ar):
    # Write your code here
    cnt = 0
    for i in range(n):
        A = ar[i+1:]
        for j in A:
            sm = ar[i] + j
            if sm % k == 0:
                cnt += 1
    return cnt

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    birdid = []
    idcnt = []
    for bird in arr:
        if bird not in birdid:
            birdid.append(bird)
            idcnt.append(arr.count(bird))
    ind = idcnt.index(max(idcnt))
    return birdid[ind]

def romanToInt(s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        l = len(s)
        number = 0
        i = 0
        while i < l:
            num = dic[s[i]]
            if i < l-1:
                num2 = dic[s[i+1]]
                if num < num2:
                    number = number + num2 - num
                    i += 2
                else:
                    number = number + num
                    i += 1
            else:
                number = number + num
                i += 1
        
        return number

def isValid(s: str) -> bool:

    stack = []    
    
    d = {
        "(":")",
        "[":"]",
        "{":"}",
    }
    
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0

a = isValid("()}")