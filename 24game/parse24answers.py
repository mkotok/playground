# import matplotlib.pyplot as plt

def read_csv(fp):
    cases = []
    answers = []
    with open(fp, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            cases.append(line[:4])
            answers.append(line[-1])
    return cases, answers


test_cases, test_answers = read_csv('answers24game.csv')
gold_cases, gold_answers = read_csv('answers24game_gold.csv')

assert test_cases == gold_cases
test = [0 if x == "None" else 1 for x in test_answers]
gold = [0 if x == "None" else 1 for x in gold_answers]

print test == gold
