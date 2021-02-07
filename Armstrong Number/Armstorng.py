while True:
    userInput=int(input("Enter a number: "))

    userInput= str(userInput)
    result, mul=0,0

    for i in userInput:
        i = int(i)
        mul= i*i*i
        result+= mul
        
    if result == int(userInput):
        print(f"{userInput} = {result} \nCorrect")
        x=str(input("Do you want to continue(Y/N)"))
        if x=="N":
            break
    else:
        print(f"{userInput} != {result} \nWrong")
        x=str(input("Do you want to continue(Y/N)"))
        if x=="N":
            break
