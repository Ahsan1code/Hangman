import random


def userwish():
    print("Enter 1 to play hangman :\nEnter 2 if you want to exit :")
    choice1=input("Enter your choice : ")
    return choice1
while True:
    choice = userwish()
    if choice=='1':
        def choose_word():
            words = []
            file_found= True
            try:
                file = open("hangmanwords.txt", "rt")
                for line in file:
                    for word in line.strip().split(","):
                        words.append(word.strip())
                file.close()
            except FileNotFoundError:
                print("file not found")
                file_found=False
            if file_found:
                if len(words)>0:
                    return words[random.randint(0, len(words)-1)]
                else:
                    print("No word exist in the file")
                    exit()
            else:
                exit()
        a=choose_word()
        # print("The word i have chose",a)
        #finiding  no of vowels in the selected word
        def novowels(selected_word):
            count=0
            for i in selected_word :
                if i in "aeiouAeiou":
                    count+=1
            return count
        turn= novowels(a)
        # print(turn)
        length_vowels=turn
        #finding nunmber of moves in the basis of vowels into the words
        moves= lambda a : len(a)*(0.5) if novowels(a)> len(a) else len(a)*1.5
        print("\n---------Let's play Hangman-------------\n")
        print("Total moves you have : ",int(moves(a)))
        #display hidden word
        def display_word(word, guess_word):
            display=""
            for letter in word :
                if letter in guess_word:
                    display+=letter
                else:
                    display +="*"
            return display
        #user guessing word
        def guessword():
            while True:
                enterword= input("Please enter your word choice: ")
                if len(enterword) !=1 or not enterword.isalpha():
                    print("invalid guess,! please enter a single word")
                else:
                    return enterword
        #playing function
        def playhangman():
            selected_word=a
            guess_letter=set()
            incorrect_guesses=0
            max_incorrect=moves(a)
            while incorrect_guesses < int(max_incorrect):
                print(display_word(selected_word, guess_letter))
                guess= guessword()
                if guess in guess_letter:
                    print("You have already guessed that : ")
                guess_letter.add(guess)
                if guess in selected_word:
                    if set(selected_word).issubset(guess_letter):
                        print(display_word(selected_word, guess_letter))
                        print("Congratulations ! You have guessed the word\nYou win")
                        print("The word was : ",a)
                    else:
                        print("correct guess")
                else:
                    print("Incorrect word")
                    incorrect_guesses+=1
            print("----------------------\n")
            print("You lose the game\nYou ran out of moves")
            print("The word was : ", a)
            print("----------------------\n")
        playhangman()
    elif choice=='2':
        print("---------Thank you:)----------")
        exit()
    else:
        print("\nPlease enter the valid choice 1 or 2 \n")