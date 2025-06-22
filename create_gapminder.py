import sqlite3
import pandas as pd

class CreateGapminderDB:
    def __init__(self): # 初始化需要建立的屬性
        # 把檔案名稱放在一個list做紀錄
        self.file_names = ["ddf--datapoints--gdp_pcap--by--country--time",
                            "ddf--datapoints--lex--by--country--time",
                            "ddf--datapoints--pop--by--country--time",
                            "ddf--entities--geo--country"]
        # 資料表名稱
        self.table_names = ["gdp_per_capita", "life_expectancy", "population", "geography"]

    def import_as_dataframe(self):
        # 載入panda 模組，建立一個空的 dictionary，準備儲存資料表名稱（table_name）對應的 DataFrame （透過read_csv函數）
        df_dict = dict() 
        for file_names, table_names in zip (self.file_names, self.table_names):
            file_path = f"data/{file_names}.csv"
            df = pd.read_csv(file_path)
            df_dict[table_names] = df  # table_names 是key
        return df_dict
    
    def create_database(self):
        connection = sqlite3.connect("data/gapminder.db")
        df_dict = self.import_as_dataframe()
        for k,v in df_dict.items():
            v.to_sql(name=k, con=connection, index=False, if_exists="replace")
        drop_view_sql = """
        DROP VIEW IF EXISTS plotting;
        """
        create_view_sql = """ 
        CREATE VIEW plotting AS
        SELECT
            geography.name AS country_name,
            geography.world_4region AS continent,
            gdp_per_capita.time AS dt_year,
            gdp_per_capita.gdp_pcap AS gdp_per_capita,
            life_expectancy.lex AS life_expectancy,
            population.pop AS population
        FROM gdp_per_capita
        JOIN geography
        ON gdp_per_capita.country = geography.country
        JOIN life_expectancy
        ON gdp_per_capita.country = life_expectancy.country AND gdp_per_capita.time = life_expectancy.time
        JOIN population
        ON gdp_per_capita.country = population.country AND gdp_per_capita.time = population.time
        WHERE gdp_per_capita.time < 2024
        """
        cur = connection.cursor()
        cur.execute(drop_view_sql)
        cur.execute(create_view_sql)
        connection.close()

create_gapminder_db = CreateGapminderDB()
create_gapminder_db.create_database()
