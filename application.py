import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter

with st.form(key='Twitter_form'):
    hastag = st.text_input('What do you want to search for?')
    number = st.slider('How many tweets do you want to get?', 0,500,step =20)
    output_csv = st.radio('Save a CSV file?', ['Yes', 'No'])
    file_name = st.text_input('Name the CSV file:')
    submitted = st.form_submit_button("Submit")
tweetdata = []
if submitted:

        for i, tweets in enumerate(sntwitter.TwitterHashtagScraper("hastag since:2022-10-01 until:2022-10-05").get_items()):
            if i > (number):
                break
            tweetdata.append([tweets.date, tweets.content, tweets.user.username, tweets.url])

            df = pd.DataFrame(tweetdata, columns=['date', 'tweets', "username", 'url'])
            df.to_csv(f'{file_name}.csv', index=False, encoding='utf=8')

        df.Store_csv = True

        if output_csv=='yes':
            df.Output = f'{file_name}.csv'
        st.dataframe(df)
