print('hi')
# cats = ['eno', 'toki', 'socks', 'smooshie', 'fred']
# cats2 = cats
# print(cats)
# print(cats2)
# cats[3] = 'sasha'
# print(cats)
# print(cats2)  # this has been mutated

# a touple uses () not []
dogs = ('blue', 'fido', 'charles', 'teddy', 'lassie')
dogs2 = list(dogs)
dogs2[2] = 'bubba'
# print(dogs)
# print(dogs2)

# sets
courses = {'art', 'pottery', 'PE', 'Math'}
fun_courses = {'art', 'painting', 'pottery',
               'PE', 'Math', 'python', 'webdesign'}
print(courses.intersection(fun_courses))
print(sorted(courses.union(fun_courses)))
