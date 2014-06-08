# DEAR Cale,
# Great you have gotten here
# Press the button that says "run"
# Then in the menu press "Run Modude"
#DO NOT MESS WITH THE PROGRAM
#This is a change
import easygui, random, datetime
correct = 0
incorrect = 0
incorrectproblems = []
problemsuserdid = 0
RightWrongB = False
#def AddMultprintproblem(level, Operation):
 #   value1 = random.randint(0, 5)
  #  if level == "1":
   #     answer = add1level1 + add2level1
    #    answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level1) + "\n+ " + str(add2level1))
   # if level == "2":
    #    answer = add1level2 + add2level2
      #  answerusergot = easygui.enterbox(title = "Math flash", msg = "    " + str(add1level2) + "\n+" + "  " + str(add2level2))
   # if level == "3":
    #        answer = add1level3 + add2level3
    #        answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level3) + "\n+ " + str(add2level3))
     #   if level == "4":
     #       answer = add1level3 + add2level3
     #       answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level4) + "\n+ " + str(add2level4))
def Change(name, level, operation, correct, incorrect, problemsuserdid):
    timenow = datetime.datetime.now()
    things = open(name + ".txt", "a")
    things.write("On " + str(timenow) + "\n " + name +
                 " did " + operation + " level " + level + "\n They got " + str(correct) + " problems right\n and " +
                 str(incorrect) + " problems wrong" +
                 "\n the problems they got wrong were:\n")
    things.close()
    for onewrongproblem in incorrectproblems:
        things = open(name + ".txt", "a")
        things.write("\n" + onewrongproblem)
        things.close()
    things = open(name + ".txt", "a")
    things.write("\n\n")
    things.close()
    print "you got " + str(correct) + " correct problems."
    print "you got " + str(incorrect) + " incorrect problems."

    operation = chooseoperation()
    level = chooselevel()
    all = [name, level, operation]
    return all
   



#    allproblemsides = [[[add1level1, add2level1],[add1level2, add2level2], [add1level3, add2level3],[add1level4, add2level4]], [[sub1level1, sub2level1],[sub1level2, sub2level2], [sub1level3, sub2level3],[sub1level4, sub2level4]], [[mult1level1, mult2level1],[mult1level2, mult2level2], [mult1level3, mult2level3],[mult1level4, mult2level4]]]
def anothertry(no1, no2, operation, tries):

    tries = tries + 1
    easygui.msgbox(title = "Math flash", msg = "Sorry that was wrong \n try again")
    if operation == "Addition":
        answer = no1 + no2
        answerusergot = easygui.enterbox(title = "Math flash",
                                         msg = "    "+ str(no1) +
                                         "\n+ " + str(no2))

    if operation == "Subtraction":
        answer = no1 - no2
        answerusergot = easygui.enterbox(title = "Math flash",
                                         msg = "    "+ str(no1) +
                                         "\n- " + str(no2))
    if operation == "Multiplication":
        answer = no1 * no2
        answerusergot = easygui.enterbox(title = "Math flash",
                                         msg = "    "+ str(no1) +
                                         "\nX " + str(no2))
    if operation == "Division":
        answer = no1 / no2
        answerusergot = easygui.enterbox(title = "Math flash",
                                         msg = "    "+ str(no1) +
                                         "\n/ " + str(no2))
    Right = CheckAnswer(answer, answerusergot)
    if not Right:
        
        if not tries == 3:
            anothertry(no1, no2, operation, tries)
    else:
        easygui.msgbox(title = "Math flash", msg = "Great that was right, but the first time you did it it was wrong so this problem is wrong")

def AppendIncorrectProblems(allproblemsides, incorrectproblems, operation, level, first, secound):
    tries = 1
    if operation == "Addition":
        if level == "1":
            incorrectproblems.append(str(allproblemsides[0][0][0]) + " + " + str(allproblemsides[0][0][1]))
            anothertry(allproblemsides[0][0][0], allproblemsides[0][0][1], operation, tries)
        if level == "2":
            incorrectproblems.append(str(allproblemsides[0][1][0]) + " + " + str(allproblemsides[0][1][1]))
            anothertry(allproblemsides[0][1][0], allproblemsides[0][1][1], operation, tries)
        if level == "3":
            incorrectproblems.append(str(allproblemsides[0][2][0]) + " + " + str(allproblemsides[0][2][1]))
            anothertry(allproblemsides[0][2][0], allproblemsides[0][2][1], operation, tries)

        if level == "4":
            incorrectproblems.append(str(allproblemsides[0][3][0]) + " + " + str(allproblemsides[0][3][1]))
            anothertry(allproblemsides[0][3][0], allproblemsides[0][3][1], operation, tries)

    elif operation == "Subtraction":
        if level == "1":
            incorrectproblems.append(str(allproblemsides[1][0][0]) + " - " + str(allproblemsides[1][0][1]))
            anothertry(allproblemsides[1][0][0], allproblemsides[1][0][1], operation, tries)

        if level == "2":
            incorrectproblems.append(str(allproblemsides[1][1][0]) + " - " + str(allproblemsides[1][1][1]))
            anothertry(allproblemsides[1][1][0], allproblemsides[1][1][1], operation, tries)
        if level == "3":
            incorrectproblems.append(str(allproblemsides[1][2][0]) + " - " + str(allproblemsides[1][2][1]))
            anothertry(allproblemsides[1][2][0], allproblemsides[1][2][1], operation, tries)
        if level == "4":
            incorrectproblems.append(str(allproblemsides[1][3][0]) + " - " + str(allproblemsides[1][3][1]))
            anothertry(allproblemsides[1][3][0], allproblemsides[1][3][1], operation, tries)

    elif operation == "Multiplication":
        if level == "1":
            incorrectproblems.append(str(allproblemsides[2][0][0]) + " X " + str(allproblemsides[2][0][1]))
            anothertry(allproblemsides[2][0][0], allproblemsides[2][0][1], operation, tries)
        if level == "2":
            incorrectproblems.append(str(allproblemsides[2][1][0]) + " X " + str(allproblemsides[2][1][1]))
            anothertry(allproblemsides[2][1][0], allproblemsides[2][1][1], operation, tries)
        if level == "3":
            incorrectproblems.append(str(allproblemsides[2][2][0]) + " X " + str(allproblemsides[2][2][1]))
            anothertry(allproblemsides[2][2][0], allproblemsides[2][2][1], operation, tries)
        if level == "4":
            incorrectproblems.append(str(allproblemsides[2][3][0]) + " X " + str(allproblemsides[2][3][1]))
            anothertry(allproblemsides[2][3][0], allproblemsides[2][3][1], operation, tries)
            
    elif operation == "Division":
        incorrectproblems.append(str(first) + " / " + str(secound))
        anothertry(first, secound, operation, tries)

def CheckAnswer(correctanswer, useranswer):
    if str(correctanswer) == str(useranswer):
        return True
    else:
        return False

def askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems):
    first = 0
    secound = 0
    #Addition
    add1level1 = random.randint(0, 5)
    add1level2 = random.randint(2, 10)
    add1level3 = random.randint(2, 20)
    add1level4 = random.randint(2, 99)
    
    add2level1 = random.randint(0, 5)
    add2level2 = random.randint(2, 10)
    add2level3 = random.randint(2, 20)
    add2level4 = random.randint(2, 99)
    #Subtraction
    sub1level1 = random.randint(1, 10)
    sub1level2 = random.randint(5, 20)
    sub1level3 = random.randint(5, 50)
    sub1level4 = random.randint(5, 99)
    
    sub2level1 = random.randint(0, 5)
    sub2level2 = random.randint(1, 20)
    sub2level3 = random.randint(1, 50)
    sub2level4 = random.randint(1, 99)
    
    mult1level1 = random.randint(0, 5)
    mult1level2 = random.randint(0, 10)
    mult1level3 = random.randint(0, 12)
    mult1level4 = random.randint(0, 99)
    mult2level1 = random.randint(0, 5)
    mult2level2 = random.randint(0, 10)
    mult2level3 = random.randint(0, 12)
    mult2level4 = random.randint(0, 99)
     
    div1level1 = random.randint(1, 5)
    div1level2 = random.randint(1, 10)
    div1level3 = random.randint(1, 12)
    div1level4 = random.randint(1, 99)
    div2level1 = random.randint(1, 5)
    div2level2 = random.randint(1, 10)
    div2level3 = random.randint(1, 12)
    div2level4 = random.randint(1, 99)
    allproblemsides = [[[add1level1, add2level1],[add1level2, add2level2], [add1level3, add2level3],[add1level4, add2level4]], [[sub1level1, sub2level1],[sub1level2, sub2level2], [sub1level3, sub2level3],[sub1level4, sub2level4]], [[mult1level1, mult2level1],[mult1level2, mult2level2], [mult1level3, mult2level3],[mult1level4, mult2level4]], [[div1level1, div2level1],[div1level2, div2level2], [div1level3, div2level3],[div1level4, div2level4]]]

    if operation == "Addition":
        if level == "1":
            answer = add1level1 + add2level1
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level1) + "\n+ " + str(add2level1))
        if level == "2":
            answer = add1level2 + add2level2
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    " + str(add1level2) + "\n+" + "  " + str(add2level2))
        if level == "3":
            answer = add1level3 + add2level3
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level3) + "\n+ " + str(add2level3))
        if level == "4":
            answer = add1level4 + add2level4
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(add1level4) + "\n+ " + str(add2level4))
    elif operation == "Division":
        if level == "1":
            notanswer = div1level1 * div2level1
            first = notanswer
            secound = div1level1
            answer = div2level1
        if level == "2":
            notanswer = div1level2 * div2level2
            first = notanswer
            secound = div1level2
            answer = div2level2

        if level == "3":
            notanswer = div1level3 * div2level3
            first = notanswer
            secound = div1level3
            answer = div2level3
            answer = div1level3 * div2level3
        if level == "4":
            notanswer = div1level4 * div2level4
            first = notanswer
            secound = div1level4
            answer = div2level4
            answer = div1level4 * div2level4
        answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(first) + "\n/ " + str(secound))

    elif operation == "Multiplication":
        if level == "1":
            answer = mult1level1 * mult2level1
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(mult1level1) + "\nX " + str(mult2level1))
        if level == "2":
            answer = mult1level2 * mult2level2
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    " + str(mult1level2) + "\nX " + "  " + str(mult2level2))
        if level == "3":
            answer = mult1level3 * mult2level3
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(mult1level3) + "\nX " + str(mult2level3))
        if level == "4":
            answer = mult1level3 * mult2level3
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(mult1level4) + "\nX " + str(mult2level4))

    elif operation == "Subtraction":

        if level == "1":
            if sub1level1 < sub2level1:
                subchanging1 = sub2level1
                subchanging2 = sub1level1
                sub2level1 = subchanging2
                sub1level1 = subchanging1
            answer = sub1level1 - sub2level1
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(sub1level1) + "\n- " + str(sub2level1))
        if level == "2":
            if sub1level2 < sub2level2:
                subchanging1 = sub2level2
                subchanging2 = sub1level2
                sub2level2 = subchanging2
                sub1level2 = subchanging1
            answer = sub1level2 - sub2level2
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    " + str(sub1level2) + "\n-" + "  " + str(sub2level2))
        if level == "3":
            if sub1level3 < sub2level3:
                subchanging1 = sub2level3
                subchanging2 = sub1level3
                sub2level3 = subchanging2
                sub1level3 = subchanging1
            answer = sub1level3 -  sub2level3
            answerusergot = easygui.enterbox(title = "Math flash", msg = "    "+ str(sub1level3) + "\n- " + str(sub2level3))
        if level == "4":
            if sub1level4 < sub2level4:
                subchanging1 = sub2level4
                subchanging2 = sub1level4
                sub2level4 = subchanging2
                sub1level4 = subchanging1
            answer = sub1level4 - sub2level4
            answerusergot = easygui.enterbox(title = "Math flash", msg = "     "+ str(sub1level4) + "\n- " + str(sub2level4))
    RightWrongB = CheckAnswer(answer, answerusergot)
    allproblemsides = [[[add1level1, add2level1],[add1level2, add2level2], [add1level3, add2level3],[add1level4, add2level4]], [[sub1level1, sub2level1],[sub1level2, sub2level2], [sub1level3, sub2level3],[sub1level4, sub2level4]], [[mult1level1, mult2level1],[mult1level2, mult2level2], [mult1level3, mult2level3],[mult1level4, mult2level4]], [[div1level1, div2level1],[div1level2, div2level2], [div1level3, div2level3],[div1level4, div2level4]]]

    if RightWrongB:
        correct = correct + 1
        problemsuserdid = correct + incorrect
        keepgoing = easygui.buttonbox(title = "Math flash",
                                      msg = "Great that was correct \n \n You have done " +
                                      str(problemsuserdid) +
                                      " proplems\nYou got " + str(incorrect) +
                                      " problems incorrect \nYou got " + str(correct) +
                                      " problems correct",
                                      choices=('Ok', 'Quit', "Change Operation/Level"))
        if keepgoing == "Ok":
            askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems)
        elif keepgoing == "Change Operation/Level":
            all = Change(name, level, operation, correct, incorrect, problemsuserdid)
            level =  all[1]
            operation = all[2]
            name = all[0]
            correct = 0
            incorrect = 0
            problemsuserdid = 0
            incorrectproblems = []
            askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems)

        else:
            Quitting = easygui.buttonbox(title = "Math flash", msg = "Are you sure you would like to Quit", choices=('Ok', 'Return to mathflash'))
            if Quitting == 'Return to mathflash':
                operation = chooseoperation()
                level = chooselevel()
            else:
                Quit(name, level, operation, correct, incorrect, incorrectproblems)
                
    if not RightWrongB:
        incorrect = incorrect + 1
        problemsuserdid = correct + incorrect
        AppendIncorrectProblems(allproblemsides, incorrectproblems, operation, level, first, secound)
        keepgoing = easygui.buttonbox(title = "Math flash", msg = "Sorry that is wrong \n \n You have done " + str(problemsuserdid) +
                                      " proplems\nYou got " +
                                      str(incorrect) +
                                      " problems wrong \nYou got " +
                                      str(correct) + " problems right",
                                      choices=('Ok', 'Quit',
                                               "Change Operation/Level"))
        if keepgoing == "Ok":
            askingquestion(operation, level, name, correct, incorrect, problemsuserdid ,RightWrongB, incorrectproblems)
        elif keepgoing == "Change Operation/Level":
            all = Change(name, level, operation, correct, incorrect, problemsuserdid)
            level= all[1]
            operation = all[2]
            name = all[0]
            correct = 0
            incorrect = 0
            problemsuserdid = 0
            incorrectproblems = []
            askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems)

        else:
            Quitting = easygui.buttonbox(title = "Math flash", msg = "Are you sure you would like to Quit", choices=('Ok', 'Return to mathflash'))
            if Quitting == 'Return to mathflash':
                askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems)
            else:
                Quit(name, level, operation, correct, incorrect, incorrectproblems)
def Quit(name, level, operation, correct, incorrect, incorrectproblems):
    timenow = datetime.datetime.now()
    things = open(name + ".txt", "a")
    
    things.write("On " + str(timenow) + "\n " + name +
                 " did " + operation + " level " + level + "\n They got " + str(correct) + " problems right\n and " +
                 str(incorrect) + " problems wrong" +
                 "\n the problems they got wrong were:\n")
    things.close()
    for onewrongproblem in incorrectproblems:
        things = open(name + ".txt", "a")
        things.write("\n" + onewrongproblem)
        things.close()
    things = open(name + ".txt", "a")
    things.write("\n\n")
    things.close()
    print "done quitting"
    print "you got " + str(correct) + " correct problems."
    print "you got " + str (incorrect)+" incorrect problems."

    
def chooseoperation():
    Operation = easygui.buttonbox(title = "Math flash", msg = "What Operation would you like to do?", choices=('Addition', 'Subtraction', "Multiplication", "Division"))
    return Operation
    
def chooselevel():
    level = easygui.buttonbox(title = "Math flash", msg = "What level would you like to do?", choices=('1', '2', "3", "4"))
    return level

    
def askingname():
    name = easygui.buttonbox(title = "Math flash", msg = "What is your name?", choices=("Boston", "Cale", "Tamara", "Brad", "Tester"))
    return name

#Main Program start    
name = askingname()
operation = chooseoperation()
level = chooselevel()
askingquestion(operation, level, name, correct, incorrect, problemsuserdid, RightWrongB, incorrectproblems)

#Things that need to be impmented
# - User sees how many problems they have done (right, wrong, all)DONE
# - Writing to a file ---  DONE
#          includes asking name DONE
#          Wrong proplems DONE
#          how many correct problems DONE
#          how many incorrect problems DONE
#          how mang proples user got DONE
# - Finish levels DONE
# - Add division as backwards multiplcation DONE
# - Give user 3 tries to get the write answer -- then give it to them
