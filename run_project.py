#!/usr/bin/python3

from random import randint
from time import time
from alg1_alg2 import maxSubarrayEnum as MSE, bettMaxSubarrayEnum as BMSE
from alg3 import alg3
from linear_max_subarray import linear_max_subarray as LMS
from read_and_write_data import write_csv, read_problems, write_answers


def generate_array(n):
    arry = []
    for i in range(n):
        arry.append(randint(-100, 100))
    return arry


def average_time(func, arry):
    sum = 0
    for i in range(10):
        t = time()
        func(arry)
        sum += time() - t
    return sum/10


def get_times(func, n, step):
    times = []
    for i in range(1, n, step):
        arry = generate_array(i)
        time = average_time(func, arry)
        times.append((time, i))
    return times


def get_time_data():
    write_csv('alg1.csv', get_times(MSE, 254, 9))
    write_csv('alg2.csv', get_times(BMSE, 1501, 20))
    write_csv('alg3.csv', get_times(alg3, 20001, 250))
    write_csv('alg4.csv', get_times(LMS, 300001, 3000))


def run_problems():
    problems = read_problems('MSS_Problems.txt')
    write_answers('MSS_Results.txt', run_function(MSE, problems), 'Results from enumeration algorithm:')
    write_answers('MSS_Results.txt', run_function(BMSE, problems), 'Results from better enumeration algorithm:')
    write_answers('MSS_Results.txt', run_function(alg3, problems), 'Results from divide and conquer algorithm:')
    write_answers('MSS_Results.txt', run_function(LMS, problems), 'Results from linear algorithm:')


def run_function(func, problems):
    answers = []
    for problem in problems:
        answer = func(problem)
        answers.append((problem, answer[0], answer[1]))
    return answers


def main():
    # get_time_data()
    run_problems()


if __name__ == '__main__':
    main()
