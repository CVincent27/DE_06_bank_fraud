import csv

def get_data_csv():
    path_csv = '../data/transactions.csv'
    with open('./data/transactions.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)        
        # print premières lignes
        i = 0
        
        for row in reader:
            i = i+1
            print(row)
            if i == 8:
                break
           

        
                
get_data_csv()

# D:\Projet_data\DE_06_Fraude_bancaire\data\transactions.csv
# data\transactions.csv