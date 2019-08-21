import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_val(sentence):

    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    message = ""
    message = str(sentiment_dict['compound'])
    return message

def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    message = ""
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        message = "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        message = "Negative"

    else :
        message ="Neutral"

    return message
#Name of the file you want to vaderize
#filename = "400.csv"
filename = input("Input name of the file to be vadrized:")

#Name of the file after it's been adjusted
#vaderFile = 'adjusted.csv'
vaderFile = input("Input new vaderized file name:")

#number of the column (count starting from 0)
tweetNumber = 3

col1 = ['VADER_Score']
col2 = ['VADER_Val']
with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        result = sentiment_scores(str(row[tweetNumber]))
        col1.append(str(result))

        result = sentiment_val(str(row[tweetNumber]))
        col2.append(str(result))

with open(filename,  'r', encoding='utf-8') as ifile:
    with open(vaderFile, 'w', encoding='utf-8') as ofile:
        for line, new1, new2 in zip(ifile, col1, col2):
            new_line = line.rstrip('\n') + ',' + str(new1) + ',' + str(new2) + '\n'
            ofile.write(new_line)
