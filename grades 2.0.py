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

# ''' Using method range(from 91 to 101) find elements from 90 to 100.
# 	Counting from 91 to 101 cuz programming languages are counting from 0
# '''
for x in range(91, 101):
# 	''' Method count() counting the same elements in the list.
# 		And then we adding this information to variable A
# 	'''

    # Taking key and value from the dictionary
	grades_dic['A'] += grade_list.count(x)

for x in range(76, 90):
	grades_dic['B'] += grade_list.count(x)

for x in range(61, 75):
	grades_dic['C'] += grade_list.count(x)

for x in range(51, 60):
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
