import string

# İngilizce kelimeler
positive_words_en = {"good", "great", "happy", "love", "excellent", "amazing", "nice", "fantastic", "wonderful"}
negative_words_en = {"bad", "sad", "hate", "terrible", "awful", "poor", "angry", "horrible", "unhappy"}

# Türkçe kelimeler
positive_words_tr = {"iyi", "harika", "mutlu", "sevinç", "mükemmel", "güzel"}
negative_words_tr = {"kötü", "üzgün", "nefret", "berbat", "fena", "sinirli"}

# Tüm kelimeleri birleştir
all_positive_words = positive_words_en.union(positive_words_tr)
all_negative_words = negative_words_en.union(negative_words_tr)

def clean_word(word):
    return word.strip(string.punctuation).lower()

def analyze_sentiment(text: str):
    score = 0
    words = text.split()
    for word in words:
        clean = clean_word(word)
        if clean in all_positive_words:
            score += 1
        elif clean in all_negative_words:
            score -= 1

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment, score
