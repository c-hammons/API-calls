import pytrends
import pandas as pd
from pytrends.request import TrendReq



drugs = ['Avalide', 'Avapro', 'Coumadin', 'Eliquis', 'Plavix', 'Pravachol', 'Bydureon', 'Byetta', 'Farxiga', 'Glucophage',
          'Glucophage XR', 'Glucovance', 'Kombiglyze', 'Onglyza', 'Atripla', 'Azactam', 'Baraclude', 'Daklinza', 'Evotaz', 'Megace',
          'Reyataz', 'Sustiva', 'Videx', 'Videx EC', 'Zeri', 'Kenalog-10', 'Kenalog-40', 'BiCNU', 'CeeNU', 'Droxia', 'Empliciti',
          'Erbitux', 'Etopophos', 'Ixempra', 'Lysodren', 'Megace', 'Opdivo', 'Sprycel',  'Taxol', 'Vumon',
          'Yervoy', 'Abilify', 'Orencia', 'Nulojix']

for drug in drugs:
    pytrends = TrendReq(hl='en-US')
    keyword = []
    keyword.append(drug)
    pytrends.build_payload(kw_list=keyword, cat=0, timeframe='today 5-y', geo='US')
    df = pytrends.interest_over_time()
    drug_info = []
    drug_info.append(df)


