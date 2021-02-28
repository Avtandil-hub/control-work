
# # # # lesson 1.5

# # # a = 'lorem ipsum dolor sit amet, consectur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore mana aliqua.'
# # # #o
# # # b = 0
# # # #probel
# # # c = 0 
# # # # bez probel
# # # d = ''
# # # #lesson 1.5
# # # for i in a:     
# # #     if i == 'o':
# # #         b += 1
# # #     elif i == ' ':
# # #         c += 1

# # # print('dlina: ' + str(len(a)))

# # # # lesson 1.5
# # # print('string o: ' + str(b))
# # # print("probel: " + str(c))

# # # # lesson 1.1
# # # print('simvol: ' + str(len(a) - c))

# # # # lesson 1.3 
# # # print(a[::-1])

# # # # lesson 1.4 
# # # print(a.replace(" ",  ""))



# # #lesson 2

# # b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# # #lesson 2.1
# # # print(type(b))
# # print('Чисел: ' + str(len(b)))
# # # lesson 2.2
# # print('chetnyi: ' + str(b[29:60][::2]))
# # # lesson 2.3
# # print('obratnyi: ' + str(b[19:50][1::2][::-1]))

# # # lesson 2.4
# # b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
# # a = [34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,b]
# # c = [67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,a]



# # # d = b[33:66]
# # # e = b[66:100]

# # # a = b[:33]
# # # d.append(e)
# # # a.append(d)

# # print('koshuu:'+ str(c))

# #lesson 3
ip = input('IP: ').split('.')
new_ip = ip[::-1]              # lesson 3.1

new_dic_ip = {}
old_dic_ip = {}
i = 1
for j in new_ip:               # lesson 3.2
    new_dic_ip[i] = j
    i += 1

    c = 1                      # lesson 3.3
    for a in ip:
        old_dic_ip[c] = a
        c += 1

print(new_dic_ip)
print(old_dic_ip)