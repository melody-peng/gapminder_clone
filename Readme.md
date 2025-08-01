# Project: 200 Countries, 200 Years, 4 Minutes

# Summary
This project, “200 Countries, 200 Years, 4 Minutes,” is a recreation of the famous data visualization by Hans Rosling: [200 Countries, 200 Years, 4 Minutes](https://www.youtube.com/watch?v=jbkSRLYSojo). I used `pandas` and `sqlite3` to build the database, used `matplotlib` for proof of concept, and finally created the finished product with `plotly.express`.

# Approach
- Install Miniconda
- Create the environment using the environment.yml file:

```bash
conda env create -f environment.yml
```
- Place the four CSV files from the `data/` folder into the `data/` directory of your working directory.
- Activate the environment and run `python create_gapminder_db.py` to generate `gapminder.db` in the `data/` folder.
- Activate the environment and run `python plot_with_px.py` to generate `gapminder_clone.html`.

