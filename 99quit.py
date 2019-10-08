line = input("Enter a text to the screen. If you would like to exit, press 99: ")
if int(line).isdigit():      
    if((line) != 99):
        print(line)
    else:
        exit()
else:
    print(line)