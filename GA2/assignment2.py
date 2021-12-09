'''
    This file contains the template for Assignment2.  For testing it, I will place it
    in a different directory, call the function <vankin_max_score>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

def vankin_max_score(input_file_path, output_file_path):
    '''
    This function will ontain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    #read in input file
    array = []
    with open(input_file_path, "r") as f:
        size = int(f.readline().strip("\n"))
        for lines in f:
            int_list = [int(i) for i in lines.strip("\n").split(",")]
            array.append(int_list)

    total = 0
    list = [0] * size
    #temporary size value for array
    n = size - 1

    #nested for loop that goes through each element of the list of lists, starts at the bottom right corner
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            #count variable to iterate through list of max values
            c = n - j
            #bc bottom right corner
            if (i == n and j == n):
                list[0] = array[n][n]
                total = array[n][n]
            #bc for bottom row (compares previous value for a maximum)
            elif (i == n):
                list[c] = array[n][j] + max(list[c-1], 0)
            #bc for right column (checks if value will increase the total)
            elif (j == n):
                list[0] = array[i][n] + max(list[0], 0)
            #for any other index, compare to value below and value to the right, adds max value
            else:
                list[c] = array[i][j] + max(list[c], list[c-1])
            #checks to see if the current column max is greater than the total max, replaces if so, else nothing otherwise
            total = max(total, list[c])

    #generate output file
    total = str(total)
    f = open(output_file_path, "w")
    f.write(total)
    f.close()

    return total


vankin_max_score('input0.in', 'input0.out')
