#!/usr/bin/env python3
'''Given a set of investment projects with their respective profits, we 
need to find the most profitable projects. We are given an initial capital 
and are allowed to invest only in a fixed number of projects. Our goal is 
to choose projects that give us the MAXIMUM PROFIT.
We can start an investment project only when we have the required capital. 
Once a project is selected, we can assume that its profit has become our 
capital.

Example 1
Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1,
Number of Projects=2

`Project Capitals` is the required capital for each project in 
`Project Profits`.In this case, 0 is the required capital for the project 
with profit of 1(the first project); 1 is the capital required for the 
project with profit of 2(the second project); 2 is the capital required for
the project with profit of 3(the third project).So, in order for us to 
understand easily, we can align the above like this.
Project Capitals =[0,1,2]
Project Profits = [1,2,3]
-So, we are supposed to find only 2 projects that gives us the Maximum 
Profit, with us having an initial capital of 1.
-With initial capital of 1, we can start the second project with profit
of 2.Because, as per problem statement, once we start a project, we can
assume that its profit has become our capital, our total capital goes to 
3(initial Capital (1) + profit(2)).
-With capital of 3, we now have enough capital to start the third project(
which has required capital of 2) and our total capital goes to 
6(initial capital(3) + profit(3))
-After the completion of the two projects, our total capital will be 
6(1 + 2 + 3). Therefore, with an initial capital of 1, 2 projects that give
us the MAXIMUM PROFIT is the 2nd & 3rd project.

Example 2
Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], 
Initial Capital=0, Number of Projects=3

Project Capitals = [0,1,2,3]
Project Profits  = [1,2,3,5]
-So, we are supposed to find 3 projects that give us the MAXIMUM profit, with
us having an initial capital of 0.
-With capital of 0, we can start the 1st project, bringing our total capital
to 1(initial capital 0 + profit 1)
-With capital of 1, we can start the 2nd project with profit of 2, bringing
our total capital to 3(capital  + 2 profit)
-With capital of 3, we could start the 3rd project with profit of 3, but 
that wouldnt give us the MAXIMUM PROFIT.Instead, we start the 4th project
with profit of 5 since we have its required capital of 3, thus bringing our
total capital to 8(3 + 5).
-After the completion of the 3 projects, our total capital will be 
8(1 + 2 + 5). Therefore, with an initial capital of 0, 3 projects that give
us the MAXIMUM PROFIT is the 1st, the 2nd & the 4th project.

Solution
-While selecting projects we have 2 constraints:
1. We can select a project only when we have the required capital.
2. There is a maximum limit on how many projects we can select.
-Since we don't have any constraint on time, we should choose a project, 
among the projects for which we have enough capital, which gives us a 
maximum profit.Following this greedy approach will give us the best 
solution.

-While selecting a project, we will do 2 things:
1. Find all the projects that we can choose with the available capital.
2. From the list of projects in the 1st step, choose the project that gives
us a maximum profit.

-We can follow the Two Heaps approach similar to MedianOfAStream. Here are 
the steps of our algorithm:
1. Add all project capitals(ie, the capital requirement of each project) to
a Min-Heap, so that we can select a project with the smallest capital 
requirement.
2. Go through the top projects of the Min-heap and filter(select) the 
projects that can be completed within our available capital(Initial Capital),
within the context of the fixed amount of projects we are supposed to invest
in. Insert the profits of all these projects into a max-heap, so that we can 
choose a project with the maximum profit/Highest profit.
3. Finally, select the top project of the max-heap for investment.
4. Repeat the 2nd and 3rd steps for the required number of projects.

-`for i in range(len(capitals)):
            heapq.heappush(min_capital_heap, (capitals[i], i))` - in this 
first for loop, we are looping through the capital requirements of each 
project in the `capitals` list and putting both the capitals and their 
respective indices(positions) in the `capitals` list as a tuple in the Min
Heap. We put the indices there so that we keep track of the original 
position of each capital value in the `capitals` list.When the loop exits, 
the project with smallest capital requirement will be at the top of the 
Min-Heap.
-`for _ in range(number_of_projects):` - In this loop, the `_` character 
indicates that the loop variable is not going to be used inside the loop. 
Essentially, it means "I need to loop this many times, but I don't care 
about the loop variable itself, because I'm not gonna use it inside the loop."
-`while min_capital_heap and min_capital_heap[0][0] <= available_capital:`ie
if the Min-Heap is not empty AND the SMALLEST capital requirement for a project 
is less or equal the available capital, then that means we can invest in 
this project as we have the required capital(`min_capital_heap[0][0]` - 
min_capital_heap is a Min-heap implemented using python lists, meaning
the SMALLEST capital requirement will be at index 0 of the list.Because our
min-heap holds a tuple of each capital requirement & its index or position
in the original `capitals` list, to get this SMALLEST capital requirement, 
we first access the tuple at index 0 of the min-heap(min_capital_heap[0]) 
and then we get the SMALLEST capital requirement, which will be at index 0 of 
the tuple,(hence why min_capital_heap[0][0])), so we invest into this project
-`min_capital_heap[0][0] <= available_capital` - ie, in order for us to 
invest in a project, the project's capital requirement has to be equal to
our initial capital `available_capital` or less hence <=.
-`capital_index = heapq.heappop(min_capital_heap)[1]` - we are popping the
index or position of the SMALLEST capital requirement, which index is at
index 1 of the tuple, because when we pop from Min-Heap, we get a 
tuple returned and then we access index 1 of the tuple which is where the
index we want is sitting at.We store or save this index in `capital_index`.

'''
import heapq

class MaximizeCapital:
    def __init__(self):
        pass

    @staticmethod
    def find_maximum_capital(capitals, profits, number_of_projects, initial_capital):
        min_capital_heap = []
        max_profit_heap = []

        # insert all project capitals to a min-heap
        for i in range(len(capitals)):
            heapq.heappush(min_capital_heap, (capitals[i], i))

        available_capital = initial_capital
        for _ in range(number_of_projects):
            # find all projects(in Min heap) that can be selected within 
            # the available capital and insert them in a  max-heap
            while min_capital_heap and min_capital_heap[0][0] <= available_capital:
                capital_index = heapq.heappop(min_capital_heap)[1]
                heapq.heappush(max_profit_heap, (-profits[capital_index], capital_index))

            # terminate if we are not able to find any project that can be completed within the available capital
            if not max_profit_heap:
                break

            # select the project with the maximum profit
            available_capital += -heapq.heappop(max_profit_heap)[0]

        return available_capital

if __name__ == "__main__":
    result = MaximizeCapital.find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)
    print("Maximum capital:", result)
    result = MaximizeCapital.find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)
    print("Maximum capital:", result)
