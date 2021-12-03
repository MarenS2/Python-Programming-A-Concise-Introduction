"""
Problem 3_1:
Write a function that reads a text file and counts the number of letters in it.
Print both the text file and the number of letters. Do this so that the
printout isn't doubled space (use an end= argument in the print statement).
Also, skip a line before printing the count. Note that it is easy to get the
number of letters in each line using the len() function.
Here is my run for HumptyDumpty.txt.  Your output should look just like this
for the autograder:
problem3_1("humptydumpty.txt")
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.
There are 141 letters in the file.
"""
#%%
def problem3_1(txtfilename):
    """ Opens file and prints its contents line by line. """
    infile = open(txtfilename)

    sum = 0

    for line in infile:
        sum = sum + len(line)
        print(line, end="") # the file has "\n" at the end of each line already

    print("\n\nThere are", sum, "letters in the file.")

    infile.close()

#%%
