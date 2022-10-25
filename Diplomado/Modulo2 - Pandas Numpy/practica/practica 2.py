"""
 0   country                              3081 non-null   object 
 1   iso_code                             2833 non-null   object 
 2   date                                 3081 non-null   object 
 3   total_vaccinations                   1980 non-null   float64
 4   people_vaccinated                    1643 non-null   float64
 5   people_fully_vaccinated              1016 non-null   float64
 6   daily_vaccinations_raw               1642 non-null   float64
 7   daily_vaccinations                   2960 non-null   float64
 8   total_vaccinations_per_hundred       1980 non-null   float64
 9   people_vaccinated_per_hundred        1643 non-null   float64
 10  people_fully_vaccinated_per_hundred  1016 non-null   float64
 11  daily_vaccinations_per_million       2960 non-null   float64
 12  vaccines                             3081 non-null   object 
 13  source_name                          3081 non-null   object 
 14  source_website                       3081 non-null   object
""" 
import pandas as pd

df = pd.read_csv (r'country_vaccinations.csv')
df.head()
showData = pd.DataFrame(df)
#print(showData)
#print(df.to_string())
#print(df) 