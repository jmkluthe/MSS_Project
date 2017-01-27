#!/usr/bin/python3


def read_problems(filename):
    problems = []
    with open(filename, 'r') as fin:
        for line in fin:
            problems.append([int(i) for i in line.strip().split()])
    return problems


def write_answers(filename, answers):
    with open(filename, 'w') as fout:
        for i in range(len(answers)):
            fout.write(' '.join(str(j) for j in answers[i][0]) + '\n')
            fout.write(' '.join(str(j) for j in answers[i][1]) + '\n')
            fout.write(str(answers[i][2]) + '\n\n')


def read_answers(filename):
    answers = []
    with open(filename, 'r') as fin:
        contents = fin.readlines()
        for i in range(0, len(contents), 4):
            prob_array = [int(j) for j in contents[i].strip().split()]
            answer_array = [int(j) for j in contents[i+1].strip().split()]
            sum = int(contents[i+2])
            answers.append((prob_array, answer_array, sum))
    return answers

def test_functions():
    # test read_problems
    problems = read_problems('MSS_TestProblems.txt')
    print("Printing contents of MSS_TestProblems.txt:")
    for problem in problems:
        print(problem)

    # test read_answers
    answers = read_answers('MSS_TestResults.txt')
    print("\nPrinting contents of MSS_TestResults.txt:")
    for answer in answers:
        print(answer[0])
        print(answer[1])
        print(answer[2])

    # test write_answers
    print('\nWriting answers to file test_answer.txt')
    write_answers('test_answer.txt', answers)

if __name__ == "__main__":
    test_functions()