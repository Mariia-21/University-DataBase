import DB


print("Выберите следующие действия:")
print("1 - Вывод всей базы на экран")
print("2 - Вывод всех студентов базы на экран")
print("3 - Вывод всех преподавателей базы на экран")
print("4 - Вывод по заданному году рождения")

users = []
menu = int(input())

users = DB.Controller('C:\\Users\\mariia.kusailo\\Project\\input.txt').readDBFromFile()

print(users)



