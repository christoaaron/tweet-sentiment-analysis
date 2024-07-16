import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Function to load tweets from a JSON file
def load_tweets(json_file):
    with open(json_file, 'r') as file:
        tweets = json.load(file)
    return tweets

# Function to determine the sentiment category based on compound score
def categorize_sentiment(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function to perform sentiment analysis on tweets
def analyze_sentiments(tweets):
    sia = SentimentIntensityAnalyzer()
    results = []

    for tweet in tweets:
        text = tweet['text']
        sentiment = sia.polarity_scores(text)
        sentiment_category = categorize_sentiment(sentiment['compound'])
        results.append({
            'text': text,
            'sentiment': sentiment,
            'category': sentiment_category
        })
    
    return results

# Function to display sentiment analysis results
def display_results(results):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for result in results:
        if result['category'] == "Positive":
            positive_count += 1
        elif result['category'] == "Negative":
            negative_count += 1
        else:
            neutral_count += 1

        print(f"Tweet: {result['text']}")
        print(f"Sentiment: {result['category']} (Scores: {result['sentiment']})\n")

    print(f"Total Positive Tweets: {positive_count}")
    print(f"Total Negative Tweets: {negative_count}")
    print(f"Total Neutral Tweets: {neutral_count}")

    # Create a pie chart
    labels = 'Positive', 'Negative', 'Neutral'
    sizes = [positive_count, negative_count, neutral_count]
    colors = ['green', 'red', 'grey']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Sentiment Analysis of Tweets about example.com')
    plt.show() 


# Main function
if __name__ == "__main__":
    json_file = 'translated_tweets.json'  # Path to your JSON file
    tweets = load_tweets(json_file)
    results = analyze_sentiments(tweets)
    display_results(results)
