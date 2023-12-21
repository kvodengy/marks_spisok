#a = 0
#while a!="ні":
#    quote = input("Введіть рядок: ")
#    autor = input("Введіть автора: ")
#    with open ("quotes.txt", "a", encoding="utf-8") as file:
#        file.write(quote+"\n")
#        file.write("("+autor+")\n")
#    a = input("Чи хочете додати ще? ")
#    print("\n")

#with open ("quotes.txt", "r", encoding="utf-8") as file:
#    for line in file:
#        if "(" in line:
#            print(line)

class Pupil():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

best_pupils = []
sum = 0
amount = 0

with open ("spisok.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        data_pupil = Pupil(data[0], data[1], int(data[2]))
        if data_pupil.mark == 5:
            best_pupils.append(data_pupil.surname)
        sum = sum + data_pupil.mark 
        amount = amount + 1
print(best_pupils)
print(sum/amount)