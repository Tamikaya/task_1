grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
ades_average = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
print(ades_average)
students = list(sorted(students))
print(students)
print(dict([[students[0], ades_average[0]], [students[1],ades_average[1]],[students[2],ades_average[2]], [students[3],ades_average[3]], [students[4], ades_average[4]]]))




