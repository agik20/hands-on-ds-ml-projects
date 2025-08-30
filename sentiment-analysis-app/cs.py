import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# download resource yang benar
nltk.download('vader_lexicon')
nltk.download('movie_reviews')

analyzer = SentimentIntensityAnalyzer()

while True:
    next_message = input('Message: ')
    scores = analyzer.polarity_scores(next_message)
    compound = scores['compound']
    if compound > 0.1:
        print('Positive Comment')
    elif compound < -0.1:
        print('Negative Comment')
    else:
        print('Neutral Comment')
