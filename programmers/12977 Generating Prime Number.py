'''
https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
Generating Prime Number
Description
Suppose that you want to count the number of cases where a prime number is generated 
when adding 3 numbers among the given numbers. Given an array nums containing 
numbers as the parameter, write a function solution to return the number of 
cases where a prime number is generated when adding 3 different numbers among nums.

소수 만들기
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 
서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

nums = [1,2,7,6,4]
'''
def solution(nums):
    import numpy as np
    from itertools import combinations
    def isPrime(x) :
      return False if ((x%np.array(range(2,x)))==0).any() else True
    combi = list(combinations(nums, 3))
    ans_list = []
    for val in combi :
      if isPrime(val[0]+val[1]+val[2] ) :
        ans_list.append(val)
    print(ans_list)
    answer = len(ans_list)
    return answer
'''
Solution by other
'''
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
# END