# importing the modules
from IPython.display import display
import pandas as pd
  
# creating a DataFrame
dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths' : [87, 91, 97, 95],
        'Science' : [83, 99, 84, 76]}
df = pd.DataFrame(dict)
  
# displaying the DataFrame
display(df)