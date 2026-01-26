'''
Challenge 4: Score Analyzer

Create:
��� score_analyzer.py

Given:

scores = [45, 67, 89, 32, 74]


Tasks:

Print the first score and last score

Print the average score (hint: use sum() and len())

If average ≥ 50 → print "Pass"

Else → print "Fail"

Concepts tested: lists, indexing, integers, floats, conditionals
'''
scores = [45, 67, 89, 32, 74]
print(f"The first score: {scores[0]} and the last score: {scores[4]}")

average = sum(scores) / len(scores)
print(f"the average: {average}")

if average >= 50:
    print("Pass")
else:
    print("Fail")
