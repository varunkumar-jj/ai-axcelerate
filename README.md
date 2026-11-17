AIXcelerate Mood Guesser

About the project:

This project was created for Task 1 of the AIXcelerate selection process. It is a Python program that predicts whether a sentence is Happy or Sad by looking for clue words.

The project has two approaches:

1.A manually designed clue-word method using happy_words and sad_words.

2.An optional learned-score method that calculates word scores from the training examples.

The program uses only basic Python for the required mood-guessing level. No external libraries are used.

Files in this repository:

•main.py - Contains the dataset, mood-counting function, mood-guessing function, testing code, and optional bonus functions.

•README.md - Explains the project, results, AI use, and learning reflection.

•screenshot.png - Shows the program running and displaying its output.

Training data

The training data contains:

• 8 sentences labelled Happy.

• 7 sentences labelled Sad.

The count_moods() function counts the labels using a loop and two counters. For the supplied dataset, it returns:

Plain Text


(8, 7)



How the required model works

The required guess_mood(sentence) function follows these steps:

1.Converts the sentence to lowercase.

2.Replaces punctuation with spaces.

3.Splits the sentence into separate words.

4.Counts matching words in happy_words and sad_words.

5.Returns Happy if the Happy score is higher.

6.Returns Sad if the Sad score is higher or if the scores are tied.

For a tie, I chose Sad because I decided that a sentence should not be classified as Happy without positive clue-word evidence. This rule is written as a comment in the code.

Roll-number condition:

The instructions require both clue-word lists to contain exactly as many words as the last digit of the student's roll number. If the last digit is 0, each list must contain 10 words.

The current example uses three words in each list:

Python


happy_words = ["won", "surprise", "excited"]
sad_words = ["lost", "upset", "lonely"]



These lists represent the condition where the roll number ends in 3. The important rule is that both lists must contain the required number of words based on the roll-number condition.

Testing:

The program was tested using the five practice sentences provided in the instructions.

With the current example clue words, the required manual model achieved:

Plain Text


Level 2 accuracy: 80.0%



The sentence that was classified incorrectly was:

Plain Text


Today was a great day



The program returned Sad because none of the selected clue words appeared in the sentence. Both scores were therefore zero, and my tie rule selected Sad. The expected answer was Happy.

One improvement would be to choose a better set of clue words, while still obeying the roll-number word-count rule. Another improvement would be to create a better method for handling sentences that contain no clue words.

Optional bonus method:

The optional learn_scores(data) function creates a dictionary of word scores. A word receives:

• +1 when it appears in a Happy sentence.

• -1 when it appears in a Sad sentence.

The final score of a word is its Happy count minus its Sad count. The guess_mood_learned() function adds the scores of the words in a new sentence. A positive total is classified as Happy; a zero or negative total is classified as Sad, following the instructions.

With the current training data, the optional learned model achieved:

Plain Text


Bonus learned-model accuracy: 100.0%



This is a simple word-scoring method. It does not fully understand grammar, word order, negation, sarcasm, or context.

The program uses +1 internally when a word appears in a Happy sentence and -1 internally when it appears in a Sad sentence. The normal output shows the final predictions and accuracy rather than printing the complete score dictionary. This is enough for the required bonus comparison because the instructions ask for the learned model to be trained, tested, and compared with the Level 2 model.

AI declaration:

I used an AI tool while working on this project. I asked it to:

•Explain the AIXcelerate instructions in simple language.

•Explain Python concepts such as lists, tuples, functions, loops, conditions, dictionaries, string methods, and return values.

•Help me understand how to remove punctuation and ignore capital letters.

•Help me implement and test the roll-number condition for the number of clue words.

•Review the program structure and explain the output.

•Help me organise this README.

I did not use the code without review. I read the code, ran it, checked the output, and studied the reason for each part. I understand the main flow: the program stores labelled examples, cleans the input sentence, counts clue-word matches, compares the scores, and returns a mood. I can also explain the optional word-score method and its limitations.

Reflection:

The hardest part was understanding how a program can make a simple prediction using word evidence instead of understanding a sentence like a human. I also had to understand why lowercase conversion and punctuation removal are necessary for reliable word matching.

I learned how to define and call functions, use loops and counters, process strings, use lists and dictionaries, calculate accuracy, and handle words that the program has not seen before. I also learned that a word-counting method can make mistakes when meaning depends on context, such as in not good.

How to run the program:

Make sure Python is installed, open a terminal in the repository folder, and run:

Bash


python main.py



On some systems, use:

Bash


python3 main.py



The program runs without user input and prints the training counts, clue words, predictions for the practice sentences, and accuracy results.

