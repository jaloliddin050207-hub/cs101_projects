raw_scores = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 75),
    ("Alice", "Physics", 90),
    ("Charlie", "History", 88),
    ("Bob", "Physics", 82),
    ("Alice", "History", 92)
]
gradebook={}
for student, subject, score in raw_scores:
    if student not in gradebook:
        gradebook[student] = {} 
        gradebook[student][subject]=score
print(gradebook)
   
