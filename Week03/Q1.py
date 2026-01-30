#Q1 - Student Grades List (Lists - Basic Operations)

grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grades: {grades}")
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")
print(f"Total number of grades: {len(grades)}")


#Q3 - Coordinate System (Tuples - Creation and Unpacking)
point1 = (3, 5)
point2 = (7, 2)
x1, y1 = point1
x2, y2 = point2
print(f"X1 = : {x1}, Y1 = {y1} ")
print(f"X2 = : {x2}, Y2 = {y2} ")
distance = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
print(f"Distance between the points: ", distance)
