#The correction file

# Given data
scores = [70, 85, 90, 70, 60, 85, 95, 100, 60]
bonus_points = 5
passing_mark = 75

# 1️⃣ List operations
total_score = sum(scores)
average_score = total_score / len(scores)

print("Total score:", total_score)
print("Average score:", round(average_score, 2))

# 2️⃣ Set operations
unique_scores = set(scores)
print("Unique scores:", unique_scores)
print("Number of unique scores:", len(unique_scores))

# 3️⃣ Tuple operations
min_max_scores = (min(scores), max(scores))
min_score, max_score = min_max_scores

print("Min and Max scores:", min_max_scores)
print("Highest score above passing mark:", max_score > passing_mark)
print("Lowest score below passing mark:", min_score < passing_mark)

# 4️⃣ Bonus points logic
modified_scores = []
for score in scores:
    if score < passing_mark:
        score += bonus_points
    modified_scores.append(score)

passed_students = 0
for score in modified_scores:
    if score >= passing_mark:
        passed_students += 1

print("Modified scores:", modified_scores)
print("Students passed after bonus:", passed_students)

# 5️⃣ Membership checks
print("Score 100 exists:", 100 in scores)
print("Passing mark exists in unique scores:", passing_mark in unique_scores)
