#lesson 1

lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dict = {}
for i in range(len(lst)):
    dict [i] = lst [i]
print(dict)


#lesson 2
import  random
number = random.randint(0,20)
i = 0
while i <= 4:
   i = i + 1
   answer = input(" Угадай число :")
   if answer == "" or answer == " exit ":
      print(" Выход из прогрпммы :")
      break 

   if not answer.isdigit():
      print(" Ввидите правильный число:")
      continue


   answer = int(answer)

   if answer == number:
      print('Класс! Вы угадали')
      break
   

   elif answer < number:
      print(" Слишком мало:")
   else:  
      print(" Слишком много:")
print(" Ход закончили :")

#lesson 3
a = input('Vvedite slovo: ')

if len(a) % 2 == 0 or len(a) < 5:
    print('error!')
elif len(a) >= 5:
    i = 5
    j = 1
    while True:
        if len(a) == i:
            print(a[j:-j])
            break
        i += 2
        j += 1


# lesson 4

a = 'Aidana'
b = 'Adilet'
c = ''

i = 0
while i <= (len(a) - 1):
    c += a[i]    
    c += b[i]    
    i += 1
print(c)