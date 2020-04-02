import codecademylib
import pandas as pd


ad_clicks = pd.read_csv('ad_clicks.csv')
 #Examine the first few rows of ad_clicks.
print(ad_clicks.head)

 #How many views (i.e., rows of the table) came from each utm_source?
ad_clicks.groupby('utm_source').user_id.count().reset_index()

 #Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

 #We want to know the percent of people who clicked on ads from each utm_source.Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.
clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index

 #Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.Save your results to the variable clicks_pivot.
clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()


#Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.
clicks_pivot['percent_clicked'] = click_pivot[True]/(click_pivot[True] +cclick_pivot[false])


#The column experimental_group tells us whether the user was shown Ad A or Ad B.Were approximately the same number of people shown both adds?
same_number = ad_clicks.groupby('experimental_group').user_id.count().reset_index
print('same_number')

 #Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.
greater_percent = ad_clicks.groupby('experimental_group','is_click').user_id.count().reset_index

