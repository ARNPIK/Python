chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","?","!",","," ","0","1","2","3","4","5","6","7","8","9"]
code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".-.-.-","..--..","-.-.--","--..--"," ","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."]

while True:
    mode = str(input("ENCRYPT(1) or DECRYPT(2) ?\n"))

    if mode == "1":
        message = str(input("Write the message you want to encrypt in capitals:\n"))
        outputMessage = ""

        for c in message:
            x = 0
            tempChar = ""
            for a in chars:
                if c == chars[x]:
                    tempChar = code[x]
                    if tempChar == " ":
                        outputMessage = outputMessage + tempChar + " "
                    else:
                        outputMessage = outputMessage + tempChar + " "
                x += 1

        print(outputMessage)

    if mode == "2":
        message = str(input("Write the message you want to decrypt:\n"))
        outputMessage = ""
        rawMessage = list(message)
        processedMessage = []
        tempString = ""

        for i in rawMessage:
            if i != " ":
                tempString += i
            if i == " ":
                processedMessage.append(tempString)
                tempString = ""

        for i in processedMessage:
            x = 0
            tempChar = ""

            for a in chars:
                if i == code[x]:
                    tempChar = chars[x]
                    outputMessage += tempChar
                x += 1

        print(outputMessage)
    print("")