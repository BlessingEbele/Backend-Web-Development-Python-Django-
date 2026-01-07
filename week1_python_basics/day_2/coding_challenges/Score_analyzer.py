'''
a well-structured Python code challenge designed specifically to make you use integers, lists, sets, tuples, and Python operators together — perfect for strengthening fundamentals.

��� Python Code Challenge: Student Score Analyzer
��� Scenario

You are building a simple score analyzer for a class.
Each student has multiple test scores. Some scores are duplicated, and you need to analyze them using different Python data types.

��� Objectives

Your program should demonstrate the use of:

Integers

Lists

Sets

Tuples

Python operators (+, -, *, /, %, ==, >, <, and, or, in)

��� Given Data
scores = [70, 85, 90, 70, 60, 85, 95, 100, 60]
bonus_points = 5
passing_mark = 75

���️ Tasks
1️⃣ List Operations

Store the scores in a list

Calculate the total score

Calculate the average score

2️⃣ Set Operations

Convert the score list into a set

Count how many unique scores exist

3️⃣ Tuple Operations

Create a tuple of:

(minimum_score, maximum_score)

Use comparison operators to check:

If maximum_score > passing_mark

If minimum_score < passing_mark

4️⃣ Integer & Operator Logic

Add bonus_points to each score only if the score is below passing_mark

Count how many students passed after bonus points

Use logical operators (and, or)

5️⃣ Membership & Conditional Logic

Check if a score of 100 exists in the original list

Check if passing_mark exists in the set of unique scores

✅ Expected Output (Example)
Total score: 715
Average score: 79.4
Unique scores: {70, 85, 90, 60, 95, 100}
Number of unique scores: 6
Min and Max scores: (60, 100)
Highest score is above passing mark: True
Lowest score is below passing mark: True
Students passed after bonus: 6
Score 100 exists: True
Passing mark exists in unique scores: False

��� Bonus Challenge (Optional)

Replace scores below passing mark using a ternary operator

Sort the unique scores without converting back to a list

Use % (modulus) to find scores divisible by 5

��� Rules

❌ No external libraries
❌ No AI autocomplete
✅ Pure Python logic
'''

