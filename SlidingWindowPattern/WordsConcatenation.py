#!/usr/bin/python3
''' Words Concatenation
Given a string and a list of words, find all the starting indices of substrings in the given string 
that are a concatenation of all the given words exactly once without any overlapping of words. It is 
given that all words are of the same length.
Pattern: Sliding Window
Similarities: Maximum Sub SubArray of Size K
Algos: at least 1 loop and if statement
D.S: HashMap
Approach:
1. We will keep track of all the words in a HashMap and try to match them in the given 
string, ie, keep the frequency of every word in a HashMap.
2. Starting from every index in the string, try to match all the words. The index, will be calculated
based on the length of one of the words, since they all of the same length
`nextWordIndex = i + j * wordLength` formular shows where the next word is. we use wL since we 
are told its the same for every word.
-`j + 1 == wordsCount)` + 1 coz j starts from 0; 
3. In each iteration, keep track of all the words that we have already seen in another HashMap.
4. If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
5. Store the index if we have found all the words.
'''

def findWordConcatenation(string, words):
    '''Returns the starting indices of substrings in the given string 
    that are a concatenation of all the given words exactly 
    once without any overlapping of words.
    '''
    wordFreqMap = {}  #keeps track of the frequency of every word.
    wordsCount = len(words) #keeps track of the total count of all the words in the list
    wordLength = len(words[0]) #keeps track of the length of each word in the list
    resultIndices = []
    #keep track of the frequency of each word in the list
    for word in words:
        if word not in wordFreqMap:
            wordFreqMap[word] = 0
        wordFreqMap[word] += 1
    for i in range ((len(string) - wordsCount * wordLength) + 1):
        wordsSeen = {} #keeps track of the frequency of each word that has been seen
        for j in range(wordsCount):
            nextWordIndex = i + j * wordLength
            #get the next word from the string 
            word = string[nextWordIndex : wordLength]
            if word not in wordFreqMap: #break if we don't need this word
                break
            if word not in wordsSeen:
                wordsSeen[word] = 0
            wordsSeen[word] += 1 #add the word to the 'wordsSeen' map
            #no need to process further if the word has higher frequency than required
            if wordsSeen[word] > wordFreqMap[word]:
                break
            if (j + 1 == wordsCount): 
                resultIndices.append(i)
    return resultIndices

print(findWordConcatenation("catfoxcat", ["cat", "fox"]))
'''Time Complexity: O(N * M * Len), where N is the number of characters in the given string,
M is the total number of words, Len is the length of a word.
Space Complexity: O(M), since at most, we will be storing all the words in the two HashMaps.
Algorithm is not outputting the correct thing for all test cases; please correct it.'''

    
