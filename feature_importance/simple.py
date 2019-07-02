# Plot the feature importances of the forest
import matplotlib.pyplot as plt
%matplotlib inline


def plot_feature_importances(importances = best_model.feature_importances_, X = X):
    
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize = (20, 6))
    plt.title("Feature importances")
    plt.bar(range(X.shape[1]), importances[indices],
           color="darkblue", align="center")
    plt.xticks(range(X.shape[1]), X.columns[indices], rotation = 90)
    plt.xlim([-1, X.shape[1]])

    plt.tight_layout()
    # plt.savefig(path + 'notebooks/5_reports/feature_importances_XGB_for_cointegration.jpg')
    plt.show()
    
plot_feature_importances()
