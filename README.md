# Tweet Sentiment Analysis

**Doing sentiment analysis using Python**

A simple app to do sentiment analysis based on retrieved tweets data

## Google Colab

https://colab.research.google.com/drive/1WZO6HJLrX2cdtpAFYRFFmApO7ArEiQTL?usp=sharing
#### How to use:
1. Open the Colab link.
2. Upload your tweets data into the Colab and renamed it into **translated_tweets.json**.
3. Install the required packages.
4. Run the code.

## Features

- **Sentiment Analysis using VADER (Valence Aware Dictionary and sEntiment Reasoner)**: Detecting specific words and rate the sentiment from it.
- **Pie Chart**: Generate Pie Chart from the sentiment analysis result.
  
## Package Used

- **nltk**: **Natural Language Toolkit** Analyze text data.
- **matploblib**: To generate the pie chart.
- **numpy**: Do the mathematical operations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/christoaaron/tweet-sentiment-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tweet-sentiment-analysis
   ```
3. Install the required packages:
   ```bash
   pip install nltk matplotlib numpy
   ```

## Usage

1. Prepare the tweet data:
   - You need to make sure that the data structure is same like the example that I added into the repository
   - If your tweets data is not in English, please translate it into English. For now, the VADER lexicon only support English text.
3. Run the script:
   ```bash
   python tweet.sentiment-analysis
   ```

## Code Overview

### `load_tweets(json_file)`

Load tweets data from JSON file that is located in the directory.

### `categorize_sentiment(score)`

To determine the sentiment category based on the score that is generated for each tweets.

### `analyze_sentiments(tweets)`

Analyze the tweets using the VADER lexicon and process the score into category that is already setted before.

### `display_results(results)`

Display the sentiment analysis results and present it in Pie Chart.

## **Example**

**Results Example**

![image](https://github.com/user-attachments/assets/8bcab04e-5d00-4d21-b4d2-611fc9877522)


![image](https://github.com/user-attachments/assets/f1ed58e0-f911-49b2-bafc-b8c4a258b5dd)
