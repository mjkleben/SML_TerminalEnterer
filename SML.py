import pyautogui
import time
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
directoryItems = os.listdir(dir_path)
# print(directoryItems)

while True:
    file = ""
    fileContent = []
    for item in directoryItems:
        print(item)
        if ".txt" in item:
            filePath = dir_path + "\\"
            file = open(filePath + item, "r")
            break

    print("File opened!")
    time.sleep(2)

    line = file.readline()
    while line:
        fileContent.append(line)
        line = file.readline()

    # print(fileContent)

    for fileLine in fileContent:
        pyautogui.typewrite(fileLine)

    file.close()

    print("-----------------------------------------------")
    input("Press Enter to start again")