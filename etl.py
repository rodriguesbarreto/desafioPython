import pandas as pd 
companies = pd.read_csv("companies.tsv",delimiter='\t')
deals = pd.read_csv("deals.tsv",delimiter='\t')
sectors = pd.read_csv("sectors.tsv",delimiter='\t')
contacts = pd.read_csv("contacts.tsv",delimiter='\t')
print(deals.dealsDateCreated)