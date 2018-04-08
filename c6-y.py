import pandas as pd
df = pd.DataFrame({'timecode' : [1419031147], 'price' : [453.3], 'volume' : [0.050]})
print(df)
pd.to_datetime(df.timecode, unit = 's')