'''
You are given a string A of size N consisting of lowercase alphabets.
You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
Find the minimum number of distinct characters in the resulting string.
Problem Constraints
1 <= N <= 100000
0 <= B < N
Input Format
The first argument is a string A.
The second argument is an integer B.
Output Format
Return an integer denoting the minimum number of distinct characters in the string.
Example Input
A = "abcabbccd"
B = 3

Example Output
2
'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        char_count = {}

        for char in A:
            if char not in char_count:
                char_count[char] = 0

            char_count[char] += 1

        counts = sorted(char_count.values())

        # Current number of distinct characters
        answer = len(counts)

        # Excluding the last element because there has to be atleast 1 character
        for i in range(len(counts) - 1):
            # We can substitute all the characters
            # Assume you are substituting for the max occurred character
            if counts[i] <= B:
                B -= counts[i]
                answer -= 1

            # If we can't substitute all counts[i]
            # We definitely can't substitute for any upcoming values
            else:
                break

        return answer
