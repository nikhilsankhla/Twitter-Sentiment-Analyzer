from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt

# function to calculate percentage
def percentage(part, whole):
    return 100 * float(part) / float(whole)

consumer_key = 'nzIAEXpQmkuQhxBdGKjHRhkln'
consumer_secret = 'QAB4nSQKyAQjzInlaBSNo2hAJDRENyIULb9E95RzQQt3RoAKrD'
accessToken = '1459848774679875585-LEaZovpOE8gwPmWIYtXqZXhzU1tveP'
accessTokenSecret = 'FNAcCFeLKtnPFQq2w46B2zJSgUGpPGryqDitVtZ9s95qM'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter YourKeyword Which you want to search")
noOfSearchTerm = int(input("Enter how many you want to analyze"))

tweets = tweepy.Cursor(api.search_tweets, q=searchTerm, lang="en").items(noOfSearchTerm)

positive = 0
negative = 0
neutral= 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity< 0.00:
        negative+=1
    elif analysis.sentiment.polarity == 0:
        neutral+=1
    elif analysis.sentiment.polarity> 0.00:
        positive+=1
positive = percentage(positive, noOfSearchTerm)
negative = percentage(negative, noOfSearchTerm)
neutral =  percentage(neutral,  noOfSearchTerm)

positive = format(positive, ".2f")
neutral = format(neutral,  ".2f")
negative = format(negative, ".2f")

print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerm) + "Tweets" )

if (polarity == 0):
    print("Neutral")
elif (polarity<0):
    print("Negative")
elif (polarity>0):
    print("positive")

labels = ['Positive ['+str(positive)+ '%', 'Neutral [' +str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen','gold','red']
patches , texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on "+searchTerm+' by analyzing '+str(noOfSearchTerm)+' Tweets. ')
plt.tight_layout()
plt.show()