# giving a list of countries that are keys and their capitals are values:
country_capital = {"Lithuania": "Vilnius", "Denmark": "Copenhagen", "Albania": "Tirana", "Andorra": "Andorra la Vella",
                   "Austria": "Vienna", "Belarus": "Minsk", "Belgium": "Brussels", "Bosnia and Herzegovina": "Sarajevo",
                   "Bulgaria": "Sofia", "Croatia": "Zagreb", "Cyprus": "Nicosia", "Czech Republic": "Prague",
                   "Estonia": "Tallinn", "Finland": "Helsinki", "France": "Paris", "Germany": "Berlin",
                   "Gibraltar": "Gibraltar", "Greece": "Athens", "Hungary": "Budapest", "Iceland": "Reykjavik",
                   "Ireland": "Dublin", "Italy": "Rome", "Latvia": "Riga", "Luxembourg": "Luxembourg",
                   "Netherlands": "Amsterdam", "Norway": "Oslo", "Spain": "Madrid", "Sweden": "Stockholm"}


def main():
    end_of_quiz = False
    correct = 0     # correct and incorrect answers starts with counting from 0
    incorrect = 0
    while not end_of_quiz and len(country_capital) > 0:     # while quiz is not false and list is not empty, do:
        country, capital = country_capital.popitem()        # picking a random country and removing it from a list
        print("What's the capital of", country, "? If you want to end quiz, say 'quit'")
        users_guess = input("Enter the answer: ")
        if users_guess == capital:                          # if user is right, he gets 1 point for correct answers
            correct += 1
        elif users_guess == "quit":                         # if user says he wants to quit, quiz is ended
            end_of_quiz = True
        else:
            incorrect += 1                                  # if user is incorrect, he gets 1 point for incorrect
    else:
        print("Correct answers: " + str(correct))
        print("Incorrect answers: " + str(incorrect))
    if len(country_capital) == 0:                           # when list is empty, printing out that quiz is done
        print("Quiz is done.")


main()
