import pandas as pd 
import numpy as np 
    
df = {'Name' : ['Amit', 'Darren', 'Cody', 'Drew', 
                'Ravi', 'Donald', 'Amy'], 
      'Score' : [50, 71, 87, 95, 63, 32, 80]} 
df = pd.DataFrame(df, columns = ['Name', 'Score']) 
  
df['Quantile_rank'] = pd.qcut(df['Score'], 4, 
                               labels = False) 
  
print(df)
