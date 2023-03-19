original_list = [',,,,,4,5,']
cleaned_list = []
for i in original_list:
    i = i.split(",")
    for j in i:
        if j.isdigit():
            cleaned_list.append(int(j))
print("--cleaned list", cleaned_list)