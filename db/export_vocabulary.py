from collections import Counter
import csv

def export_vocabulary(topic):
    file = open('../preprocessing/fixed/' + topic + '.txt', 'r')
    text = file.read().decode('utf-8')

    topic_word = text.replace('.', " ").split()


    word_count = Counter(topic_word)
    word_count = dict(word_count.items())

    bigrams = []
    for i in range(len(topic_word) - 1):
        bigrams.append(topic_word[i:i+2])

    str_bigrams = [' '.join(x) for x in bigrams]

    gram_count = Counter(str_bigrams)

    pair_count = {}

    for x in list(gram_count.items()):
        pair = x[0].split()

        if pair_count.has_key(pair[0]):
            if pair_count[pair[0]]['count'] < x[1]:
                pair_count[pair[0]] = {'follower': pair[1], 'count': x[1]}

        else:
            pair_count[pair[0]] = {'follower': pair[1], 'count': x[1]}

    with open('vocabulary/' + topic + '.csv', 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Word", "Follower", "Count"])

        for pair in list(pair_count.items()):
            word = pair[0].encode('utf-8')
            word = word.strip()
            if word.isalpha():
                writer.writerow([word, pair[1]["follower"].encode('utf-8'), word_count[pair[0]]])



topics = ['business', 'culture', 'society', 'sport', 'tech']

for topic in topics:
    export_vocabulary(topic)