import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(
        df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data Points"
    )

    # Create first line of best fit
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = pd.Series(range(1880, 2051))
    y1 = res1.intercept + res1.slope * x1
    plt.plot(x1, y1, color="red", label="Best Fit Line 1")

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    res2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    x2 = pd.Series(range(2000, 2051))
    y2 = res2.intercept + res2.slope * x2
    plt.plot(x2, y2, color="green", label="Best Fit Line 2")
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
