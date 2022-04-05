import pytrends
import pandas as pd
from pytrends.request import TrendReq
import os



drugs = ['Avalide', 'Avapro', 'Coumadin', 'Eliquis', 'Plavix', 'Pravachol', 'Bydureon', 'Byetta', 'Farxiga', 'Glucophage',
          'Glucophage XR', 'Glucovance', 'Kombiglyze', 'Onglyza', 'Atripla', 'Azactam', 'Baraclude', 'Daklinza', 'Evotaz', 'Megace',
          'Reyataz', 'Sustiva', 'Videx', 'Videx EC', 'Zeri', 'Kenalog-10', 'Kenalog-40', 'BiCNU', 'CeeNU', 'Droxia', 'Empliciti',
          'Erbitux', 'Etopophos', 'Ixempra', 'Lysodren', 'Megace', 'Opdivo', 'Sprycel',  'Taxol', 'Vumon',
          'Yervoy', 'Abilify', 'Orencia', 'Nulojix']

drugs = ['Opdivo', 'Orencia', 'Elquis']

for drug in drugs:
    pytrends = TrendReq(hl='en-US')
    keyword = []
    keyword.append(drug)
    pytrends.build_payload(kw_list=keyword, cat=0, timeframe='today 5-y', geo='US')
    #df = pytrends.interest_over_time()
    df = pytrends.interest_by_region(resolution='REGION')
    df.to_csv(drug + '_map.csv')

df = pytrends.interest_by_region(resolution='REGION')


drug1 = pd.read_csv('Avalide.csv')
map1 = pd.read_csv('Avalide_map.csv')
drug2 = pd.read_csv('Abilify.csv')
map2 = pd.read_csv('Abilify_map.csv')
drug3 = pd.read_csv('Eliquis.csv')
map3 = pd.read_csv('Eliquis_map.csv')
drug4 = pd.read_csv('Opdivo.csv')
map4 = pd.read_csv('Opdivo_map.csv')
drug5 = pd.read_csv('Orencia.csv')
map5 = pd.read_csv('Orencia_map.csv')

drug12 = pd.merge(drug1, drug2[['date','Abilify']],on='date', how='left')
drug123 = pd.merge(drug12, drug3[['date', 'Eliquis']], on='date', how='left')
drug1234 = pd.merge(drug123, drug4[['date', 'Opdivo']], on='date', how='left')
drug12345 = pd.merge(drug1234, drug5[['date', 'Orencia']], on='date', how='left')

map12 = pd.merge(map1, map2[['geoName','Abilify']],on='geoName', how='left')
map123 = pd.merge(map12, map3[['geoName', 'Eliquis']], on='geoName', how='left')
map1234 = pd.merge(map123, map4[['geoName', 'Opdivo']], on='geoName', how='left')
map12345 = pd.merge(map1234, map5[['geoName', 'Orencia']], on='geoName', how='left')

drug12345.to_csv('comp_drugs.csv')
map12345.to_csv('comp_map.csv')
