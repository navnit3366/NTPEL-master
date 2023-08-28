#Q: Write a Python program to sort a list of tuples using Lambda.

subject_marks = [('English', 79), ('Chemistry', 90), ('Maths', 80), ('Information Practices', 95), ('Physics', 92)]

print("\nOriginal list of tuples: ",subject_marks)

subject_marks.sort(key = lambda x: x[1])    # x[1] says sort by [1]th positions of tuples in the list

print("\nSorted list of tuples: ",subject_marks,end='\n\n')
