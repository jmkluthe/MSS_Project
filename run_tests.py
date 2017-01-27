#!/usr/bin/python3

""" Calls each algorithm function on the test problem set, and compares the returned
answers to the known correct answers """

from read_and_write_data import read_problems as rp, read_answers as ra
from linear_max_subarray import linear_max_subarray as lms

def test_function(func):
    test_problems = rp('MSS_TestProblems.txt')
    test_answers = ra('MSS_TestResults.txt')
    for i in range(len(test_problems)):
        answer = func(test_problems[i])
        print('Returned Answer:  {}'.format(answer))
        print('Correct Answer:   {}'.format(test_answers[i][1:3]))
        if answer == test_answers[i][1:3]:
            print('Pass\n')
        else:
            print('Fail\n')


if __name__ == "__main__":
    test_function(lms)