import pandas as pd
import csv
import streamlit as st
def value():
  values={"products":[product],"kilogram":[kg],"total":[total]}

  df=pd.DataFrame(values,columns=["products","kilogram","total"])
  df.set_index("products",inplace=True)
  st.dataframe(df)
  button = st.download_button("create new folder", df.to_csv(),file_name=f"{file_name}.csv",mime='text/csv')
  path=f"C:/Users/Star World/Downloads/{file_name}.csv "
  if button1:

   with open(f'{path}', 'a',newline='') as file:
     h=([product,kg,total])
     writer = csv.writer(file)
     writer.writerow(h)
   file.close()

st.header("SETHURAM TRADERS",)
st.subheader("Greeting to All")
st.text("Let start to work")
product=st.radio("cakesname",["plain","plums","cream","black_forest","birthday_cake"])
kilo = st.number_input("enter your data limit",0,10)
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