def find_best_student(student_names, student_scores):
    if len(student_scores) == 0:
        return None
    if not student_scores:
        return None
    

    highest_score = 0
    i = 0
    for score in student_scores:
        if score > highest_score:
            highest_score = score    
            highest_index= i
        i += 1 
    return student_names[highest_index]
names = ["Alice", "Bob", "Charlie", "David"]
scores = [88, 92, 99, 95]    
best_student = find_best_student(names , scores)
print (f"The best student is: {best_student}")
print ("The best student from an empty list :", find_best_student([],[]) )




 
    