import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def week_counts():
    week_events = ["AFCON", "Morsi"]
    week_tweets_counts = [540, 71]
    ax.set_xlabel('Event')
    ax.set_title('Tweet Counts')
    rects = ax.bar(week_events, week_tweets_counts)
    autolabel(rects)
    plt.show()

def month_counts():
    month_events = ["Coronavirus", "Libya", "Trump & Middle East", "Best in Africa", "Handball", "Book Fair", "Nancy Ajram", "Ehab Tawfik's Father", "Sultan Kaboos", "25 January"]
    month_tweets_counts = [266, 181, 212, 131, 37, 168, 90, 51, 70, 118]
    ax.set_xlabel('Event')
    ax.set_title('Tweet Counts')
    rects = ax.bar(month_events, month_tweets_counts)
    autolabel(rects)
    plt.setp(ax.get_xticklabels(), rotation=15, horizontalalignment='right')
    plt.show()

def week_fragmentation():
    category_names = ['Irrelevant Tweets', "Relevant Tweets"]
    results = {
        'AFCON': [1.11, 98.89],
        'Morsi': [1.40, 98.6]
    }
    def survey(results, category_names):
        """
        Parameters
        ----------
        results : dict
            A mapping from question labels to a list of answers per category.
            It is assumed all lists contain the same number of entries and that
            it matches the length of *category_names*.
        category_names : list of str
            The category labels.
        """
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                ax.text(x, y, str(float(c)), ha='center', va='center',
                        color=text_color, rotation=90)
        ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        return fig, ax


    survey(results, category_names)
    plt.show()

def month_fragmentation():
    category_names = ['Irrelevant Tweets', "Relevant Tweets"]
    results = {
        "Coronavirus": [1.50, 98.50],
        "Libya": [1.66, 98.34],
        "Trump & Middle East": [18.87, 81.13],
        "Best in Africa": [15.27, 84.73],
        "Handball": [13.5, 86.5],
        "Book Fair": [10.12, 89.88],
        "Nancy Ajram": [0, 100],
        "Ehab Tawfik's Father": [7.84, 92.16],
        "Sultan Kaboos": [7.14, 92.86],
        "25 January": [12.71, 87.29]
    }
    def survey(results, category_names):
        """
        Parameters
        ----------
        results : dict
            A mapping from question labels to a list of answers per category.
            It is assumed all lists contain the same number of entries and that
            it matches the length of *category_names*.
        category_names : list of str
            The category labels.
        """
        labels = list(results.keys())
        data = np.array(list(results.values()))
        data_cum = data.cumsum(axis=1)
        category_colors = plt.get_cmap('RdYlGn')(
            np.linspace(0.15, 0.85, data.shape[1]))

        fig, ax = plt.subplots(figsize=(9.2, 5))
        ax.invert_yaxis()
        ax.xaxis.set_visible(False)
        ax.set_xlim(0, np.sum(data, axis=1).max())

        for i, (colname, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)
            xcenters = starts + widths / 2

            r, g, b, _ = color
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                ax.text(x, y, str(float(c)), ha='center', va='center',
                        color=text_color, fontsize=8)
        ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
                  loc='lower left', fontsize='small')

        return fig, ax


    survey(results, category_names)
    plt.show()

def topic_classification_dataset_class_counts():
    topics = ["Culture", "Finance", "Medical", "Politics", "Religion", "Sports", "Tech"]
    counts = [13200, 16900, 16900, 16900, 13200, 16900, 16900]
    ax.set_xlabel('Category')
    ax.set_ylabel('Number of Articles')
    rects = ax.bar(topics, counts)
    autolabel(rects)
    plt.show()

def topic_classification_dataset_source_counts():
    topics = ["Akhbarona", "Arabiya", "Khaleej"]
    counts = [46900, 18500, 45500]
    ax.set_xlabel('Source')
    ax.set_ylabel('Number of Articles')
    rects = ax.bar(topics, counts)
    autolabel(rects)
    plt.show()

def topic_classification_results():
    labels = 'Politics', 'Sports', 'Medical', 'Other'
    sizes = [41.7, 25, 8.3, 25]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

def sent_analysis_class_counts():
    labels = ["Positive", "Negative"]
    counts = [993, 958]
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Number of tweets')
    rects = ax.bar(labels, counts)
    autolabel(rects)
    plt.show()

def sent_analysis_results():
    labels = "Positive", "Negative"
    sizes = [25, 75]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()
