student = {'name': 'Toki', 'age': '11', 'courses': ['math', 'physicis']}
student['phone'] = '(555)CAT-MEOW'
student.update({'age': 12})
# print(student.get('phone'))
# to get a single value off a list
print(student['courses'][0])
age = student.pop('age')


# print(len(student))
# print(age)


# for key, value in student.items():
#     print(key, value)
