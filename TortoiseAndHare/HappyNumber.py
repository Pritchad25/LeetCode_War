#!/usr/bin/python3
'''Any number will be called a happy number if it leads us to number 1
after repeatedly replacing it with a number equal to the sum of the
square of all of its digits. All other (not-happy) numbers will never 
reach 1. Instead they will be stuck in a cycle of numbers which does 
not include 1.

Question Clarification
23 will be called a happy number if it leads us to number 1 AFTER
REPEATEDLY(over&over again) replacing 23 with a number == to the sum of 
the square of all of its digits (where 'it' is 23).
All other (not-happy) numbers will never reach 1; Instead they will be stuck 
in a cycle of numbers which does not include 1.
23
2 squared + 3 squared = 4 + 9 = 13. Now replace this number(13) with a
a number == to the sum of the square of all of its digits
13
1 squared + 3 squared = 1 + 9 = 10. replace 10
10
1 squared + 0 squared = 1 + 0 = 1. Therefore, 23 is a happy number.

Example 2
12 is not a happy number because it doesnt lead to 1; instead 12 is stuck in a
cycle of numbers 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 meaning we can never reach 1.

Approach:
-The process, defined above, to find out if a number is a happy number or 
not, always ends in a cycle.
-If the number is a happy number, the process will be stuck in a cycle on number 1.
-if the number is not a happy number then the process will be stuck in a cycle with 
a set of numbers as we saw in example 2; our process got stuck in a cycle with the 
following numbers: 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
-Each number which we trying to determine if its happy or not will definitely have a cycle
-Therefore, we will use the same fast & slow pointer strategy of LinkedListCycle problem
to find the cycle and once the cycle is found, we will see if the cycle is stuck on number
1 to determine if the number is happy or not.
`digit = num % 10` firstly get the division remainder, `sum += digit * digit` because we
want to get the sum of the squares of the individual digits, we decrement and/or get the
next digit of the number by determing the quotient of the number `num` (num /= 10)
'''
def find(num):
    slow = num
    fast = num
    while True:
        slow = find_square_sum(slow)#move 1 step
        fast = find_square_sum(find_square_sum(fast))#move 2 steps
        if slow == fast:#found the cycle
            break
    return slow == 1  #see if the cycle is stuck on the number '1'

def find_square_sum(num):
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit * digit
            num //= 10
        return sum

print(find(12))
'''Time Complexity: O(logN): time complexity of the algorithm is difficult to determine.However,
we know the fact that all unhappy numbers eventually get stuck in the cycle:
4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4. Then search `unhappy numbers` on
wikipedia and youll find the explanation there.
Space Complexity: O(1)
'''
