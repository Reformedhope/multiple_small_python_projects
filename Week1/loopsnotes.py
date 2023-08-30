age = 10
cannot_drive = True

while cannot_drive == True:
    if age == 16:
        cannot_drive = False
        print("The wait is over! You can drive")
    else:
        print("still a youngin, you cannot drive")
        age +=1


        #############


        string_pokemon = "pikachu"

        for char in string_pokemon:
            print(char)

            #itterates over everything in the string individually
        

        for number in range(6):
            print(number)
            
            
            
            
            football_team = "bears"
            for char in football_team:
                print(char)
                if char == "b":
                    continue
                if char == "a":
                    break
