import pandas as pd
import numpy as np

data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("Students who scored more than 85 in scaience")

print(df[df['Science'] > 85])