'''
    This file contains the template for Assignment3.  For testing it, I will place it
    in a different directory, call the function <vidrach_itky_leda>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''
from collections import deque
import time

def vidrach_itky_leda(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    #read in input file
    start_time = time.time()
    array = []
    with open(input_file_path, "r") as f:
        size = int(f.readline().strip("\n"))
        for lines in f:
            int_list = [int(i) for i in lines.strip("\n").split(",")]
            array.append(int_list)
    n = size - 1

    print(size)
    for row in array:
        for column in row:
            print(column, end=" ")
        print()

    
    rx = 0
    ry = 0
    bx = n
    by = n

    beststeps = -1
    steps = deque()
    steps.appendleft(0)
    bag = deque([(rx, ry, bx, by)])
    redvisit = {(rx, ry, array[bx][by], array[bx][by]) : True}
    bluevisit = {(bx, by, array[rx][ry]) : True}
    previsit = {(bx, by, rx, ry) : 0}

    while (bag):
        tempcord = bag.pop()
        rx = tempcord[0]
        ry = tempcord[1]
        bx = tempcord[2]
        by = tempcord[3]
        temp = steps.pop()

        if (array[rx][ry] == 0 and array[bx][by] == 0):
            continue

#        redvisit[(rx, ry)] = True
#        bluevisit[(bx, by)] = True
#        if ((rx, ry, bx, by) in previsit):
#            continue
#        else:
        previsit[(bx, by, rx, ry)] = temp + 1

        if (rx == n and ry == n and bx == 0 and by == 0):
            if (beststeps == -1 or beststeps > temp):
                beststeps = temp
            break 

        else:            
            if (rx + array[bx][by] < size and (rx + array[bx][by] != bx or ry != by) and not ((rx + array[bx][by], ry) in redvisit)):
                if ((rx + array[bx][by], ry, bx, by) in previsit):
                    beststeps = previsit[(rx + array[bx][by], ry, bx, by)] + temp
                    break
                redvisit[(rx + array[bx][by], ry, array[bx][by])] = True
                #previsit[(bx, by, rx + array[bx][by], ry)] = temp + 1
                bag.appendleft((rx + array[bx][by], ry, bx, by))
                steps.appendleft(temp + 1)
            
            if (ry + array[bx][by] < size and (rx != bx or ry + array[bx][by] != by) and not ((rx, ry + array[bx][by]) in redvisit)):
                if ((rx, ry + array[bx][by], bx, by) in previsit):
                    beststeps = previsit[(rx, ry + array[bx][by], bx, by)] + temp
                    break
                redvisit[(rx, ry + array[bx][by], array[bx][by])] = True
                #previsit[(bx, by, rx, ry + array[bx][by])] = temp + 1
                bag.appendleft((rx, ry + array[bx][by], bx, by))
                steps.appendleft(temp + 1)
            
            if (rx - array[bx][by] >= 0 and (rx - array[bx][by] != bx or ry != by) and not ((rx - array[bx][by], ry) in redvisit)):
                if ((rx - array[bx][by], ry, bx, by) in previsit):
                    beststeps = previsit[(rx - array[bx][by], ry, bx, by)] + temp
                    break
                redvisit[(rx - array[bx][by], ry, array[bx][by])] = True
                #previsit[(bx, by, rx - array[bx][by], ry)] = temp + 1
                bag.appendleft((rx - array[bx][by], ry, bx, by))
                steps.appendleft(temp + 1)
            
            if (ry - array[bx][by] >=0 and (rx != bx or ry - array[bx][by] != by) and not ((rx, ry - array[bx][by]) in redvisit)):
                if ((rx, ry - array[bx][by], bx, by) in previsit):
                    beststeps = previsit[(rx, ry  - array[bx][by], bx, by)] + temp
                    break
                redvisit[(rx, ry - array[bx][by], array[bx][by])] = True
                #previsit[(bx, by, rx, ry - array[bx][by])] = temp + 1
                bag.appendleft((rx, ry - array[bx][by], bx, by))
                steps.appendleft(temp + 1)
            
            if (bx + array[rx][ry] < size and (rx != bx + array[rx][ry] or ry != by) and not ((bx + array[rx][ry], by) in bluevisit)):
                if ((rx, ry, bx + array[rx][ry], by) in previsit):
                    beststeps = previsit[(rx, ry, bx  + array[rx][ry], by)] + temp
                    break
                bluevisit[(bx + array[rx][ry], by, array[rx][ry])] = True
                #previsit[(bx + array[rx][ry], by, rx, ry)] = temp + 1
                bag.appendleft((rx, ry, bx + array[rx][ry], by))
                steps.appendleft(temp + 1)
            
            if (by + array[rx][ry] < size and (rx != bx or ry != by + array[rx][ry]) and not ((bx, by + array[rx][ry]) in bluevisit)):
                if ((rx, ry, bx, by + array[rx][ry]) in previsit):
                    beststeps = previsit[(rx, ry, bx, by  + array[rx][ry])] + temp
                    break
                bluevisit[(bx, by + array[rx][ry], array[rx][ry])] = True
                #previsit[(bx, by + array[rx][ry], rx, ry)] = temp + 1
                bag.appendleft((rx, ry, bx, by + array[rx][ry]))
                steps.appendleft(temp + 1)
            
            if (bx - array[rx][ry] >= 0 and (rx != bx - array[rx][ry] or ry != by) and not ((bx - array[rx][ry], by) in bluevisit)):
                if ((rx, ry, bx - array[rx][ry], by) in previsit):
                    beststeps = previsit[(rx, ry, bx - array[rx][ry], by)] + temp
                    break
                bluevisit[(bx - array[rx][ry], by, array[rx][ry])] = True
                #previsit[(bx - array[rx][ry], by, rx, ry)] = temp + 1
                bag.appendleft((rx, ry, bx - array[rx][ry], by))
                steps.appendleft(temp + 1)
            
            if (by - array[rx][ry] >= 0 and (rx != bx or ry != by - array[rx][ry]) and not ((bx, by - array[rx][ry]) in bluevisit)):
                if ((rx, ry, bx, by - array[rx][ry]) in previsit):
                    beststeps = previsit[(rx, ry, bx, by - array[rx][ry])] + temp
                    break
                bluevisit[(bx, by - array[rx][ry], array[rx][ry])] = True
                #previsit[(bx, by - array[rx][ry], rx, ry)] = temp + 1
                bag.appendleft((rx, ry, bx, by - array[rx][ry]))
                steps.appendleft(temp + 1)
                

            

# want to store steps to get a tile, cannot visit an already visited step
    print(beststeps)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    total = str(beststeps)
    f = open(output_file_path, "w")
    f.write(total)
    f.close()

    return total


vidrach_itky_leda('input0.in', 'input0.out')
