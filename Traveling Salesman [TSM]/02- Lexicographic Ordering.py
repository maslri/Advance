#!/usr/bin/env python
# coding: utf-8

# Lexicographic Ordering

# https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering

# Algorithm Phases:<br>
# <ol>
#     <li>Find the largest x such that p[x] < p[x+1].</li>
#         (If no such x exists, the permutation is the last permutation.) -> break statement
#     <li>Find the largest y such that p[x] < p[y].</li>
#     <li>Swap p[x] and p[y].</li>
#     <li>Reverse P[x+1 .. n].</li>
#     <li>Loop untill break statement reaches.</li>
# </ol>

# In[2]:


def swap(_list, index1, index2):
    _list[index1], _list[index2] = _list[index2], _list[index1] 
    return _list


# In[6]:


items = [0, 1, 2, 3, 4, 5]
print(items)
while True:
    #step 1
    largets_i = -1
    for i in range(len(items)-1):
        if items[i] < items[i+1]:
            largets_i = i
    if largets_i == -1:
        break

    #step 2
    largest_j = 0
    for j in range(len(items)):
        if items[largets_i] < items[j]:
            largest_j = j

    #step 3
    items = swap(items, largets_i, largest_j)

    #step 4
    left_half = items[:largets_i+1]
    right_half = items[largets_i+1:]
    right_half.reverse()
    items = left_half + right_half

    print(items)


# In[ ]:




