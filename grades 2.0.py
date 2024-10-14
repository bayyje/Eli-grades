total_grades = int(input('Enter the total of your grades: '))
grades = input('Enter your grades: ').split() # Converting string into list
grade_list = list(map(int, grades)) # Converting list with string number to list with int number

# Creating dictionary so we can easily access and working with elements

grades_dic = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
    'F' : 0
}

# # We are using For loops so we can go through every elements in the list

# ''' Using method range(from 90 to 100) find elements from 90 to 100. If we set 1 to 10, this method will count from 1 to 9
# That's why are counting from 90 to 101
# '''
for x in range(90, 101):
# 	''' Method count() counting the same elements in the list.
# 		And then we adding this information to variable A
# 	'''

    # Taking key and value from the dictionary
	grades_dic['A'] += grade_list.count(x)

for x in range(75, 90):
	grades_dic['B'] += grade_list.count(x)

for x in range(60, 75):
	grades_dic['C'] += grade_list.count(x)

for x in range(50, 60):
	grades_dic['D'] += grade_list.count(x)

for x in range(1, 50):
	grades_dic['F'] += grade_list.count(x)


# Bonus
# Going through the dictionary taking key and value so we can work with the exact element we want
for key, value in grades_dic.items():
    percentage = round((value / total_grades) * 100, 2)

    if value == 1:
        print(f'{key}: {value} grade {percentage}%')
    else:
        print(f'{key}: {value} grades {percentage}%')
