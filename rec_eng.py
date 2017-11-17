import pandas as pd
import numpy as np

from scipy.spatial.distance import cdist

import pickle

anclr_products = ['Keyloss', 'Paint', 'Tires', 'Windshield']


def state_region(state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }

    state = us_state_abbrev[state]

    if state in ["MA", "NY", "CT", "NJ", "NH",
                 "PA", "RI", "VT", "ME"]:
        return "NE"
    elif state in ["AK", "WY", "CA", "WA", "CO",
                   "HI", "OR", "UT", "NV", "NM",
                   "MT", "AZ", "ID"]:
        return "W"
    elif state in ["DE", "MD", "TX", "VA", "GA", "OK",
                   "NC", "LA", "TN", "FL", "KY", "AL",
                   "SC", "AR", "WV", "MS"]:
        return "S"
    elif state in ["ND", "IL", "MN", "NE", "IA", "SD",
                   "OH", "WI", "KS", "IN", "MI", "MO"]:
        return "MW"


# Data is already encoded
def read_data():
    data = pd.read_csv("formated_data.csv")
    data = data[(data['Keyloss'] != 0) |
                (data['Paint'] != 0) |
                (data['Windshield'] != 0) |
                (data['Tires'] != 0)]

    data = data.reset_index(drop=True)

    y_values = data[anclr_products]
    y_values = [data[product] for product in anclr_products]
    y_values = np.array(y_values).T
    # Delete columns with products
    X = np.array(data.drop(anclr_products, axis=1))

    return data, X, y_values


# Find users like you
def get_similar_users(test_sample):
    data, X, y_values = read_data()

    users = data.copy()
    users.drop(anclr_products, axis=1, inplace=True)

    categorical = ['Behavior', 'Location', 'Parking Space', 'Purpose']
    test_sample = pd.DataFrame(test_sample, index=[999999])
    users = users.append(test_sample)

    for category in categorical:
        users = pd.concat([users, pd.get_dummies(users[category], prefix=category)], axis=1)

    users.drop(['Age', 'Usage'], axis=1, inplace=True)
    distances = cdist(users.loc[[999999]], users.drop([999999]), 'jaccard')[0]

    num_of_similar_users = 50
    similar_users = np.argsort(distances)[:num_of_similar_users]  # 50 similar users

    recommended_products = []
    for product in anclr_products:
        if sum(data.loc[similar_users][product]) / num_of_similar_users > 0.3:  # if more than 30% of users bought
            recommended_products.append(product)

    return recommended_products


def get_recommendations(test_sample):
    # load the model from disk
    predictions = {"Keyloss": 0,
                   "Paint": 0,
                   "Tires": 0,
                   "Windshield": 0,
                   "User": 0}

    for i, y in enumerate(anclr_products):
        model = pickle.load(open('Saved_Files/' + y + '.sav', 'rb'))
        predictions[y] += model.predict_proba(np.array(list(test_sample.values())).reshape(1, -1))[0][1]

    most_probable = sorted(list(predictions.values()))[-2:]
    for key, value in predictions.items():
        if value in most_probable:
            predictions[key] = 1
        else:
            predictions[key] = 0

    similar = get_similar_users(test_sample)
    predictions["User"] = similar  # 0 until we find a similar user

    return predictions


# Extract label encoders and transform test sample
def encode_test(test_sample):
    features_to_transform = ["Behavior", "Location", "Parking Space", "Purpose"]
    for feature in features_to_transform:
        encoder = pickle.load(open('Saved_Files/' + feature + '.enc', 'rb'))
        if feature == "Parking Space" or feature == "Purpose":
            test_sample[feature] = encoder.transform(["".join(sorted(test_sample[feature].split("|")))])[0]
        else:
            test_sample[feature] = encoder.transform([test_sample[feature]])[0]


def transform_input(test_sample):
    test_sample["Location"] = state_region(test_sample["Location"])

    dic_driving = {
        1: "Passive",
        2: "Neutral",
        3: "Aggressive"
    }

    test_sample["Behavior"] = dic_driving[test_sample["Behavior"]]

    dic_parking = {
        1: "Parkinglot",
        2: "Parkinglot_r",
        3: "Garage"
    }

    test_sample["Parking Space"] = dic_parking[test_sample["Parking Space"]]

    encode_test(test_sample)

    return test_sample


def get_rec(test_sample):
    test_sample = transform_input(test_sample)
    return get_recommendations(test_sample)

#
# # Examlple with states
# samples = []
# for i in range(10):
#     samples.append({"Age": np.random.randint(16, 80),
#                   "Behavior": np.random.choice([1, 2, 3]),
#                   "Location": np.random.choice(['Maryland', 'Virginia', 'West Virginia']),
#                   "Parking Space": np.random.choice([1, 2, 3]),
#                   "Purpose": np.random.choice(["Racing", "Leisure", "Working", "Commuting", "Traveling"]),
#                   "Usage": np.random.randint(5, 30)})
#
# # Recommend 2 most probable products
# # Similar user is 0 until we find a similar user
# for sample in samples:
#     print(get_rec(sample))

# Call get_rec with such format
#test_sample = {"Age": 24, # (16 - 99)
#               "Behavior": "Aggressive", # (Passive - Neutral - Aggressive)
 #              "Location": "W", #(W, MW, NE, S)
  #             "Parking Space": "Garage|Parkinglot/R|Street", # (Garage, Parkinglot, Parkinglot/R, Street)
   #            "Purpose": "Commuting", # (Racing, Leisure, Working, Commuting, Traveling)
    #           "Usage": 15} # (1 - 30)