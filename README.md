# Collatzs-Hypothesis


In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:



Here is the logic of the unproven algorithm(Collatz's Hypothesis)



take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate as c0 ÷ 2;
if it's odd, evaluate as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for any natural number. it may even require artificial intelligence. 

But now let's solve this unproven logic using python. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

ex:



Input: 23

Output:

70
35.0
106.0
53.0
160.0
80.0
40.0
20.0
10.0
5.0
16.0
8.0
4.0
2.0
1.0
The total steps count is  15
