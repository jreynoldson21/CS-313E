"""
DNA
"""
# F i l e : dna . py
2
3 # D e s c r i p t i o n : 
#This program reads in a file containing DNA 
#sequence pairs and returns the longest common sequence.
4
5 # S t u d e n t Name : John Reynoldson
6
7 # S t u d e n t UT EID : jsr3598
8
9 # P a r t n e r Name : Pranav Pudu
10
11 # P a r t n e r UT EID : prp768
12
13 # Course Name : CS 313E
14
15 # Unique Number : 50183
16
17 # Date C r e a t e d : 8/30/24
18
19 # Date L a s t Modified : 8/30/24

def longest_subsequence(string_1, string_2):
    string_1 = string_1.upper()
    string_2 = string_2.upper()
    m, n = len(string_1), len(string_2)
    # Create a matrix to store lengths of longest common suffixes
    lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    longest = 0
    lcs_set = set()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_1[i - 1] == string_2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
                length = lcs_matrix[i][j]
                if length > longest:
                    longest = length
                    lcs_set = {string_1[i - length:i]}
                elif length == longest:
                    lcs_set.add(string_1[i - length:i])
    
    #Sort the results alphabetically and return
    return sorted(lcs_set) if longest > 1 else []
    

def main():
    """
    This main function reads the data input files and
    prints to the standard output. 
    NO NEED TO CHANGE THE MAIN FUNCTION.
    """

    # read the data
    # number of lines
    n_lines = int(input())

    # for each pair
    for _ in range(0, n_lines):
        str_1 = input()
        str_2 = input()

        # call longest_subsequence
        subsequences = longest_subsequence(str_1, str_2)

        # write out result(s)
        if not subsequences:
            print("No Common Sequence Found")

        for subsequence in subsequences:
            print(f"{subsequence}")

        # insert blank line
        print()


if __name__ == "__main__":
    main()
