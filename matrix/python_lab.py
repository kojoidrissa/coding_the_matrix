# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.
#http://codingthematrix.com/pythontutor.html


## 1: (Task 1) Minutes in a Week
minutes_in_week = 7 * 24 * 60


## 2: (Task 2) Remainder
remainder_without_mod = 2304811 - (47 * (2304811//47))

## 3: (Task 3) Divisibility
divisible_by_3 = 673 % 3 == 0 and 909 % 3 == 0


## 4: (Task 4) Conditional Expression
x = -9
y = 1/2
expression_val = 1



## 5: (Task 5) Squares Set Comprehension
first_five_squares = { x**2 for x in {1,2,3,4,5} }



## 6: (Task 6) Powers-of-2 Set Comprehension
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }



## 7: (Task 7) Double comprehension evaluating to nine-element set
X1 = { 1,2,3}
Y1 = { 3,4,5}
x1y1 = {x*y for x in X1 for y in Y1}
###I decreased the overlap in the sets
###After solving Task 8, I realized it's a matter of common factors
###not overlap



## 8: (Task 8) Double comprehension evaluating to five-element set
X2 = {1,2,4}
Y2 = {8,16,32}
x2y2 = {x*y for x in X2 for y in Y2}
###I used powers of 2 as my set elements. I wonder if this works for other
###sets of powers
###Yes: here's powers of 3
###{ 3**x for x in {0,1,2,3,4,5} }
'''
X2 = {1, 3, 9}
Y2 = {27, 81, 243}
x2y2 = {x*y for x in X2 for y in Y2}
'''


## 9: (Task 9) Set intersection as a comprehension
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
# Replace { ... } with a one-line set comprehension that evaluates to the intersection of S and T
S_intersect_T = {x for x in S if x in T}



## 10: (Task 10) Average
list_of_numbers = [20, 10, 15, 75]
# Replace ... with a one-line expression that evaluates to the average of list_of_numbers.
# Your expression should refer to the variable list_of_numbers, and should work
# for a list of any length greater than zero.
list_average = sum(list_of_numbers) / len(list_of_numbers) 



## 11: (Task 11) Cartesian-product comprehension
# Replace ... with a double list comprehension over {'A','B','C'} and {1,2,3}
cartesian_product = [[x,y] for x in {'A','B','C'} for y in {1,2,3}]



## 12: (Task 12) Sum of numbers in list of list of numbers
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Replace ... with a one-line expression of the form sum([sum(...) ... ]) that
# includes a comprehension and evaluates to the sum of all numbers in all the lists.
LofL_sum = sum([sum(x) for x in LofL])
###Use the list comprehension to create a list of the sums of the sub-lists,
###then sum that list



## 13: (Task 13) Three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
zero_sum_list = [(x,y,z) for x in S for y in S for z in S if x+y+z == 0]
'''This also works and seems a BIT more elegant
zsl = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z)) == 0]
I realized I could give the tuple being formed TO the sum function,
as it takes an iterable
'''


## 14: (Task 14) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
exclude_zero_list = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z)) == 0 and (x,y,z) != (0,0,0)]


## 15: (Task 15) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears
first_of_tuples_list = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z)) == 0 and (x,y,z) != (0,0,0)][0]



## 16: (Task 16) List and set differ
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))
example_L = [1,1,2]
###any list with a repeated element



## 17: (Task 17) Odd numbers
# Replace {...} with a one-line set comprehension over a range of the form range(n)
odd_num_list_range = {i for i in range(1,100,2)}
###start range at 1, step of 2


## 18: (Task 18) Using range and zip
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(0,5), L))
###Use `list()` to transform the output of the zip(an interable) into a list
###w/o using a list comprehension



## 19: (Task 19) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
list_sum_zip = [x+y for x, y in zip(A, B)]
###List comprehension turns output of zip(an iterable; Need to study this more)
###into a list



## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']
value_list = [bond[k] for bond in dlist]
###get the value for each occurance of key 'k' in a list of dictionaries



## 21: (Task 21) Extracting the value corresponding to k when it exists
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
#Replace [...] with a one-line comprehension 
value_list_modified_1 = [x.get(k, 'NOT PRESENT') for x in dlist] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [x.get(k, 'NOT PRESENT') for x in dlist] # <-- as you do here



## 22: (Task 22) A dictionary mapping integers to their squares
# Replace {...} with a one-line dictionary comprehension
square_dict = {k:k**2 for k in range(100)}
###Remeber: if you want a range of x continuous elements, `range(x)` works


## 23: (Task 23) Making the identity function
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension
identity_dict = {key:key for key in D}
###Identity function: f(x) = x; https://en.wikipedia.org/wiki/Identity_function



## 24: (Task 24) Mapping integers to their representation over a given base
base = 10
digits = set(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variable 'base' so it will work if a different number
# is assigned to this variable.
representation_dict = {d:(d//base**2, d%base**2//base**1, d%base**1) for d in range(base**3)}
###To get full range of 3-digit numbers, you need `base**3`
###The rest is similar to my Version Number function


## 25: (Task 25) A dictionary mapping names to salaries
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
listdict2dict = {k:id2salary[names.index(k)] for k in names if names.index(k) in id2salary.keys()}
###test = {k:id2salary[names.index(k)] for k in names}
'''Iterate through the LIST to get the keys, use the list indexes to DIRECTLY
access the DICTIONARY values. The `test` code tries that without worrying
about the "not every employee ID is represented in id2salary." condition
'''

## 26: (Task 26) Procedure nextInts
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def nextInts(L): return [x+1 for x in L]
###Standard list comprehension


## 27: (Task 27) Procedure cubes
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def cubes(L): return [i**3 for i in L] 
###Standard list comprehension


## 28: (Task 28) Procedure dict2list
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def dict2list(dct, keylist): return [dct[key] for key in keylist]
###Iterate through keylist, use those keys to return value from dct


## 29: (Task 29) Procedure list2dict
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
def list2dict(L, keylist): return { k:v for (k,v) in zip(keylist, L)}
###zip L & keylist then run a dictionary comprehension over the zip

