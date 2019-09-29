import matplotlib.pyplot as plt
import seaborn as sns

def plot_graphs(feature_1, feature_2, df):
    fig, axs = plt.subplots(ncols=4)
    fig.set_figwidth(30)
    fig.set_figheight(8)
    plt.suptitle(feature_1 + ' vs. ' + feature_2)

    sns.boxenplot(x=feature_1, y=feature_2, data=df, ax=axs[0])
    sns.boxplot(x=feature_1, y=feature_2, data=df, ax=axs[1])
    sns.violinplot(x=feature_1, y=feature_2, data=df, inner="points", ax=axs[2])
    sns.barplot(x=feature_1, y=feature_2, data=df, ax=axs[3])