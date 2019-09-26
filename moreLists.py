cats = ['math', 'python', 'node', 'CSS', 'compSci']
# print(courses.index('CSS'))
# print('math' in courses)

# the start just changes when we start the index, so does not count from 0, but 1
for index, cat in enumerate(cats, start=1):
    print(index, cat)

cat_str = ' - '.join(cats)
print(cat_str)
cat_list = cat_str.split(' - ')
print(cat_list)
