import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
choco_bar = webpage.content
soup = BeautifulSoup(choco_bar,'html.parser')
print(soup)
choco_rating = soup.find_all(attrs={'td': 'Rating'})
ratings = []
for rate in choco_rating:
  ratings.append(rate)
  float(ratings)
  plt.hist(ratings)
  plt.show()
  company_names = soup.select('.Company')
  companies = []
  for company in company_names:
    companies.append(company)
    d = {'Company': companies,'Ratings':ratings}
    df = pd.Dataframe.from_dict(d)
mean_vals = df.groupby('Company').Rating.mean()
ten_best = mean_ratings.nlargest(10)
print(ten_best)

cocoa_percent = soup.select('.CocoaPercent')
cocoa_list = []
for cocoa in cocoa_percent[1:]:
  percent = int(cocoa.get_text().strip('%'))
  cocoa_list.append(percent)
d['CocoaPercentage': cocoa_list]
df = pd.Dataframe.from_dict(d)
plt.scatter(df.CocoaPercentage, df.Rating)
plt.clf()
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
