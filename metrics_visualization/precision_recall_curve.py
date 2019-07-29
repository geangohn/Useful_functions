def precision_recall(true, pred):
    "Show the precision vs recall curve"
    
    # Calculate metrics across thresholds
    precision, recall, t = precision_recall_curve(true, pred)
    
    # Plot the curve
    plt.step(recall, precision, color='b', alpha=0.5,
             where='post')
    
    # Fill in the curve
    plt.fill_between(recall, precision, step='post', alpha=0.5,
                     color='b')

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.05])
    plt.xlim([0.0, 1.0])
    plt.title("Precision vs. Recall Curve"); plt.show();
