'''
This module contains routines for doing descriptive statistics (not inferential) using pandas dataframes
'''
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import itertools

SEPAL_LENGTH = "sepal_length"
SEPAL_WIDTH = "sepal_width"
PETAL_LENGTH="petal_length"
PETAL_WIDTH="petal_width"

def print_descriptive_stats(iris):
    print(type(iris))

    print(pd.__version__)

    print(iris.head())
    print(iris.isnull().sum())

    print(iris.isnull().head())

    print(iris.species.value_counts())

    print("\nMinimums:")
    print(iris.min())
    print("\nMaximums:")
    print(iris.max())
    print("\nMeans:")
    print(iris.mean())

    print("\nRanges:")
    print("Sepal Length:", round(max(iris[SEPAL_LENGTH]) - min(iris[SEPAL_LENGTH]), 2))
    print("Sepal Width:", round(max(iris[SEPAL_WIDTH]) - min(iris[SEPAL_WIDTH]), 2))
    print("Petal Length:", round(max(iris[PETAL_LENGTH]) - min(iris[PETAL_LENGTH]), 2))
    print("Petal Width:", round(max(iris[PETAL_WIDTH]) - min(iris[PETAL_WIDTH]), 2))

    print("\nInterquartile Ranges (50% of data is in this range):")
    print("Sepal Length:", round(iris[SEPAL_LENGTH].quantile(0.75) - iris[SEPAL_LENGTH].quantile(0.25), 2))
    print("Sepal Width:", round(iris[SEPAL_WIDTH].quantile(0.75) - iris[SEPAL_WIDTH].quantile(0.25), 2))
    print("Petal Length:", round(iris[PETAL_LENGTH].quantile(0.75) - iris[PETAL_LENGTH].quantile(0.25), 2))
    print("Petal Width:", round(iris[PETAL_WIDTH].quantile(0.75) - iris[PETAL_WIDTH].quantile(0.25), 2))

def show_iris_histograms(iris, species_names, titles, column_names):

    fig, ax = plt.subplots(1+len(species_names), len(titles), figsize=(14, 10))

    # Show histograms of each column
    for column, (title, column_name) in enumerate(zip(titles, column_names)): 
        ax[0][column].hist(iris[column_name])
        ax[0][column].set_title(title)
        ax[0][column].axvline(iris[column_name].median(), color="g", label="median", linewidth=5)
        ax[0][column].axvline(iris[column_name].mean(), color="r", label="mean")
        ax[0][column].axvline(iris[column_name].quantile(0.25), color="blue", label="Q1", linestyle="dotted")
        ax[0][column].axvline(iris[column_name].quantile(0.75), color="blue", label="Q3", linestyle="dotted")
        modes = iris[column_name].mode()
        for m in modes:
            ax[0][column].axvline(m, color="y", label="mode", linestyle="--")
        ax[0][column].legend()

    for row, species_name in enumerate(species_names, start=1):
        # Show histograms of each column for each species_name (e.g. "setosa")
        for column, (title, column_name) in enumerate(zip(titles, column_names)): 
            data = iris[iris["species"] == species_name]
            ax[row][column].hist(data[column_name])
            ax[row][column].set_title(f"{species_name.capitalize()}-{title}")
            ax[row][column].axvline(data[column_name].median(), color="g", label="median", linewidth=5)
            ax[row][column].axvline(data[column_name].mean(), color="r", label="mean")
            ax[row][column].axvline(data[column_name].quantile(0.25), color="blue", label="Q1", linestyle="dotted")
            ax[row][column].axvline(data[column_name].quantile(0.75), color="blue", label="Q3", linestyle="dotted")
            modes = data[column_name].mode()
            for m in modes:
                ax[row][column].axvline(m, color="y", label="mode", linestyle="--")

            ax[row][column].legend()

    fig.tight_layout()
    plt.show()

def show_one_iris_scatter(iris, species_names, titles, column_names, main_title):
    combinations = list(itertools.combinations(zip(titles, column_names), 2))
    fig, ax = plt.subplots(2, 3, figsize=(14,8))

    for index, combination in enumerate(combinations):
        row = index // 3
        column = index % 3
        ax[row][column].set_title(f"{combination[0][0]} vs {combination[1][0]}")
        ax[row][column].scatter(iris[combination[1][1]], iris[combination[0][1]])

        ax[row][column].axvline(iris[combination[1][1]].quantile(0.25), color="r", label=f"Q1 {combination[1][0]}")
        ax[row][column].axvline(iris[combination[1][1]].quantile(0.75), color="r", label=f"Q3 {combination[1][0]}")

        ax[row][column].axhline(iris[combination[0][1]].quantile(0.25), color="g", label=f"Q1 {combination[0][0]}")
        ax[row][column].axhline(iris[combination[0][1]].quantile(0.75), color="g", label=f"Q3 {combination[0][0]}")

        ax[row][column].legend()

    fig.suptitle(main_title)
    plt.tight_layout()
    plt.show()

def show_iris_scatter_plots(iris, species_names, titles, column_names):
    # Show scatter plots between every dimension, no filtering
    show_one_iris_scatter(iris, species_names, titles, column_names, "All Data")
    for species_name in species_names:
        data = iris[iris["species"] == species_name]
        show_one_iris_scatter(data, species_names, titles, column_names, f"{species_name.capitalize()} Data")

iris = sns.load_dataset('iris')

species_names = ["setosa", "virginica", "versicolor"]
titles = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
column_names = [SEPAL_LENGTH, SEPAL_WIDTH, PETAL_LENGTH, PETAL_WIDTH]


#show_iris_histograms(iris, species_names, titles, column_names)
show_iris_scatter_plots(iris, species_names, titles, column_names)

#print_descriptive_stats(iris)