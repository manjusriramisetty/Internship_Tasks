# Problem Name: Introduction to Sets - Average
# HackerRank Link:https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(arr):
    distinct_heights = set(arr)
    return sum(distinct_heights) / len(distinct_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(f"{result:.3f}")
