# Convert Marks to Grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {} # Empty Dic
for i in student_scores:
    if student_scores[i] >= 91: # student_scores[i] prints only the value and it is comparing with user defined value
        student_grades[i] = "Outstanding" # Updating the key to empty Dic with the string
    elif student_scores[i] >= 81:
        student_grades[i] = "Exceeds Expectations"
    elif student_scores[i] >= 71:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] =  "Fail"
print(student_grades)
