from youtube_comment_scraper_python import *
import pandas as pd
import time

url = "https://youtu.be/avz06PDqDbM"

youtube.open(url)
comments = []
for i in range(0, 25):
    result = youtube.video_comments()
    data = result['body']
    comments.extend(data)

df=pd.DataFrame(data)
print(df)
time.sleep(10)
df.to_csv("video_comments.csv")