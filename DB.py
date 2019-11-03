
class Person:
    def __init__(self, firstName, lastName, DOB, grant, faculty, course):
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = DOB
        self.grant = grant
        self.faculty = faculty
        self.course = course


class Students(Person):
    pass


class Teachers(Person):
    pass


class Controller:
    def __init__(self, path):
        self.path = path

    def readDBFromFile(self):   # function for reading all data from file
        users = []
        for line in open(self.path):
            user = []
            for i in line.split(' '):
                user.append(i.split('=')[1])
            users.append(user)
        return users

    def printDB(dbName):   # function for printing all data from file
        firstName = 1
        lastName = 2
        birthday = 3
        money = 4
        faculty = 5
        age = 6
        for user in dbName:
            print('%-12s %-12s %-14s %-12s %-10s %-5s'
                  % (user[firstName], user[lastName], user[birthday], user[money], user[faculty], user[age]))

    def createLists(users):  # function for creating two lists (students, teachers)
        id = 0               # id in file: 1 - students, 2 - teachers
        firstName = 1
        lastName = 2
        birthday = 3
        money = 4
        faculty = 5
        age = 6
        studentsList = []
        teachersList = []
        for user in users:
            if user[id] == '2':
                line = Students(user[firstName], user[lastName], user[birthday], user[money], user[faculty], user[age])
                studentsList.append(line)   # list of all students in database
            else:
                line = Teachers(user[firstName], user[lastName], user[birthday], user[money], user[faculty], user[age])
                teachersList.append(line)   # list of all teachers in database
        return studentsList, teachersList   # function returned two lists

    def printingList(listName):  # function for printing lists
        for user in listName:
            print('%-12s %-12s %-14s %-12s %-10s %-5s'
                  % (user.firstName, user.lastName, user.DOB, user.grant, user.faculty, user.course))

    def foundYear(year, listName):  # function for search record in database for the entered year
        for user in listName:
            if user.DOB[-4:] == year:
                print('%-12s %-12s %-14s %-12s %-10s %-5s'
                      % (user.firstName, user.lastName, user.DOB, user.grant, user.faculty, user.course))