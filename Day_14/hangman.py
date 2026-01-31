from faker import Faker

fake = Faker()

word = fake.word().upper()
guess_word = list()


for i in word:
    guess_letter = input("Guess a letter: ").upper()
    if guess_letter == word[i]:
        print(f"Correct! Current state: {guess_letter}")
        
