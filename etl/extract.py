import csv
import pandas as pd

def get_data_csv():
    path_csv = './data/transactions.csv'
    df = pd.read_csv(path_csv)
    print(df.head(2)) 

        
                
get_data_csv()

# D:\Projet_data\DE_06_Fraude_bancaire\data\transactions.csv
# data\transactions.csv