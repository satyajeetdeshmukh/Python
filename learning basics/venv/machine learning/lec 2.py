import quandl
import pandas as pd
df = quandl.get('WIKI/GOOGL')

print(df.head())