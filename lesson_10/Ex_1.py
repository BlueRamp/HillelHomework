some_txt_file = open("newFile.txt", "w")
while True:
    text = input("Input some string (To exit press Enter): ")
    if text != "":
        some_txt_file.write(text+"\n")
    else:
        break
some_txt_file.close()
