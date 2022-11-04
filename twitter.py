
import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pymongo
a = st.sidebar.radio("Navigation",["About us","Home","version"])

if a=="Home":
   st.header("TWITTER DATA SCRAPER")
   st.subheader("Greeting to All")
   st.text("Let start to scrape your data from twitter")
   with st.form("my form"):
    hastag = st.text_input('What do you want to search for?', placeholder="#spiderman")
    number=st.number_input("enter your data limit",0,500,10)
    start_date = st.date_input('enter starting date in formate:yyyy-mm-dd')
    end_date = st.date_input('enter end date in formate:yyyy-mm-dd')
    submitted = st.form_submit_button("Search")
try:
    tweetdata = []
    t=f"{hastag} since:{start_date} until:{end_date}"
    for i, tweets in enumerate(sntwitter.TwitterHashtagScraper(t).get_items()):
        if i > (number):
            break
        tweetdata.append([tweets.date, tweets.content, tweets.user.username, tweets.url,tweets.retweetedTweet])
    df = pd.DataFrame(tweetdata, columns=['date', 'tweets', "username", 'url','retweet'])
    st.dataframe(df)
    file_name = st.text_input('Name the CSV file:')
    st.download_button("Download as CSV", df.to_csv(), file_name=f'{file_name}.csv', mime='text/csv')
    g = df.to_dict("records")
    if st.button("Upload into MongoDB"):
      client = pymongo.MongoClient("mongodb://localhost:27017/")
      my_db = client["scrapped_database"]
      my_col = my_db["twitter"]
      x = my_col.insert_many(g)
      for x in my_col.find():
          st.markdown(x)
except:
       st.error("something wrong--please re-enter your value")
if a=="About us":
     st.write("1.In this application is used to scraper the twitter data by using snscraper module,")
     st.write("2.Front end of the application is build using streamlit tool,")
     st.write("3.output of the application is we get csv folder ,")
     st.write("4.If the output of the data can be stored by using mongodb in the form of dictonary")
if a=="version":
    st.write("streamlit---1.13.0")
    st.write("pymongo---4.2.0")
    st.write("pandas---1.5.0")
    st.write("snscrape---0.4.3.20220106")



