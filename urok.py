#lesson 1
# i = 0
# while  i < 1000:
#     if i % 17 == 0:
#         print(i)
#     i += 1


# lesson 2
# lst_new = []

# i = 0
# while i < 1000:
#     if i % 17 == 0 and i % 2 == 0:
#         lst_new.append(i)
#     i += 1
# print("kol: " + str(len(lst_new)))
# print("chislo: " + str(lst_new))

# lesson 3

lst_1 = [12, 71, -33, 0, 86]
lst_2 = []
lst_3 = []

# i = 0 
# while i <= (len(lst_1)-1):
#     lst_2.append(lst_1[i] * 5)
#     i += 1

# print(lst_2)

for i in range(len(lst_1)):
    lst_3.append(lst_1[i] * 10)
    i += 1
print(lst_3)


