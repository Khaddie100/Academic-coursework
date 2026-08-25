# # numbers = [1,2,3,4,5]
# # figures = numbers

# #print(figures[1:2])

# # numbers = [1,2,3]
# # f = numbers
# # f is numbers
# # f [1] = 6
# # print(numbers)

# # def calc(num):
# #    for i in range(len(num)) :
# #      num[i] = num[i] **2


# # numbers = [1,2,3,4]
# # calc(numbers)
# # print(numbers)

# # mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
# # a=0
# # total = 0
# # while a < 3:
# #     b = 0
# #     while b < 2:
# #         total += mylist[a][b]
# #         b += 1
# #     a += 1
# # print(total)

# # n = 10
# # while n != 1:
# #     print (n,)
# #     if n % 2 == 0: # n is even
# #         n = n // 2
# #     else: # n is odd
# # #         n = n * 3 + 1
# # def add_square(numbers):
# #     last_num = numbers[-1]
# #     my_list = numbers.append(last_num ** 2)

# # my_list = [2, 3, 4]
# # add_square(my_list)
# # print(my_list)


# #babies is a dictionary that contains the names of babies as keys and their weights in kilograms as values
# babies = {
#     "Baby Joe":2.8,
#     "Baby Ella":3.0,
#     "Baby Mike":3.5,
#     "Baby Joy":3.2
# }

# #the for loop is used to iterate through the items in the babies dictionary
# #the items() method is used to get both the keys (names) and values (weights) from the dictionary
# #the loop prints the name of each baby along with their weight in kilograms using the print function
# #the output will display the names of the babies followed by their corresponding weights in kg, formatted as "Baby Name Weight kg"
# for names, weights in babies.items():
#     print(names, weights, "kg")

# my_tup = (3, 2, 1, 2)
# print(tuple(sorted(my_tup)))

# print(dict().get("no", "help!"))

# d = {'apple': 1, 'banana': 2, 'orange': 3, 'grape': 2}

# v = 2 

# for k in d:
#     if d[k] == v:
#         print(k)

# result = dict()
# for key in d:
#     val = d[key]
#     if val not in result:
#         result[val] = [key]
#     else:
#         result[val].append(key)

# my_list = [3, 2, 1]
# print(my_list.sort())

# fin = open('word.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

i = 2
def myf(s, n):

    global i

    print(s * i * n)

myf('hi-', 3)