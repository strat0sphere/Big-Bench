import nltk
import random
from nltk.corpus import movie_reviews
import sys


def document_features(document):
    
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


if __name__=="__main__":
    
    # print document_features(movie_reviews.words('pos/cv957_8737.txt')) 

    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = all_words.keys()[:2000]
    
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    
    random.shuffle(documents)

    featuresets = [(document_features(d), c) for (d,c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    # print nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(5)