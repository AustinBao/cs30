import random

letters = ["s", "k", "b", "i", "d"]

essay = ""
target_word = "skibidi"
current_word = ""

# necessary to check current with target in the case the initial random letters SOMEHOW form skibidi
while current_word != target_word:
    random_index = random.randint(0, 4)
    random_letter = letters[random_index]
    essay += random_letter
    current_word += random_letter

    if current_word.endswith(target_word):
        break

print(essay)
