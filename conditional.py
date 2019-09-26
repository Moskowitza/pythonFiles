language = 'Javascript'
secondLang = 'Python'
# No Switch case, just use elif
if language == 'Javascript':
    print("Javascript the best")
elif language == 'Python':
    print("Python best Language")
elif language == 'JAVA':
    print("Really, JAVA?")
else:
    print("that's ok")

user = 'Admin'
logged_in = False
# You can use the 'and' keyword to check fall through or use 'or' to check for one
if user == "Admin" or logged_in:
    print('Welcome to Admin Page')
else:
    print('Sorry, not admin')
