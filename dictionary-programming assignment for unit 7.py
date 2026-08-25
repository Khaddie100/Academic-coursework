#this is the dictionary originally provided by the teacher
records = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

#a function to invert the dictionary is created as instructed for the assignment
def inverted_dictionary(data):

    inverted = {}
    # inverted {} is an empty dictionary created to store the inverted result

    for student, courses in data.items():
        # the above loop iterates through the original dictionary

        for course in courses:
            # this loop iterates through the values 'courses'

            if course not in inverted:
                # this checks if the course already exists in the new dictionary
                inverted[course] = []

            inverted[course].append(student)
            # this adds the student to the list of that course

    return inverted


# calling the function
result = inverted_dictionary(records)

# displays the content of both the original and inverted dictionaries
print("Original Dictionary:")
print(records)

print("\nInverted Dictionary:")
print("{")

#this for loop iterates through the inverted dictionary and returns tuples containing the key and value.
for course, students in result.items():
    print(f" '{course}': {students},")
    #f-string prints the course and the list of students in the required format
print("}")