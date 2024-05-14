import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from collections import Counter

# Generate dataset
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))
X = MinMaxScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)
y_predict = np.empty(len(y_test), dtype=np.int64)

# Function to compute Euclidean distance
def dist(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Main k-NN function
def main(X_train, X_test, y_train, y_test):
    global y_predict
    k = 3

    for i, test_item in enumerate(X_test):
        # Calculate distances from the test item to all training items
        distances = [dist(train_item, test_item) for train_item in X_train]

        # Get the indices of the k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # Get the labels of the k nearest neighbors
        nearest_labels = y_train[nearest_indices]

        # Predict the label by finding the most common label (mode)
        y_predict[i] = Counter(nearest_labels).most_common(1)[0][0]

    print(y_predict)

# Run the main function
main(X_train, X_test, y_train, y_test)
