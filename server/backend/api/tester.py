from datetime import datetime
from datetime import timedelta
from textblob import TextBlob
import numpy as np
import random
import matplotlib.pyplot as plt


def tests():
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    count = 0
    tweet = "This is a good product"
    tweet1 = "This is a bad product"
    tweet2 = "I dont even know what to say"
    feedback = [tweet, tweet1, tweet2]
    for i in feedback:
        txt = i
        count += 1
        analysis = TextBlob(txt)
        polarity += analysis.sentiment.polarity
        if analysis.sentiment.polarity == 0.00:
            neutral += 1
        elif analysis.sentiment.polarity < 0.00:
            negative += 1
        elif analysis.sentiment.polarity > 0.00:
            positive += 1

    positive = 100*float(positive)/float(count)
    negative = 100*float(negative)/float(count)
    neutral = 100*float(neutral)/float(count)
    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')
    labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]',]
    sizes = [positive, neutral, negative]
    colors = ['yellowgreen', 'gold', 'red']
    patches, texts=plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Sentiment analysis system\nCustomer feedback chart\n Total number of feedback: '+str(count)+'')
    plt.axis('equal')
    plt.tight_layout()
    randomnum=random.randint(1, 99999)
    filepathnew='static/plots/'+str(randomnum)+'.png'
    plt.savefig(filepathnew)
    # plt.show()


# tests()