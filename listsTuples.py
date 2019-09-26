courses = ['math', 'python', 'node', 'CSS', 'compSci']
activities = ['painting', 'photography', 'needlework', 'climbing']
print(len(courses))
# print(courses[-1])  # get last item
# # Slice back and forth
# print(courses[1:])
# courses.append('art')
# print(courses[-1])
# courses.insert(3, 'archery')
# print(courses)

courses.extend(activities)
print(courses)

# remove items from list
courses.remove('node')
print(courses)
lastitem = courses.pop()
print(lastitem)
courses.sort()
nums = [3, -6, 1, 634, 6, 2, 9]
sortedNums = sorted(nums)
print(sortedNums)
sum = sum(nums)
print(sum)
