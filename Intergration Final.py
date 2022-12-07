# Assignment: Integration Sprint Two
# Name: Alexandra Poole
# Description: This is a sailor moon trivia game!

# This is my question function that I will use to ask my questions
# efficiently!
def question_function(question, user_answer):
    # This is my exit clause
    answer_correct = False
    # This is my while loop that makes it to where the user can't get the
    # question wrong!
    while not answer_correct:
        print(question, sep="\n")
        user_input = input("What is your answer? ")
        if user_answer != user_input:
            print("Nope! Try Again!")
        # Using bool for valid or invalid inputs
        else:
            answer_correct = True


def quiz_questions():
    # This is my intro where I say hey to the user and tell them about me!
    user_name = input("What is your name? ")
    print("Hello ", user_name, " I'm Alex", sep="~")
    print("Thank you for coming to play my trivia game", end=". \n")

    # This is me using the function I just created for each question!
    question_function("Okay first question! What is Sailor Moon's name? "
                      "\nSailor \nUsagi \nMoon \nLuna", "Usagi")
    # This is how I'm keeping points
    points = 3
    question_function("Who is Sailor Moon's love interest? "
                      "\nThe Moon \nJared \nTuxedo Mask \nNaruto",
                      "Tuxedo Mask")
    points += 3
    question_function("How old is Usagi at the beginning of the series? "
                      "\n14 \n30 \n20 \n24", "14")
    points += 3
    question_function("What is Sailor Moon's finishing move in the first "
                      "season? \nBrat Cry \nMoon Tiara Magic "
                      "\nLollipop Throw \nCat Throw", "Moon Tiara Magic")
    points += 3

    print("You have " + str(points) + " points.")

    double_or_half = input("Would you like to double or half? ")
    truth = 2
    double_question = False
    square_question = False
    if double_or_half == "yes" or double_or_half == "Yes":
        double_question = True
    if double_or_half != "yes" and double_or_half != "Yes":
        end_loop = False
        while not end_loop:
            user_input = input("Are you sure?")
            truth -= 1
            if user_input == "No":
                double_question = True
                end_loop = True
            elif user_input == "no":
                double_question = True
                end_loop = True
            else:
                if truth == 0:
                    double_question = False
                    # Because of the truth variable this will only print on
                    # the last loop!
                    print("Okay sorry, have a good day!")
                end_loop = True
    if double_question:
        print("Yay!" * 2)
        double_question = input("True or False, Usagi is Neo Queen "
                                "Serenity. ")
        if not double_question == "False" or double_question == "false":
            points = points * 2
            print("Good job! You have " + str(points) + " points now!")
        elif double_question == "false" or double_question == "False":
            points = points / 2
            print("Nope and now you have " + str(points) + " points.")
    if double_question:
        square_or_nothing = input("Now do you want to square or nothing? ")
        if square_or_nothing == "yes" or square_or_nothing == "Yes":
            square_question = True
        if square_or_nothing != "yes" and square_or_nothing != "Yes":
            end_loop = False
            while not end_loop:
                sure = input("Are you sure?")
                truth -= 1
                if sure == "No":
                    square_question = True
                    end_loop = True
                elif sure == "no":
                    square_question = True
                    end_loop = True
                else:
                    if truth == 0:
                        square_question = False
                        print("Okay sorry, have a good day!")
                    end_loop = True
        if square_question:
            square_question = input("True or False, Usagi is Neo Queen "
                                    "Serenity. ")
            if not square_question == "False" or square_question == "false":
                points = points ** 2
                print("Good job! You have " + str(points) + " points now!")
            elif square_question == "false" or square_question == "False":
                points = points // 2
                points = points % 2
                print("Nope and now you have " + str(points) + " points.")
    if points > 12:
        print("Good Job! You did Great! Above and beyond!")
    elif points == 12:
        print("Not a big risk taker are you?")
        print("Good Job Anyway!!")
    else:
        print("Pretty stinky job, but hey you took a risk!")
    for _ in range(2):
        print("Well Thanks For Playing My Quiz!")
    # I'm using this here to create and amend a high score file to keep
    # scores!
    in_file = open("high_score.txt", 'a')
    in_file.write("Name: " + user_name)
    in_file.write("\nScore: " + str(points))
    in_file.write("\n")
    in_file.close()
    # I am now reading in that file to tell the user the previous high scores!
    high_score = open("high_score.txt")
    hs = high_score.read()
    print(hs)
    print("Wow look at those high scores!")


def personality_quiz():
    # This is my intro where I say hey to the user and tell them about me!
    user_name = input("What is your name? ")
    print("Hello ", user_name, " I'm Alex", sep="~")
    print("Thank you for coming to play my personality quiz", end=". \n")

    mamoru = 0
    usagi = 0
    chibiusa = 0

    question_one = input("Which One Best Describes You? \nEarly Bird "
                         "\nNight Owl \nBoth \n")
    if question_one == "Early Bird":
        mamoru += 1
    elif question_one == "Night Owl":
        usagi += 1
    elif question_one == "Both":
        chibiusa += 1
    question_two = input("Which One Best Describes You? \nEmotional \nStoic"
                         " \nHot-Headed \n")
    if question_two == "Emotional":
        usagi += 1
    elif question_two == "Stoic":
        mamoru += 1
    elif question_two == "Hot-Headed":
        chibiusa += 1
    question_three = input("Which One Best Describes You? \nBrown Hair "
                           "\nBlonde Hair \nColored Hair \n")
    if question_three == "Brown Hair":
        mamoru += 1
    elif question_three == "Blonde Hair":
        usagi += 1
    elif question_three == "Colored Hair":
        chibiusa += 1
    question_four = input("Which One Best Describes You? \nSweet "
                          "\nIntelligent \nFunny \n")
    if question_four == "Sweet":
        chibiusa += 1
    elif question_four == "Intelligent":
        mamoru += 1
    elif question_four == "Funny":
        usagi += 1
    question_five = input("Which One Best Describes You? \nMisunderstood "
                          "\nUnderstood \n")
    if question_five == "Misunderstood":
        usagi += 1
        chibiusa += 1
    elif question_five == "Understood":
        mamoru += 1
    if usagi >= 3:
        print("Congrats! You are most like Usagi and/or Sailor Moon herself!"
              "You can be emotional at times but you are dependable when the"
              "team needs you!")
    elif chibiusa >= 3:
        print("Congrats! You are most like Chibiusa! She is the daughter of"
              "Mamoru and Usagi! You may be a bit hot-headed but at the"
              "end of the day you are a sweetheart!")
    elif mamoru >= 3:
        print("Congrats! You are most like Mamoru! He is a stoic hero"
              "who is ready to swoop in and save the day! You can be stoic"
              "but are a team player!")
    else:
        print("You are unique and don't seem to fit any of our characters"
              " today! If you would like you could take it again and"
              "adjust your answers!")


def menu():
    print("Sailor Moon Quiz Game \nSailor Moon Personality Quiz \nQuit")
    menu_choice = input("Which would you like to play? ")
    quiting = False
    option_a = ["Sailor Moon Quiz Game", "sailor moon quiz game", "quiz game",
                "Quiz Game", "1", "A", "a"]
    option_b = ["Sailor Moon Personality Quiz",
                "sailor moon personality quiz",
                "Personality Quiz", "personality quiz", "2", "B", "b"]
    while not quiting:
        if menu_choice in option_a:
            quiz_questions()
            print("Sailor Moon Quiz Game Again \nSailor Moon Personality Quiz"
                  " \nQuit")
            menu_choice = input("Which would you like to play? ")
        elif menu_choice in option_b:
            personality_quiz()
            print("Sailor Moon Quiz Game \nSailor Moon Personality Quiz Again"
                  " \nQuit")
            menu_choice = input("Which would you like to play? ")
        elif menu_choice == "Quit" or menu_choice == "quit":
            quiting = True


def main():
    menu()


main()
