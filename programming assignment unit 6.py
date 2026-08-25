employees_main_list = ['Abel','Esther','Umar','Queen','Aisha','Paul','Anna','Hassan','Luke','Benjamin']
# print(0)
sub_list1 = employees_main_list[ :5]
# print(0)
sub_list2 = employees_main_list[5: ]
# print(0)
# sub_list2.append("Kristi Brown")
# print(0)
del sub_list1[1]
print(sub_list1)
new_list = sub_list1 + sub_list2
print(0)

salary_list = [50000, 60000, 55000, 70000, 150000, 48000, 62000, 80000, 75000, 100000]
print(0)
for i in range(len(salary_list)):
    percent_increase = salary_list[i] * 0.04
    salary_list[i] += percent_increase
print(0)

salary_list.sort()
print(salary_list)
top_3_salaries = salary_list[-3: ]
print(top_3_salaries)


#this is the sentence that I want to split into a list of words
#sentence is the variable here
sentence = "I went to the market to buy some fruits and vegetables for my family."

word_list = sentence.split(' ')
#the split() method is used to split the sentence into a list of words on every space and the result is stored in the variable word_list
print(word_list)
#the print function is used to display the list of words 

reversed_list = word_list[::-1]
print(reversed_list)
#the slicing [::-1] is used to reverse the order of the words in the list 
#the slicing means start from the end of the list and move backwards to the beginning
#the result is stored in the variable reversed_list, which is then printed to display the reversed list of words.