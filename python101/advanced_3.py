#
with open("urls.txt", "r") as file:
    lines = file.readlines()

print(lines)

with open("urls_corrected.txt", "w") as file:
    for line in lines:
        line_remove_s line.replace("s","",1)
        line_remove_s_add_slash = line_remove_s[:6] + "/" + line_remove_s[:6]
        file.write(line_remove_s_add_slash)

#take data from user and put in file
line = input("Enter values: ")
line_list = line.split(",")
with open("user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")

with open("user_data.txt") as file:
    while True:
        line = input("Write a value")
        if line == "CLOSE":
            file.close()
            break
        else:
            file.write(line + "\n")


file = open("user_data_save_close", "a+")

while True:
    line = input("Write a value")
    if line == "SAVE":
        file.close()
        file = open("user_data_save_close.txt", "a+")
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
