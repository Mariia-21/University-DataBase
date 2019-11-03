

class Students:
    def __init__(self, firstName, lastName, DOB, grant, faculty, cource):
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = DOB
        self.grant = grant
        self.faculty = faculty
        self.cource = cource


class Teachers:
    def __init__(self, firstName, lastName, DOB, grant, faculty, cource):
        self.firstName = firstName
        self.lastName = lastName
        self.DOB = DOB
        self.grant = grant
        self.faculty = faculty
        self.cource = cource


class Controller:
    def __init__(self, path):
        self.path = path

    def readDBFromFile(self):
        users = []
        for line in open(self.path):
            user = []
            for i in line.split(' '):
                user.append(i.split('=')[1])
            users.append(user)
        return users
