# Python3 DFS solution to schedule chapters
# for reading in given days

# A DFS based recursive function to store
# the optimal path in path[] of size path_len.
# The variable Sum stores Sum of all edges on
# current path. k is number of days spent so far.
def assignChapters(u, path, path_len, Sum, k):
    global CHAPTERS, DAYS, NOLINK, optical_path, DAG, Min

    # Ignore the assignment which requires
    # more than required days
    if (k < 0):
        return

    # Current assignment of chapters to days
    path[path_len] = u
    path_len += 1

    # Update the optimal assignment if necessary
    if (k == 0 and u == CHAPTERS):
        if (Sum < Min):
            updateAssignment(path, path_len)
            Min = Sum

    # DFS - Depth First Search for sink
    for v in range(u + 1, CHAPTERS + 1):
        Sum += DAG[u][v]
        assignChapters(v, path, path_len, Sum, k - 1)
        Sum -= DAG[u][v]


# This function finds and prints
# optimal read list. It first creates a
# graph, then calls assignChapters().
def MinAssignment(pages):
    global CHAPTERS, DAYS, NOLINK, optical_path, DAG, MIN

    # 1) ............CONSTRUCT GRAPH.................
    # Partial Sum array construction S[i] = total pages
    # till ith chapter
    avg_pages = 0
    Sum = 0
    S = [None] * (CHAPTERS + 1)
    path = [None] * (DAYS + 1)
    S[0] = 0

    for i in range(CHAPTERS):
        Sum += pages[i]
        S[i + 1] = Sum

    # Average pages to be read in a day
    avg_pages = round(Sum / DAYS)

    # DAG construction vertices being chapter name &
    # Edge weight being |avg_pages - pages in a chapter|
    # Adjacency matrix representation
    for i in range(CHAPTERS + 1):
        for j in range(CHAPTERS + 1):
            if (j <= i):
                DAG[i][j] = NOLINK
            else:
                Sum = abs(avg_pages - (S[j] - S[i]))
                DAG[i][j] = Sum

    # 2) ............FIND OPTIMAL PATH................
    assignChapters(0, path, 0, 0, DAYS)

    # 3) ..PROPTIMAL READ LIST USING OPTIMAL PATH....
    print("Optimal Chapter Assignment :")
    ch = None
    for i in range(DAYS):
        ch = optimal_path[i]
        print("Day", i + 1, ": ", ch, end=" ")
        ch += 1
        while ((i < DAYS - 1 and ch < optimal_path[i + 1]) or
               (i == DAYS - 1 and ch <= CHAPTERS)):
            print(ch, end=" ")
            ch += 1
        print()


# This function updates optimal_path[]
def updateAssignment(path, path_len):
    for i in range(path_len):
        optimal_path[i] = path[i] + 1


# Driver Code

# Define total chapters in the book
# Number of days user can spend on reading
CHAPTERS = 4
DAYS = 3
NOLINK = -1

# Array to store the final balanced schedule
optimal_path = [None] * (DAYS + 1)

# Graph - Node chapter+1 is the sink
#		 described in the above graph
DAG = [[None] * (CHAPTERS + 1)
       for i in range(CHAPTERS + 1)]

Min = 999999999999
pages = [7, 5, 6, 12]

# Get read list for given days
MinAssignment(pages)
