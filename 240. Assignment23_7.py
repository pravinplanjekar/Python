import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
'Name': ['Amit', 'Sagar', 'Pooja'],
'Math': [85, 90, 78],
'Science': [92, 88, 80],
'English': [75, 85, 82]
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science'] + df['English']

plt.bar(df['Name'], df['Total'])
plt.xlabel("Students name")
plt.ylabel("Total marks")
plt.title("Bar plot")
plt.show()