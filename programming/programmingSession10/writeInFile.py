# A programa to wirte in a txt file.

filename = input("Please enter the fileanme")
with open(filename, "w") as file_object:
    file_object.write("I like programming.\n")
    