def floatInputValidator(msg, reMsg):
    userInput=input(msg)
    while not type(userInput)==float:
        try:
            userInput=float(userInput)
        except Exception as e:
            print(f"the following error has occured {e}")
            userInput=input(reMsg)
    return userInput