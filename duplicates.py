import pandas as pd
import codecs


data = pd.read_csv(
    'file.csv', low_memory=False
    )
df = pd.DataFrame(data)
duplicates = df.pivot_table(
    index =['column_name'], aggfunc = ['size'] # size->Nullable 
    )
pd.set_option("display.max_rows",None)
print(duplicates, file=codecs.open(
    'New_file.csv', 'w', 'utf-8')
    )


