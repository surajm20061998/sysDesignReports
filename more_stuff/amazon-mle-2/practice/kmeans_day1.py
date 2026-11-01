"""Day 1 teaching reference: Lloyd's K-means with supplied initial centers."""
import numpy as np


def assign_labels(X, centroids):
    # Each column contains squared distances to one centroid.
    distances = np.empty((len(X), len(centroids)), dtype=float)
    for j, center in enumerate(centroids):
        distances[:, j] = np.sum((X - center) ** 2, axis=1)
    # argmin picks the first index when distances tie.
    return np.argmin(distances, axis=1)


def kmeans(X, initial_centroids, max_iter=100, tol=1e-4):
    X = np.asarray(X, dtype=float)
    centroids = np.array(initial_centroids, dtype=float, copy=True)

    if X.ndim != 2 or X.shape[0] == 0 or X.shape[1] == 0:
        raise ValueError("X must have shape [N, D], with N and D positive")
    if centroids.ndim != 2 or centroids.shape[1] != X.shape[1]:
        raise ValueError("centroids must have shape [K, D]")
    if not 1 <= len(centroids) <= len(X):
        raise ValueError("require 1 <= K <= N")
    if not np.isfinite(X).all() or not np.isfinite(centroids).all():
        raise ValueError("inputs must be finite")
    if not isinstance(max_iter, (int, np.integer)) or max_iter < 1:
        raise ValueError("max_iter must be a positive integer")
    if not np.isfinite(tol) or tol < 0:
        raise ValueError("tol must be finite and nonnegative")

    for _ in range(max_iter):
        labels = assign_labels(X, centroids)
        new_centroids = centroids.copy()

        for j in range(len(centroids)):
            members = X[labels == j]
            if len(members) > 0:
                new_centroids[j] = members.mean(axis=0)
            # Empty cluster: keep its previous centroid.

        shifts = np.linalg.norm(new_centroids - centroids, axis=1)
        centroids = new_centroids
        if shifts.max() <= tol:
            break

    # Centers moved after labels were computed; synchronize returned labels.
    labels = assign_labels(X, centroids)
    return centroids, labels


def _self_check():
    X = np.array([[0., 0.], [0., 2.], [8., 8.], [8., 10.]])
    initial = np.array([[0., 0.], [8., 8.]])
    centers, labels = kmeans(X, initial)
    np.testing.assert_allclose(centers, [[0, 1], [8, 9]])
    np.testing.assert_array_equal(labels, [0, 0, 1, 1])
    np.testing.assert_array_equal(initial, [[0, 0], [8, 8]])

    centers, labels = kmeans(X, [[0., 0.]])
    np.testing.assert_allclose(centers, [[4, 5]])
    np.testing.assert_array_equal(labels, [0, 0, 0, 0])

    centers, labels = kmeans([[1.], [1.], [1.]], [[1.], [100.]])
    np.testing.assert_allclose(centers, [[1], [100]])
    np.testing.assert_array_equal(labels, [0, 0, 0])

    # max_iter=1: old assignments differ from final nearest-center labels.
    centers, labels = kmeans([[0.], [2.], [3.], [10.]], [[0.], [3.]], max_iter=1)
    np.testing.assert_allclose(centers, [[0], [5]])
    np.testing.assert_array_equal(labels, [0, 0, 1, 1])

    centers, labels = kmeans([[0.], [2.]], [[0.], [2.]])
    np.testing.assert_allclose(centers, [[0], [2]])
    np.testing.assert_array_equal(labels, [0, 1])

    # Tie at x=1 is assigned to the smaller centroid index.
    np.testing.assert_array_equal(assign_labels(np.array([[1.]]), np.array([[0.], [2.]])), [0])
    print("Passed: separated clusters, K=1, duplicates/empty cluster, iteration limit, fixed point, ties, input preservation.")


if __name__ == "__main__":
    _self_check()
