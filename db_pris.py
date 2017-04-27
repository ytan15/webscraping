import pandas as pd
import numpy as np
import sqlite3

reactors_pris_2016 = pd.read_csv("../yukuntan/webscraping/reactors_pris_2016.csv", encoding = "ISO-8859-1")

reactors_partial = reactors_pris_2016[['Country', 'Reactor Unit', 'Type','Net Capacity (MWe)',]].copy()
reactors_partial = reactors_partial.rename(columns={'Reactor Unit': 'Name'})

sLength = len(reactors_partial['Country'])
reactors_partial['Lat'] = pd.Series(np.zeros(sLength), index=reactors_partial.index)
reactors_partial['Long']= pd.Series(np.zeros(sLength), index=reactors_partial.index)

def into_sql(df):
    sqlite_file = 'test.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('DROP TABLE IF EXISTS testTable;')
    # THIS IS NOT WORKING "probably unsupported type"
    sql = '''
    CREATE TABLE testTable(
        'index', 'Name' TEXT, 'Long' REAL, 'Lat' REAL, 'Country' TEXT, 'Type' TEXT, 'Net Capacity (MWe)' REAL
    )
    '''
    c.execute(sql)
    df.to_sql(name='testTable',
              con=conn,
              if_exists='append',
              index=True)

    conn.close()
    return

into_sql(reactors_partial)
