import streamlit as st
import pandas as pd
import pyrebase
#'''This is for streamlit sidebar for mode window and decoration into our application'''
a = st.sidebar.radio("Navigation",["Home","PROJECT","about us","version"])
if a=="Home":
     st.header("WELCOME TO SETHURAM TRADERS")
     st.subheader("Introduction")
     st.write("In this application major used for bakery shops .It can be easy and quick understandable application")
     st.subheader("advantages")
     st.write("1.Costless application")
     st.write("2.Easy understandable")
     st.write("3.we can able to store the data to data base")
     st.header("MOBILE USERS..PLEASE ENABLE DESKTOP SITE ON YOUR BROWSER ")

if a=="version":

     st.write("streamlit==1.13.0")
     st.write('PyAutoGUI==0.9.53')
     st.write('pyrebase5==5.0.1')
     st.write('pandas==1.5.1')

if a=="about us" :
    st.header("ABOUT")
    st.subheader("In this application is made for model of simple billing purpose")
    st.header("FOUNDERS")
    st.write("1.Jethuram Jeyabal-founder")
    st.write("2.Jeyashree Sethuram-co.founder")
    st.write("3.Ajithkumar Sekar-App developer")
if a=="PROJECT":
 st.header("SETHURAM TRADERS",)     #heading for our application
 st.subheader("Greeting to All")    #sub heading for our application
 st.text("Let start to work")       #text for streamlit
 date=st.date_input('date input')   #date input button

 # creating columns for our application button
 col1, col2, col3 = st.columns(3)

 # plum cake front end using 'html'

 with col1:
        st.markdown('<p style="font-size:20px">plum cake <br /> 1kg=250</p>', unsafe_allow_html=True)

# in this column get product kg and calculate total
 with col2:
        number = st.number_input(label="plum kg", step=0.5, format="%.1f")
        kg = 250
        total = kg * number
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total}</p>', unsafe_allow_html=True)

 # plain cake
 with col1:
        st.markdown('<p style="font-size:20px">plain cake <br /> 1kg=150</p>', unsafe_allow_html=True)

 with col2:
        number1 = st.number_input(label="plain kg", step=0.5, format="%.1f")
        kg1 = 150
        total1 = kg1 * number1
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total1}</p>', unsafe_allow_html=True)

 # cream cake
 with col1:
        st.markdown('<p style="font-size:25px">cream cake <br /> 1kg=440</p>', unsafe_allow_html=True)

 with col2:
        number2 = st.number_input(label="cream kg", step=0.5, format="%.1f")
        kg2 = 440
        total2 = kg2 * number2
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total2}</p>', unsafe_allow_html=True)

 # birthday cake
 with col1:
        st.markdown('<p style="font-size:25px">Birthday cake <br /> 1kg=480</p>', unsafe_allow_html=True)

 with col2:
        number3 = st.number_input(label="birthday kg", step=0.5, format="%.1f")
        kg3 = 480
        total3 = kg3 * number3
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total3}</p>', unsafe_allow_html=True)

 # blackforest
 with col1:
        st.markdown('<p style="font-size:25px">blackforest cake <br /> 1kg=545</p>', unsafe_allow_html=True)

 with col2:
        number4 = st.number_input(label="bf kg", step=0.5, format="%.1f")
        kg4 = 545
        total4 = kg4 * number4
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total4}</p>', unsafe_allow_html=True)

 # plum one piece
 with col1:
        st.markdown('<p style="font-size:25px">plum cake peace <br /> 1kg=20</p>', unsafe_allow_html=True)

 with col2:
        number5 = st.number_input(label="plum 1 peace", step=1.0, format="%.1f")
        kg5 = 20
        total5 = kg5 * number5
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total5}</p>', unsafe_allow_html=True)

 # browne peace
 with col1:
        st.markdown('<p style="font-size:25px">browne cake peace <br /> 1kg=50</p>', unsafe_allow_html=True)

 with col2:
        number6 = st.number_input(label="1 peace browne", step=1.0, format="%.1f")
        kg6 = 50
        total6 = kg6 * number6
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total6}</p>', unsafe_allow_html=True)

 # blackforest peace
 with col1:
        st.markdown('<p style="font-size:20px">blackforest 1 peace <br /> 1kg=80</p>', unsafe_allow_html=True)

 with col2:
        number7 = st.number_input(label="blackforest 1 peace", step=1.0, format="%.1f")
        kg7 = 80
        total7 = kg7 * number7
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total7}</p>', unsafe_allow_html=True)

 # cupcake
 with col1:
        st.markdown('<p style="font-size:20px">cup cake 1 peace <br /> 1kg=30</p>', unsafe_allow_html=True)

 with col2:
        number8 = st.number_input(label="cup cake 1 peace", step=1.0, format="%.1f")
        kg8 = 30
        total8 = kg8 * number8
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total8}</p>', unsafe_allow_html=True)

 # calculate total amount using add function
 grand_total = total1 + total2 + total3 + total4 + total + total5 + total6 + total7 + total8
 st.markdown(f'<p style="font-size:20px">over all total price={grand_total}</p>',unsafe_allow_html=True)

 #create dataframe using pandas

 data={"cakes":['plum','plain','cream','birthday_cake','blackforest',
               'plum piece','browny peace','blackforest peace','cup cake peace'],
   "1kg_price":[kg,kg1,kg2,kg3,kg4,kg5,kg6,kg7,kg8],
      "buy_kg":[number,number1,number2,number3,number4,number5,number6,number7,number8],
      "total each":[total,total1,total2,total3,total4,total5,total6,total7,total8],
      "total":[grand_total,0,0,0,0,0,0,0,0],
       "date=":[date,0,0,0,0,0,0,0,0]}
 df = pd.DataFrame.from_dict(data, orient='index')
 st.dataframe(df)

 #create upload button for data into  firebase database
 if st.button("upload to database"):
        config = {'apiKey': "AIzaSyChEJILixmFxMhyImwUyrVwaHpYqVt4oRw",
                  'authDomain': "onyx-elevator-352407.firebaseapp.com",
                  'databaseURL': "https://onyx-elevator-352407-default-rtdb.firebaseio.com",
                  'projectId': "onyx-elevator-352407",
                  'storageBucket': "onyx-elevator-352407.appspot.com",
                  'messagingSenderId': "913631374819",
                  'appId': "1:913631374819:web:9457f51b7c22e1799604d6",
                  'measurementId': "G-QS1LWR421D"}
        firebase = pyrebase.initialize_app(config)
        database = firebase.database()
        d=df.to_json()
        database.push(d)
