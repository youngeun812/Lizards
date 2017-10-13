# Lizards
First assignment for CSCI 561: Foundations of Artificial Intelligence at USC.
Essentially, we needed to solve the N Queens (Lizards) problem with P obstacles.
Three algorithms were to be implemented. DFS, BFS and Simulated Annealing.

The spec for Input and Output is:

# Input:
The file input.txt in the current directory of your program will be formatted as follows:
First line: instruction of which algorithm to use: BFS, DFS or SA
Second line: strictly positive 32-bit integer n, the width and height of the square nursery strictly positive 32-bit
Third line: integer p, the number of baby lizards
Next n lines: the n x n nursery, one file line per nursery row (to show you where the trees are). It will have a 0 where there is nothing, and a 2 where there is a tree.

# Output:
The file output.txt which your program creates in the current directory should be formatted as follows:
First line: OK or FAIL, indicating whether a solution was found or not. If FAIL, any following lines are ignored.
Next n lines: the n x n nursery, one line in the file per nursery row, including the baby lizards and trees. It will have a 0 where there is nothing, a 1 where you placed a baby lizard, and a 2 where there is a tree.

Every test case has 5 minutes to complete, exceeding which the test case fails.

# Miscellaneous
Note that these algorithms are by no means the best way to solve this particular problem.
Treating it as a Constraint Satisfaction Problem would be considerably more efficient.

I also have included an input generation script. While testing, the highest n for each algorithm (without trees)
DFS : n = 29
BFS : n = 12
SA : n >= 700

Simulated Annealing is a valley descent algorithm and to a large extend is at the mercy of the initial random state.
I successfully tested it for n = 700 after which the results were largely inconsistent.
