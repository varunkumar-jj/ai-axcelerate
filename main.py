"""
AIXcelerate Task 1: Happy/Sad Mood Guesser

The program predicts whether a sentence is Happy or Sad.
"""

# Training dataset provided in the assignment
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),

    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]
# Example for a roll number ending in 3.
# Change these lists according to your own roll number.

happy_words = ["won", "surprise", "excited"]
sad_words = ["lost", "upset", "lonely"]
def count_moods(data):
    """
    Count how many Happy and Sad sentences are present.

    Returns:
        A tuple containing:
        (number_of_happy_sentences, number_of_sad_sentences)
    """

    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count
def words_only(text):
    """
    Convert text to lowercase and remove punctuation.

    Example:
        "I Lost my phone!"
        becomes
        ["i", "lost", "my", "phone"]
    """

    cleaned_text = ""

    for character in text.lower():
        if character.isalnum():
            cleaned_text += character
        else:
            cleaned_text += " "

    return cleaned_text.split()
def guess_mood(sentence):
    """
    Guess whether a sentence is Happy or Sad.

    The function counts matching words from happy_words
    and sad_words.
    """

    sentence_words = words_only(sentence)

    happy_score = 0
    sad_score = 0

    for word in sentence_words:

        if word in happy_words:
            happy_score += 1

        if word in sad_words:
            sad_score += 1

    if happy_score > sad_score:
        return "Happy"

    # Tie rule:
    # If both scores are equal, choose Sad.
    # This avoids calling a sentence Happy without positive evidence.
    return "Sad"
# Practice sentences given in the assignment
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]
def calculate_accuracy(data):
    """
    Test the mood guesser and calculate accuracy percentage.
    """

    correct_answers = 0

    for sentence, expected_mood in data:
        predicted_mood = guess_mood(sentence)

        print("Sentence:", sentence)
        print("Expected mood:", expected_mood)
        print("Predicted mood:", predicted_mood)
        print()

        if predicted_mood == expected_mood:
            correct_answers += 1

    accuracy = (correct_answers / len(data)) * 100

    return accuracy
def learn_scores(data):
    """
    Learn a score for every word.

    Happy sentence word: +1
    Sad sentence word: -1

    Final score:
        Happy word count - Sad word count
    """

    scores = {}

    for sentence, mood in data:
        sentence_words = words_only(sentence)

        for word in sentence_words:

            if word not in scores:
                scores[word] = 0

            if mood == "Happy":
                scores[word] += 1

            elif mood == "Sad":
                scores[word] -= 1

    return scores
# Learn word scores from the training data
learned_scores = learn_scores(train_data)


def guess_mood_learned(sentence):
    """
    Guess the mood using automatically learned word scores.
    """

    total_score = 0

    sentence_words = words_only(sentence)

    for word in sentence_words:
        # Unknown words receive a score of 0
        total_score += learned_scores.get(word, 0)

    if total_score > 0:
        return "Happy"

    # Positive score means Happy.
    # Zero or negative score means Sad.
    return "Sad"
if __name__ == "__main__":

    print("Training mood counts:")
    print(count_moods(train_data))
    print()

    print("Happy clue words:", happy_words)
    print("Sad clue words:", sad_words)
    print()

    print("Testing Level 2 guess_mood function:")
    print("------------------------------------")

    level_2_accuracy = calculate_accuracy(practice_data)

    print("Level 2 accuracy:",
          f"{level_2_accuracy:.1f}%")
    print()

    print("Testing bonus learned model:")
    print("----------------------------")

    learned_correct_answers = 0

    for sentence, expected_mood in practice_data:
        predicted_mood = guess_mood_learned(sentence)

        print("Sentence:", sentence)
        print("Expected mood:", expected_mood)
        print("Predicted mood:", predicted_mood)
        print()

        if predicted_mood == expected_mood:
            learned_correct_answers += 1

    learned_accuracy = (
        learned_correct_answers / len(practice_data)
    ) * 100

    print("Bonus learned-model accuracy:",
          f"{learned_accuracy:.1f}%")
