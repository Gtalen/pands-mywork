 # Plot the best fit line
     # creating the scatterplot of petal length and petal width
    fig, ax = plt.subplots(figsize = (13, 8))
    sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species', ax = ax)
    ax.plot(plen_values, pwidth_values, color='black', ax = ax [0, 0])
    plt.title('Scatterplot of Iris Petal Length and Petal Width')
    plt.savefig('Heatmap of the Iris dataset.png') # Saving the plot
    #plt.close()   # Closing the plot