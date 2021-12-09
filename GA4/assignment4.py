'''
    This file contains the template for Assignment4.  For testing it, I will place it
    in a different directory, call the function <first_second_third_mst>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

'''
Alex Young, Ethan Ng, Steven Bui
CS 325
GA 4
11/22/2020
'''

from queue import PriorityQueue
import time


def first_second_third_mst(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''

    #total runtime of O(VE)
    #read in input file to a priority queue
    start_time = time.time()
    q = PriorityQueue()
    length = 0
    lengthB = 0
    lengthC = 0
    mstA = {}
    with open(input_file_path, "r") as f: # loops through E edges
        n = int(f.readline().strip("\n"))
        i = 0
        if (n != 1):
            for lines in f:
                int_list = [int(i) for i in lines.strip("\n").split(",")]
                i = i + 1
                for j in range(i, n):
                    q.put((int_list[j], (i - 1, j)))

    if (n > 1):
        (length, lengthB, lengthC) = mst(q, n, mstA)

    if (n < 3):
        total1 = str(length)
        total2 = str("none")
        total3 = str("none")

    else:
        total1 = str(length)
        total2 = str(lengthB)
        total3 = str(lengthC)

    total = total1 + "\n" + total2 + "\n" + total3
    f = open(output_file_path, "w")
    f.write(total)
    f.close()

    #print(total)
    #print("--- %s seconds ---" % (time.time() - start_time))
    return total


def mst(q, n, mstA):
    x = 0
    path = [(x,) for x in range(n)]
    prev = {}
    length = 0
    delta1 = -1
    delta2 = -1
    temp1 = -1
    temp2 = -1
    
    for x in range(n): # loops through V edges
        s = True
        d = True

        while(s and d and q.empty() != True): # loops through a constant number of edges
            u = q.get()
            done = False
            for z in range(len(path)): # loops V edges
                if (done == True):
                    pass
                elif (path[z].count(u[1][0]) != 0 and path[z].count(u[1][1]) != 0): # both vertices in same path
                    s = True
                    done = True
                else:
                    s = False
            
            if (s != True): # both vertices in different paths
                mstA[x] = (u[0], u[1][0], u[1][1])
                vX = 0
                vY = 0
                for z in range(len(path)): # record the path that vertices are in (V edges)
                    if (path[z].count(u[1][0]) != 0):
                        vX = z
                    if (path[z].count(u[1][1]) != 0):
                        vY = z
                path[vX] = path[vX] + path[vY]
                path.pop(vY)
                prev[mstA[x]] = path.copy()
                length = length + u[0] #update the mst length

            if s: #if vertices in the same path
                delta = -1
                prevW = (0, 0, 0)
                low = []
                low.clear()
                for i in range(x): # for all the current edges (V)
                    icheck = -1
                    jcheck = -1
                    diff = u[0] - mstA[i][0]
                    neighbor = True
                    dupdiff = -1
                    if (delta2 > temp2):
                        temp2 = delta2
                    if ((diff <= delta2 or delta2 == -1) and delta2 != 0): # check edge if it can create a second mst if it has an eligible weight difference
                        p = 0
                        if (i > 0):
                            p = i - 1
                        for j in range(len(prev[mstA[p]])): # if the vertices are in different paths of the previous mst edge (if they connect these paths together) (V)
                            if (prev[mstA[p]][j].count(u[1][0]) != 0):
                                icheck = j
                            if (prev[mstA[p]][j].count(u[1][1]) != 0):
                                jcheck = j
                        if (icheck != -1 and jcheck != -1 and icheck != jcheck):
                            if (delta == -1):
                                delta = diff
                            elif (delta == diff):
                                neighbor = False
                                for h in range(len(prev[mstA[p]])): #if we have repeated weights, check if they are in the same path (V)
                                    if (prev[mstA[p]][h].count(mstA[p][2]) == prev[mstA[p]][h].count(prevW[1]) and prev[mstA[p]][h].count(mstA[p][2]) != 0):
                                        neighbor = True
                                    if (prev[mstA[p]][h].count(mstA[p][1]) == prev[mstA[p]][h].count(prevW[2]) and prev[mstA[p]][h].count(mstA[p][1]) != 0):
                                        neighbor = True
                                if (neighbor == True):
                                    dupdiff = diff
                                else:
                                    dupdiff = 0
                            else:
                                delta = min(delta, diff)
                            if (diff <= dupdiff or dupdiff == -1): # if current edge is the lowest weight for this edge
                                low.append(delta) # maybe could fix logic here with dupdiff and temp
                                (temp1, temp2) = deltaX(delta, temp1, temp2)
                            prevW = mstA[p]
                
                if (delta != -1):
                    low.sort() # minimum weight at low[0]
                    if (len(low) > 1):
                        if (low[0] == low[1]): # this means that we had a duplicate diff
                            delta = low[0]
                            (delta1, delta2) = deltaX(delta, delta1, delta2)
                            (delta1, delta2) = deltaX(delta, delta1, delta2)
                        else:
                            (delta1, delta2) = deltaX(delta, delta1, delta2)
                    else:
                        (delta1, delta2) = deltaX(delta, delta1, delta2)
                
            if (len(path) == 1 and len(mstA) == x): # stop if mst is full and the weight of all edges left is too large to impact delta
                deltaCont = max(delta1, delta2)
                if ((u[0] - (deltaCont)) > mstA[x-1][0] and delta2 != -1):
                    d = False

    if (delta2 == -1): # for edge cases where an edge generates the 2nd and 3rd mst but they arent duplicates -- logic probably off here
        delta2 = temp2
    
    return (length, length + delta1, length + delta2)


def deltaX(diff, delta1, delta2): # updates delta1 and delta2 by the difference in the current edge and mst edge
    if (delta1 == -1):
        delta1 = diff
    elif (delta1 == diff):
        if (delta2 == -1):
            delta2 = diff
        else:
            delta2 = min(diff, delta2)
    else:
        temp = delta1
        if (delta1 >= diff):
            if (delta2 == -1):
                delta2 = temp
            else:
                delta2 = min(temp, delta2)
            delta1 = min(delta1, diff)
        else:
            if (delta2 == -1):
                delta2 = diff
            else:
                delta2 = min(diff, delta2)
    return (delta1, delta2)


#first_second_third_mst('input0.in', 'input0.out')
