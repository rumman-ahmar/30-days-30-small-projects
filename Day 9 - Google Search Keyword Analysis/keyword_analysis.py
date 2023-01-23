# import libraries
import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# create the trends request object
trends = TrendReq()

# keyword interest among the regions
trends.build_payload(kw_list=["Python"])
regions = trends.interest_by_region().sample(10)


# visualize the keyword interest data
regions.reset_index().plot(x="geoName", y="Python",
                           figsize=(120, 16), kind="bar")
plt.show()


# trending search keywords
trending_keywords = trends.trending_searches(pn="india")
print(trending_keywords)


# get weekly count
time_df = trends.interest_over_time()
# drop isPartial column
time_df = time_df.drop(columns=['isPartial'])
# print time_df in reverse order
print(time_df[::-1])


# visualize time_df
time_df.reset_index().plot(x="date", y="Python",
                           figsize=(120, 16), kind="line")
plt.show()


# google keywrod suggestion
suggetions = trends.suggestions(keyword="Python")
suggetions_df = pd.DataFrame(suggetions)
print(suggetions_df)
