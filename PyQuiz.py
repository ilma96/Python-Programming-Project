'''
Name: Ilma Shaharin

'''

def new_quiz():
    user_input = []  # to collect the user's guesses in a list after each iteration to compare user guesses with correct answers
    correct_user_ans = 0    # As the questions gets iterated, the user's correct answers will increment at the same time
    num_of_questions = 0  # counter for the number of questions
    for key in quiz_questions:
        print("********************************************************************************")
        print(key)
        for a in quiz_options[num_of_questions]:
        # indexing the questions in the quiz options so that each question can have its own set of options
            print(a)
        user_choice = input("Enter your choice (A, B, C or D): ").upper()
        user_input.append(user_choice) # to append user's choices in a list
        correct_user_ans += check_correct_ans(quiz_questions.get(key), user_choice) #incrementing the correct answers by 1 so that the quiz points can be added
        num_of_questions+=1  # incrementing so that each question can have its own set of choices
    show_cumulative_score(correct_user_ans, user_input)  # to display the score after all the questions have finished their iteration

def check_correct_ans(correct_ans, user_input):
    if(correct_ans==user_input):
        print("Correct Answer!")
        return 1
# after each user input, if the if-statement is true, the correct user answers will be incremented in the previous function.
    else:
        print("Wrong Answer!")
        return 0            # the user receives a zero for a wrong answer

def show_cumulative_score(correct_ans, user_input):
    print()
    print()
    print("Results are below: ")
    print("------------------------")
    print("The correct answers are: ", end="")
    for k in quiz_questions:
        print(quiz_questions.get(k), end=" ")
    # iterating through the values of the quiz_question dictionary to display the comparison
    print()
    print()
    print("Your answers are: ", end="")
    for l in user_input:
        print(l, end=" ")
    # iterating through the user's given input to display the comparison
    print()
    print()

    final_score = int(correct_ans/len(quiz_questions)*100)
    print("Your cumulative score is: {:>15}".format(str(final_score))+"%")

def do_it_again():
    user_res = input("Would you like to try again? (type yes or no): ").lower()
    if user_res == "yes":
        return True
    # as long as the user response is "yes", the while loop will be true and the user can start the quiz again
    else:
        return False

# dictionary for the quiz questions
quiz_questions={
    "What type of Programming does Python support?" : "D",
    "Is Python compiled or interpreted language?" : "C",
    "Which of the following is true for variable names in Python?" : "A",
    "Which of the following is the truncation division operator in Python?" : "C",
    "Which of the following functions is a built-in function in python?" : "A",
    "Which of these define for packages in Python?" : "B",
    "What is the order of namespaces in which Python looks for an identifier?" : "D",
    "To add a new element to a list we use which Python command?" : "B",
    "Which of the following is a Python tuple?" : "C",
    "Which of the following is a feature of Python DocString?" : "D"
}

# quiz options represented in a 2D list for each question
quiz_options=[["A. Object-oriented programming", "B. Structured programming", "C. Functional programming", "D. All of the above"],
              ["A. Python language is both compiled and interpreted", "B. Python language is only interpreted", "C. Python language is neither compiled nor interpreted", "D. Python language is only interpreted"],
              ["A. Unlimited length", "B. Underscore and ampersand are the only two special characters allowed", "C. All private members must have leading and trailing underscores", "D. None of the above"],
              ["A. |", "B. /", "C. //", "D. %"],
              ["A. print()", "B. factorial()", "C. sqrt()", "D. sum()"],
              ["A. A number of files containing Python definitions and statements", "B. A folder of python modules", "C. A set of programs making use of Python modules", "D. A set of main modules"],
              ["A. Python first searches the built-in namespace, then the global namespace and finally the local namespace", "B. Python first searches the global namespace, then the local namespace and finally the built-in namespace", "C. Python first searches the built-in namespace, then the local namespace and finally the global namespace", "D. Python first searches the local namespace, then the global namespace and finally the built-in namespace"],
              ["A. list.addLast(47)", "B. list.append(47)", "C. list.addEnd(47)", "D. list.add(47)"],
              ["A. {0, 1, 4}", "B. {9,34}", "C. (0, 1, 4)", "D. [0,1,4]"],
              ["A. It provides a convenient way of associating documentation with Python modules, functions, classes, and methods", "B. In Python all functions should have a docstring", "C. Docstrings can be accessed by the __doc__ attribute on objects", "D. All of the above"]]

new_quiz()   # calling the function to start the quiz

'''
 if the user types yes, he/she can do the quiz again. The while loop will execute until the user types "no"
'''
while do_it_again():
    new_quiz()
print("You typed no, so, have a nice day!")
