import random

"""Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb"."""

def exercises(string, k):
    maxstring = ""
    for i in range(len(string)-k):
        char_used = []
        inside_string = ""

        for j in range(i, len(string)):
            if (len(char_used)<k) or (len(char_used) ==k and (string[j] in char_used)):
                inside_string += string[j]
                if string[j] not in char_used:
                    char_used.append(string[j])
            else:
                break
        
        if len(inside_string)>len(maxstring):
            maxstring= inside_string
        
    return maxstring

#print(exercises("abcbaada", 3))

"""The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2."""

def MC(points):
    total = 0
    for i in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        r = (x*x+y*y)**(1/2)
        if r<=1:
            total+=1

    areacircle = total*4 /points #square we are placing the circle is 4 square units in area
    return areacircle

#print(MC(1000000))

"""The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them."""

def get_edit_distance(string1, string2):
    #with similar lenghts:
    changes = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            changes +=1

    return changes 

"""Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out: 2
1.5
2
3.5
2
2
2"""

def get_string_of_medians(stream):
    start_list = [stream[0], stream[1]]
    def get_median(current_stream):
        current_stream.sort()
        count = 1
        maxA=[1,current_stream[0]]
        maxB=[1,current_stream[1]]
        for i in range(len(current_stream)-1):
            if current_stream[i] == current_stream[i+1]:
                count += 1
            else:
                if maxA[0] < count and maxA[0]<maxB[0]:
                    maxA = [count,current_stream[i]]
                    count = 1
                elif maxB[0]<count:
                    
                    maxB = [count,current_stream[i]]
                    count = 1
                else:
                    count = 1
        if maxA[0]==maxB[0]:
            return (maxA[1]+maxB[1])/2
        if maxA[0]>maxB[0]:
            return maxA[1]
        else:
            return maxB[1]

    for i in range(2,len(stream)):
        print(get_median(start_list))
        start_list.append(stream[i])

get_string_of_medians( [2, 1, 5, 7, 2, 0, 5])

