import os

import pandas as pd
import csv
import streamlit as st
import os
def value():
  values={"products":[product],"kilogram":[kg],"total":[total]}

  df=pd.DataFrame(values,columns=["products","kilogram","total"])
  df.set_index("products",inplace=True)
  st.dataframe(df)
  button = st.download_button("create new folder", df.to_csv(),file_name=f"{file_name}.csv",mime='text/csv')

  if button1:

   with open(f"C:/Users/Star World/Downloads/abi.csv ", 'a',newline='') as file:
     h=([product,kg,total])
     writer = csv.writer(file)
     writer.writerow(h)
   file.close()
a = st.sidebar.radio("Navigation",["working rules","Home","about us","version"])
if a=="working rules":
     st.header("WELCOME TO SETHURAM TRADERS")
     st.write("step1.Select all your inputs,")
     st.write("step2.download the folder you work for the project ,")
     st.write("step3.first time only you should download as folder after that you just click add to save data automatically,")
     st.write("step4.current pathway of the folder is C:/Users/Star World/Downloads/{file_name}.csv ")

if a=="version":

     st.write("streamlit---1.13.0")
     st.write("pandas---1.5.0")

if a=="about us" :
    st.header("ABOUT")
    st.subheader("In this application is made for model of simple billing purpose")
    st.header("FOUNDERS")
    st.write("1.Jethuram Jeyabal-founder")
    st.write("2.Jeyashree Sethuram-co.founder")
    st.write("3.Ajithkumar Sekar-App developer")
if a=="Home":
 st.header("SETHURAM TRADERS",)
 st.subheader("Greeting to All")
 st.text("Let start to work")
 product=st.radio("cakesname",["plain","plums","cream","black_forest","birthday_cake"])
 kilo = st.number_input("enter kg of cake",0,10)
 file_name=st.text_input("enter file name to download")

 button1=st.button("add")
 if product=="plain":
    kg=kilo
    total = kg * 240
    st.markdown(total)
    value()
 if product=="plums":
    kg=kilo
    total = kg * 120
    st.markdown(total)
    value()
 if product=="cream":
    kg=kilo
    total = kg * 220
    st.markdown(total)
    value()
 if product=="black_forest":
    kg=kilo
    total = kg * 230
    st.markdown(total)
    value()
 if product=="birthday_cake":
    kg=kilo
    total = kg * 320
    st.markdown(total)
    value()
