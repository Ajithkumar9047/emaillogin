import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import datetime as dt
import pymongo

a = st.sidebar.radio("Navigation",["Home","About us","version"])
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
if a=="Home":
   st.header("TWITTER DATA SCRAPER",)
   st.subheader("Greeting to All")
   st.text("Let start to scrape your data from twitter")
   hastag = st.text_input('What do you want to search for?')
   number=st.number_input("enter your data limit",0,500)
   start_date = st.date_input('enter starting date in formate:yyyy-mm-dd')
   end_date = st.date_input('enter end date in formate:yyyy-mm-dd')
   file_name = st.text_input('Name the CSV file:')
   submitted = st.button("Search")
   download = st.button("download as csv")
   tweetdata = []
   t=f"{hastag} since:{start_date} until:{end_date}"
   if submitted:

    for i, tweets in enumerate(sntwitter.TwitterHashtagScraper(t).get_items()):
        if i > (number):
            break
        tweetdata.append([tweets.date, tweets.content, tweets.user.username, tweets.url,tweets.retweetedTweet])
    df = pd.DataFrame(tweetdata, columns=['date', 'tweets', "username", 'url','retweet'])
    df.to_csv(f'{file_name}.csv', index=False, encoding='utf=8')
    g = df.to_dict("records")
     client = pymongo.MongoClient("mongodb+srv://ajithkumaraji9047:<password>@cluster0.f8nzez2.mongodb.net/?retryWrites=true&w=majority")
    mydb = client["mydatabase"]
    mycol = mydb["twitterscraper"]

    x = mycol.insert_many(g)

    for x in mycol.find():
        st.markdown(x)

    df.Store_csv = True
    if download:
        df.Output = f'{file_name}.csv'



