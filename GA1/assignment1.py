'''
    This file contains the template for Assignment1.  You should fill the
    function <majority_party_size>.  The function, recieves two inputs:
      (1) n: the number of delegates in the room, and
      (2) same_party(int, int): a function that can be used to check if two members are
      in the same party.

    Your algorithm in the end should return the size of the largest party, assuming
    it is larger than n/2.

    I will use <python3> to run this code.
'''
# CS325 Group Assignment 1
# Alex Young, Steven Bui, Ethan Ng
# O(nlogn) runtime
def majority_party_size(n, same_party):
    '''
        n (int): number of people in the room.
        same_party (func(int, int)): This function determines if two delegates
            belong to the same party.  same_party(i,j) is True if i, j belong to
            the same party (in particular, if i = j), False, otherwise.

        return: The number of delegates in the majority party.  You can assume
            more than half of the delegates belong to the same party.
    '''

    # Replace the following line with your code.

    low = int(0)
    high = int(n - 1)
    print ("delegates:", n, "left:", low, "right:", high)
    x, y = split(low, high, same_party) # split function returns majority party delegate and count

    print ("majority index:", x, " count:", y)

    return y # y is the count of the majority delegate party

# O(logn) runtime
def split (low, high, same_party):
    m = int((low + high + 1) / 2)
    c = int(high - low + 1)
    if (c == 1):
        return low, 1
    if (c == 2):
        i1 = low
        i2 = high
        c1 = 1
        c2 = 1
    if (c >= 3): # as long as there are at least room for 3 delegates to split, the function will recursively half itself 
        i1, c1 = split(low, m - 1, same_party)
        i2, c2 = split(m, high, same_party)
    print ("m:", m, "left:", low, "right:", high, "c1:", c1, "c2:", c2)
    if (i1 == -1 and i2 != -1): # case where one of the previous pair didn't match
        print (i2, c2)
        return i2, c2 + count(low, m - 1, i2, same_party)
    elif (i1 != -1 and i2 == -1):
        print (i1, c1)
        return i1, c1 + count(m, high, i1, same_party)
    elif (i1 == i2): # case where a single index is being checked
        print (i1, c1)
        return i1, c1 + count(m, high, i1, same_party)
    elif (same_party(i1, i2) == False): # case where a pair does not match
        c1 = c1 + count(m, high, i1, same_party)
        c2 = c2 + count(low, m - 1, i2, same_party)
        if (c1 == c2): # if the mismatch has equal counts, return a fake index and no count (they cancel)
            print (-1, 0)
            return -1, 0
        elif (c1 < c2): # if one of the parties has more delegates, it gets passed onward
            print (i2, c2)
            if (c1 + c2 == c):
                return i2, c2
            else:
                return i2, c2
        else: # case where pair of indexes match parties
            print (i1, c1)
            if (c1 + c2 == c): # if the total count is equal the total of previous counts, everything is accounted for
                return i1, c1
            else: # if not, make sure the previous count is added up
               return i1, c1
    else: #case where a pair does match, return a index and the total count
        print (i1, c1 + c2)
        return i1, c1 + c2

# O(n) runtime
def count(low, high, delegate, same_party): # function to loop through and count the previous pair's same party members
    c = 0
    index = low
    while (index <= high):
        if (same_party(delegate, index) == True):
            c = c + 1
        index = index + 1
   
    return c