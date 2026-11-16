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
