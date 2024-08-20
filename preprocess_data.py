import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(filepath):

    df = pd.read_csv(filepath)


    # selecting all the relevant features from dataset
    features = df[['acousticness', 'danceability', 'energy', 
                   'instrumentalness', 'liveness', 'loudness', 
                   'speechiness', 'tempo', 'valence']]

    # normalizing features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    return scaled_features, df

if __name__ == "__main__":
    filepath = 'data/data.csv'
    scaled_features, df = load_and_preprocess(filepath)
