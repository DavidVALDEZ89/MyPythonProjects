import requests
import tweepy
import pandas as pd
import seaborn as sns
import nltk
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from keys import *
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer



# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('vader_lexicon')

# import re

client = tweepy.Client(bearer_token=TOKEN,
                       return_type=requests.Response
                       )

# Replace with your own search query
query = 'from:BrusselsTimes -is:retweet'

tweets = client.search_recent_tweets(query = query,
                                     tweet_fields = ['author_id', 'created_at',"public_metrics"], 
                                     max_results = 100)

tweet_dict = tweets.json()
tweet_data = tweet_dict['data']

# print (tweet_dict)
# print (tweet_data)

df = pd.json_normalize(tweet_data)



df['text'] = df['text'].astype(str).str.lower()

regexp = RegexpTokenizer('\w+')

df['text_token'] = df['text'].apply(regexp.tokenize)

stopwords = nltk.corpus.stopwords.words("english")

my_stopwords = ['https', "belgian", "belgium",  "july" , 'dverloes', 'julienpain', 'davanac']
stopwords.extend(my_stopwords)

df['text_token'] = df['text_token'].apply(
    lambda x: [item for item in x if item not in stopwords])

df['text_string'] = df['text_token'].apply(
    lambda x: ' '.join([item for item in x if len(item) > 2]))

all_words = ' '.join([word for word in df['text_string']])

tokenized_words = nltk.tokenize.word_tokenize(all_words)

fdist = FreqDist(tokenized_words)

df['text_string_fdist'] = df['text_token'].apply(
    lambda x: ' '.join([item for item in x if fdist[item] >= 1]))

wordnet_lem = WordNetLemmatizer()

df['text_string_lem'] = df['text_string_fdist'].apply(wordnet_lem.lemmatize)

all_words_lem = ' '.join([word for word in df['text_string_lem']])

wordcloud = WordCloud(width=1200,
                      height=800,
                      random_state=2,
                      max_font_size=100).generate(all_words_lem)

plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
plt.savefig('./test.png')


words = nltk.word_tokenize(all_words_lem)
fd = FreqDist(words)


top_10 = fd.most_common(15)

fdist = pd.Series(dict(top_10))

sns.set_theme(style="ticks")

sns.barplot(y=fdist.index, x=fdist.values, color='blue')

fig = px.bar(y=fdist.index, x=fdist.values)

fig.update_layout(barmode='stack', yaxis={'categoryorder': 'total ascending'})

fig.show()







df.to_csv ("myTweeterData.csv")

