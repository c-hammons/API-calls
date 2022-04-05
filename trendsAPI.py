import pytrends
import pandas as pd
from pytrends.request import TrendReq


pytrend = TrendReq(hl='en-US')
drugs = ['Avalide', 'Avapro', 'Coumadin', 'Eliquis', 'Plavix', 'Pravachol', 'Bydureon', 'Byetta', 'Farxiga/Forxiga', 'Glucophage',
          'Glucophage XR', 'Glucovance', 'Kombiglyze', 'Onglyza', 'Atripla', 'Azactam', 'Baraclude', 'Daklinza', 'Evotaz', 'Megace',
          'Reyataz', 'Sustiva', 'Videx', 'Videx EC', 'Zeri', 'Kenalog-10', 'Kenalog-40', 'BiCNU', 'CeeNU', 'Droxia/Hydrea', 'Empliciti',
          'Erbitux', 'Etopophos', 'Ixempra', 'Lysodren', 'Megace', 'Opdivo', 'Sprycel',  'Taxol', 'Vumon',
          'Yervoy', 'Abilify', 'Orencia', 'Nulojix', 'Bristol Meyers Squibb']
kw = drugs[0]
df = pd.DataFrame()
pytrend.build_payload(kw_list=['google'], cat=0, timeframe='today 5-y', geo='US')
df = pytrends.interest_over_time(kw_list=['Avalide'])
