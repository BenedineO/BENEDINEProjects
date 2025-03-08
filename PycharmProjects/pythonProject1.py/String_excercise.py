# Creating a multiline string of 5 sentences and applying some methods to manipulate my strings.

# Enclosing my multistring variable in triple double quotes
my_drive = """As i embark on my tech journey, i always remember that the only constant is innovation.
I am not afraid to take risks, experiment with new ideas, and push the boundaries of what's possible.
Every line of code, every project, and every failure is an opportunity to learn and grow.
I stay curious, stay hungry, sleep less and always learning. The tech industry needs my unique perspective, creativity,and passion.
So, i move ahead, dream big, and code even bigger – the future of tech is mine to create!"""

# Converting 2nd sentence into an uppercase and printing it out.
sentence = my_drive.split('\n') # splitting the sentences
sentence[1] = sentence[1].upper()  # Extracted line 1 and made it uppercase
my_drive = '\n'.join(sentence)  # Joined all sentences back again
print(my_drive)

# Extracting the 10th word from my sentences.
words = my_drive.split()
tenth_word = words[9]  # Indexing begins at 0
print(f"The 10th word is: {tenth_word}")

# Multiplying the 10th word 10 times
word_repetition = tenth_word * 10

# Printing my final output using the f-string.
print(f"My Final Output is: {word_repetition}")
