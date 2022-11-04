def main():
    # Assignment: Integration Sprint Two
    # Name: Alexandra Poole
    # Description: This is a sailor moon trivia game!
    # This is my intro where I say hey to the user and tell them about me!
    user_name = input("What is your name? ")
    print("Hello", user_name, "I'm alex and this is my revamp of my first program!", sep="~")
    print("Thank you for coming to play my trivia game", end=". ")

    # This is my function for each question in the game
    def question_function(question, option1, user_answer, option2, option3, ):
        answer = 0
        user_input = 1
        # This is my while loop that makes it to where the user can't get the question wrong!
        while answer != user_input:
            print(question, option1, user_answer, option2, option3, sep="\n")
            user_input = input("What is your answer? ")
            answer = user_answer
            if answer != user_input:
                print("Nope! Try Again!")
            else:
                # This is how the program breaks out of the loop!
                break
    # This is me using the function I just created for each question!
    question_function("Okay first question! What is Sailor Moon's name?", "Sailor", "Usagi", "Moon", "Luna")
    # This is how I'm keeping points
    points = 3
    question_function("Who is Sailor Moon's love interest?", "The Moon", "Tuxedo Mask", "Jared", "Naruto")
    points += 3
    question_function("How old is Usagi at the beginning of the series?", "30", "14", "20", "24")
    points += 3
    question_function("What is Sailor Moon's finishing move in the first season?", "Brat Cry", "Moon Tiara Magic",
                      "Lolipop Throw", "Cat Throw")
    points += 3
    print("You have " + str(points) + " points.")
    double_or_half = input("Would you like to double or half? ")
    # I'm using an if statement and for loop to ask the user a question and double check they are sure!
    truth = 2
    if double_or_half == "yes" or double_or_half == "Yes":
        double = True
    if double_or_half != "yes" and double_or_half != "Yes":
        for x in range(2):
            sure = input("Are you sure?")
            truth -= 1
            if sure == "No":
                double = True
                break
            elif sure == "no":
                double = True
                break
            else:
                if truth == 0:
                    double = False
                    # Because of the truth varible this will only print on the last loop!
                    print("Okay sorry, have a good day!")
                continue
    if double:
        print("Yay!" * 2)
        double_question = input("True or False, Usagi is Neo Queen Serenity. ")
        if not double_question == "False" or double_question == "false":
            points = points * 2
            print("Good job! You have " + str(points) + " points now!")
        elif double_question == "false" or double_question == "False":
            points = points / 2
            print("Nope and now you have " + str(points) + " points.")
    if double:
        square_or_nothing = input("Now do you want to square or nothing? ")
        if square_or_nothing == "yes" or square_or_nothing == "Yes":
            square = True
        if square_or_nothing != "yes" and square_or_nothing != "Yes":
            for x in range(2):
                sure = input("Are you sure?")
                truth -= 1
                if sure == "No":
                    square = True
                    break
                elif sure == "no":
                    square = True
                    break
                else:
                    if truth == 0:
                        square = False
                        print("Okay sorry, have a good day!")
                    continue
        if square:
            square_question = input("True or False, Usagi is Neo Queen Serenity. ")
            if not square_question == "False" or square_question == "false":
                points = points ** 2
                print("Good job! You have " + str(points) + " points now!")
            elif square_question == "false" or square_question == "False":
                points = points // 2
                points = points % 2
                print("Nope and now you have " + str(points) + " points.")
    # I'm using this here to create and amend a high score file to keep scores!
    in_file = open("high_score.txt", 'a')
    in_file.write("Name: " + user_name)
    in_file.write("\nScore: " + str(points))
    in_file.write("\n")
    in_file.close()
    if points > 12:
        print("Good Job! You did Great! Above and beyond!")
    elif points == 12:
        print("Not a big risk taker are you?")
        print("Good Job Anyway!!")
    else:
        print("Pretty stinky job, but hey you took a risk!")
    print("Well Thanks For Playing My Quiz!")
    # I am now reading in that file to tell the user the previous high scores!
    high_score = open("high_score.txt")
    hs = high_score.read()
    print(hs)
    print("Wow look at those highscores!")
    print("Welp, That's all folks!")


main()
