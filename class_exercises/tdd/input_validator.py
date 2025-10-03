import pyinputplus as pyip
name = pyip.inputStr("Please enter your name: ")
age = int(pyip.inputInt("Please enter your age: ",
       min=3,
       max=100,
       ))
