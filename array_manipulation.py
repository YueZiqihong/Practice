# Hackerrank exercise
# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def arrayManipulation(n, queries):
    l = [0]*(n+1)
    for i in range(len(queries)):
        l[queries[i][0]-1] += queries[i][2]
        l[queries[i][1]] -= queries[i][2]
    maximum = 0
    summ = 0
    for i in range(n):
        summ += l[i]
        if summ > maximum:
            maximum = summ
    return maximum
