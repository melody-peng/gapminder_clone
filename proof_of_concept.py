
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql(""" SELECT * FROM plotting;""", con=connection)
connection.close()
print(plotting_df.shape)

#先建立空白畫布
fig, ax = plt.subplots()
def update_plot(year_to_plot: int):
    ax.clear()
    subset_df = plotting_df[plotting_df["dt_year"] == year_to_plot]
    lex = subset_df["life_expectancy"].values
    gdp_pcap = subset_df["gdp_per_capita"].values
    cont = subset_df["continent"].values
    print(subset_df["continent"].unique())
    color_map = {
        "asia": "r",
        "africa": "g",
        "europe": "b",
        "americas": "c"
    }
    #建構畫布與軸物件
    for xi, yi, ci in zip(gdp_pcap, lex, cont):
        ax.scatter(xi, yi, color = color_map[ci])
    ax.set_title(f"The World in {year_to_plot}")
    ax.set_xlabel("GDP Per Capita (in USD)")    
    ax.set_ylabel("Life Expectancy")    
    ax.set_xlim(0,100000)
    ax.set_ylim(20,100)

#繪製動畫
ani = animation.FuncAnimation(fig, func=update_plot, frames=range(2000,2024), interval=10)
ani.save("animation.gif",fps=10)



