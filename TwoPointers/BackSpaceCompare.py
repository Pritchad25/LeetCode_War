#!/usr/bin/python3
'''Problem Challenge 2:
Given two strings containing backspaces (identified by the character '#'), check if 
the two strings are equal.

Approach:
1. To compare the given strings, first, we need to apply the backspaces and an efficient way to 
do this would be from the end of both the strings.
2. We can have separate pointers, pointing to the last element of the given strings.
3. We can start comparing the characters pointed out by both the pointers to see if the 
strings are equal.
4. If, at any stage(ie for any iteration), the character pointed out by any of the pointers 
is a backspace('#') we will skip and apply the backspace until we have a valid character 
available for comparison.
'''
def BackspaceCompare(str1, str2):
    '''Compares two strings containing backspaces to determine
    if they are equal
    '''
    #use two pointer approach to compare the strings
    index1 = len(str1) - 1 #the index of last element of string str1
    index2 = len(str2) - 1# the index of last element of string str2
    while (index1 >= 0 or index2 >= 0): #loop will run for the total length of the string that is
        #bigger between the two
        i1 = getNextValidCharIndex(str1, index1)
        i2 = getNextValidCharIndex(str2, index2)
        if (i1 < 0 and i2 < 0):#reached the end of both the strings
            return True
        if (i1 < 0 or i2 < 0): #ie we've reached the end of one string yet not having reached the
            #end of the other string, THEN theyre not equal.
            return False
        if (str1[i1] != str2[i2]):#check if the characters we're currently standing in are equal,
            #if they are not, then the two strings are not equal
            return False
        #Otherwise, if we havent reached the end of both strings and we havent reached the end of
        #one string or the other and the two characters from both strings are EQUAL, THEN we move
        #on to compare the next VALID characters from both strings as shown below. Its -1 becoz
        #we started from the back of both strings, going 'frontward' hence we have to decrement
        #this index of a Valid character which we're currently character standing on both strings
        #which indexes are i1 and i2.
        index1 = i1 - 1 
        index2 = i2 - 1
    return True

def getNextValidCharIndex(str, index):
    '''Gets the next Valid Character Index.
    We either (1)encounter a backspace, take note of it or account for it
    and skip it or(2) we're applying the backspace to a VALID character and
    skipping this character or (3) we're standing in a valid character which 
    we should compare to the other character in the other string meaning
    '''
    backspaceCount = 0 #keeps track of count of backspaces.
    while (index >= 0):#runs for the total length of the length of the string 'str'
        if (str[index] == '#'): #found a backspace character
            backspaceCount += 1 #counting the backspace character by incrementing backspaceCount
            #and then skip this backspace character by incrementing `index` below 
        elif (backspaceCount > 0): #applying the backspace to this non-backspace character that we are currently
            #standing in. When we apply it, we're decrementing the number of backspaces we have
            #in our string and also skipping this VALID character by decrementing `index` below
            #because we've applied the backspaceCharacter.
            backspaceCount -= 1
        else:#that is, the character we're currently standing in is not a backspace and we've not
            #not encountered a backspace before which we need to apply, THEN we're standing in
            #a valid character which we need to compare
            break 
        index -= 1 #skip a backspace or a valid character
    return index

print(BackspaceCompare('xywrrmp', 'xywrrmu#p'))
'''Time Complexity: O(M + N) where M and N are the lengths of the
two strings respectively.
Space Complexity: O(1)(constant space)
'''
