import random

#create a sequence of word to choose from

WORDS=("python", "jumble","easy","difficult","answer","xelophone")

#pick one word randomly

word=random.choice(WORDS)

correct=word

jumble=""


while word:
    position=random.randrange(len(word))

    jumble +=word[position]

    word=word[:position] + word[(position +1):]


    #start the print

    print("jumble is",jumble)


    guess=input("your guess ")

    guess=guess.lower()

    while (guess !=correct) and (guess !=""):

        print("that's not it")

        guess=input("your guess ")

        guess=guess.lower

        if guess== correct:

            print("\n that's it you guessed it")

            print("thanks for playing")
