import pandas as pd
import numpy as np

from collections import Counter

import pickle

anclr_products = ['Keyloss', 'Paint', 'Tires', 'Windshield']


def get_mode(a, axis=0):
    a = np.array(a)
    scores = np.unique(np.ravel(a))       # get ALL unique values
    testshape = list(a.shape)
    testshape[axis] = 1
    oldmostfreq = np.zeros(testshape)
    oldcounts = np.zeros(testshape)

    for score in scores:
        template = (a == score)
        counts = np.expand_dims(np.sum(template, axis),axis)
        mostfrequent = np.where(counts > oldcounts, score, oldmostfreq)
        oldcounts = np.maximum(counts, oldcounts)
        oldmostfreq = mostfrequent

    return mostfrequent, oldcounts


def read_data():
    data = pd.read_csv("formated_data.csv")
    data = data.iloc[:200000]
    data = data[(data['Keyloss'] != 0) |
                (data['Paint'] != 0) |
                (data['Windshield'] != 0) |
                (data['Tires'] != 0)]

    y_values = data[anclr_products]
    y_values = [data[product] for product in anclr_products]
    y_values = np.array(y_values).T
    # Delete columns with products
    X = np.array(data.drop(anclr_products, axis=1))

    return data, X, y_values


def get_similar_users(test_sample):
    def shrink_data(data, test_sample):
        data_shrinked = data[(data['Age'] < test_sample[0] + 5) &
                             (data['Age'] > test_sample[0] - 5) &
                             (data['Behavior'] == test_sample[1]) &
                             (data['Location'] == test_sample[2]) &
                             (data['Usage'] < test_sample[-1] + 5) &
                             (data['Usage'] > test_sample[-1] - 5)]

        data_shrinked = data_shrinked[(data_shrinked['Behavior'] == test_sample[1]) &
                                      (data_shrinked['Location'] == test_sample[2])]

        return data_shrinked

    def binary_encoding(data):
        return data['Keyloss'] * 8 + data['Paint'] * 4 + data['Windshield'] * 2 + data['Tires'] * 1

    def masking(data, selectors):
        # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
        return list(d for d, s in zip(data, selectors) if s)

    data, X, y_values = read_data()

    binary = binary_encoding(data)

    c = dict(Counter(binary))

    # Pick 5 most common bundles except 0 and convert to binary
    bundles_keys = [bin(num)[2:].zfill(4) for num in sorted(c, key=c.get, reverse=True)[:5]]

    data_shrinked = shrink_data(data, test_sample)

    data_bundles = np.array(data_shrinked[anclr_products])

    relevant_bundles = [''.join(map(str, bundle)) for bundle in data_bundles
                        if ''.join(map(str, bundle)) in bundles_keys]

    top_bundle = list(get_mode(relevant_bundles, axis=0)[0][0])
    top_bundle = [int(prod) for prod in top_bundle]

    return masking(anclr_products, top_bundle)


def get_recommendations(test_sample):
    # load the model from disk
    predictions = {"Keyloss": 0,
                   "Paint": 0,
                   "Tires": 0,
                   "Windshield": 0,
                   "User": 0}

    for i, y in enumerate(anclr_products):
        model = pickle.load(open('Saved_Files/' + y + '.sav', 'rb'))
        predictions[y] += model.predict(np.array(test_sample).reshape(1, -1))[0]

    similar = get_similar_users(test_sample)
    predictions["User"] = similar

    return predictions


def encode_test(test_sample):
    features_to_transform = ["Behavior", "Location", "Parking Space", "Purpose"]
    for feature in features_to_transform:
        encoder = pickle.load(open('Saved_Files/' + feature + '.enc', 'rb'))
        if feature == "Parking Space" or feature == "Purpose":
            test_sample[feature] = encoder.transform(["".join(sorted(test_sample[feature].split("|")))])[0]
        else:
            test_sample[feature] = encoder.transform([test_sample[feature]])[0]


if __name__ == '__main__':
    test_sample = {"Age": 45,  # (16 - 99)
                   "Behavior": "Passive",  # (0 - 3)
                   "Location": "NE",  # (0 - 3)
                   "Parking Space": "Parkinglot/R|Street",  # (0 - 14)
                   "Purpose": "Commuting",  # (0 - 62)
                   "Usage": 15}  # (1 - 30)

    encode_test(test_sample)

    pred = get_recommendations(list(test_sample.values()))

    print(pred)