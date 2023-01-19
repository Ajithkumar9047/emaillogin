import streamlit as st
import pandas as pd
import en_core_web_sm
nlp = en_core_web_sm.load()
path = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for i in range(len(path)):
            df = (path[0])
            df2=path[1]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('stopwords')
from pyresparser import ResumeParser
def main():

    data = ResumeParser(df).get_extracted_data()
    st.write(data['skills'])
    data2 = ResumeParser(df2).get_extracted_data()
    st.write(data2['skills'])
    content = [ data['skills'],data2['skills']]
    vectorizer = CountVectorizer(analyzer=lambda x: x)
    result = vectorizer.fit_transform(content)
    st.write("skillset:", cosine_similarity(result)[1][0] * 100, "%")
if st.button('extract'):
    main()



