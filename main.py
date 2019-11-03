import DB

i = 1
users = []
studentsList = []
teachersList = []

while i == 1:
    print("Выберите следующие действия:\n")
    print("1 - Вывод всей базы на экран")
    print("2 - Вывод всех студентов базы на экран")
    print("3 - Вывод всех преподавателей базы на экран")
    print("4 - Вывод по заданному году рождения")
    print("5 - Выход с программы")
    try:
        menu = int(input())
        users = DB.Controller('C:\\Users\\mariia.kusailo\\Project\\input.txt').readDBFromFile()  # reading all data from file
        studentsList, teachersList = DB.Controller.createLists(users)  # two lists(students, teachers)

        if menu == 1:
            DB.Controller.printDB(users)  # printing all data from file

        elif menu == 2:
            print("Список студентов:")
            DB.Controller.printingList(studentsList)   # printing all students from file

        elif menu == 3:
            print("Список преподавателей:")
            DB.Controller.printingList(teachersList)   # printing all teachers from file

        elif menu == 4:
            year = input("Введите год рождения для поиска ")  # search records in the database for the entered year
            print("Студенты ", year, " года рождения:\n")
            DB.Controller.foundYear(year, studentsList)
            print("Преподаватели ", year, " года рождения:\n")
            DB.Controller.foundYear(year, teachersList)

        elif menu == 5:
            quit()             # exit from programme

        else:
            print("Вы ввели неверное значение!")

    except ValueError:
        print("Что-то пошло не так :( ")