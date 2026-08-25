try:
    with open("word.txt") as fin:
        lines = fin.readlines()
    for line in lines:
        word = line.strip()
        #li
        print(word)
except FileNotFoundError:
    print("The file word.txt was not found.")
# else:
#     with open("word.txt") as fin:
#         lines = fin.readlines()
#         print(lines)
#     for line in lines:
#         word = line.strip()
#         print(word)
#     fin.close()

        