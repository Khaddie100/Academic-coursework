#original dictionary to store the key-value pairs from the sales.txt file
original_dictionary = {}

with open("sales.txt", 'r') as file:
# Read each line from the file, split it into key and value, and store it in the original dictionary
    for line in file:
        if line:
            key, value = line.split(":")        #split(:) to separate key and value
            values = value.split(",")           # split(,) to separate multiple values
            original_dictionary[key] = values   
            # store the key and list of values in the original dictionary

inverted_dictionary = {}
#inverted dictionary to store the key-value pairs in reverse order (value as key and key as value)

for key, values in original_dictionary.items():     
# iterate through the original dictionary to create the inverted dictionary
    for value in values:                            
        value = value.strip()                       
        # remove any leading or trailing whitespace from the value

        if value not in inverted_dictionary:     # Check if the value is already a key in the inverted dictionary
            inverted_dictionary[value] = []      # If not, initialize it with an empty list
        inverted_dictionary[value].append(key)      
        # Adds the original key to the list of keys associated with the value in the inverted dictionary

with open("inverted-sales.txt", "w") as file:           #write the inverted dictionary to a new file called "inverted-sales.txt"
    for key, values in inverted_dictionary.items():
        file.write(f"{key}: {', '.join(values)}\n")
        #write the formatted key and values to the file, with values joined by a comma and space

print("Inverted dictionary written to inverted-sales.txt")