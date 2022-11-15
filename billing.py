import pyautogui
import streamlit as st
import pandas as pd
import pyrebase
a = st.sidebar.radio("Navigation",["working rules","Home","about us","version"])
if a=="working rules":
     st.header("WELCOME TO SETHURAM TRADERS")
     st.write("step1.Select all your inputs,")
     st.write("step2.download the folder you work for the project ,")
     st.write("step3.first time only you should download as folder after that you just click add to save data automatically,")
     st.write("step4.current pathway of the folder is C:/Users/Star World/Downloads/{file_name}.csv ")

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
if a=="Home":
 st.header("SETHURAM TRADERS",)
 st.subheader("Greeting to All")
 st.text("Let start to work")
 date=st.date_input('date input')
 col1, col2, col3 = st.columns(3)
 # plum cake

 with col1:
        st.markdown('<p style="font-size:20px">plum cake <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number = st.number_input(label="plum kg", step=0.5, format="%.1f")
        kg = 250
        total = kg * number
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total}</p>', unsafe_allow_html=True)
 # plain cake
 with col1:
        st.markdown('<p style="font-size:20px">plain cake <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number1 = st.number_input(label="plain kg", step=0.5, format="%.1f")
        kg1 = 150
        total1 = kg1 * number1
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total1}</p>', unsafe_allow_html=True)

 # cream cake
 with col1:
        st.markdown('<p style="font-size:25px">cream cake <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number2 = st.number_input(label="cream kg", step=0.5, format="%.1f")
        kg2 = 440
        total2 = kg2 * number2
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total2}</p>', unsafe_allow_html=True)
 # birthday cake
 with col1:
        st.markdown('<p style="font-size:25px">Birthday cake <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number3 = st.number_input(label="birthday kg", step=0.5, format="%.1f")
        kg3 = 480
        total3 = kg3 * number3
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total3}</p>', unsafe_allow_html=True)

 # blackforest
 with col1:
        st.markdown('<p style="font-size:25px">blackforest cake <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number4 = st.number_input(label="bf kg", step=0.5, format="%.1f")
        kg4 = 545
        total4 = kg4 * number4
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total4}</p>', unsafe_allow_html=True)

 # plum one piece
 with col1:
        st.markdown('<p style="font-size:25px">plum cake peace <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number5 = st.number_input(label="plum 1 peace", step=1.0, format="%.1f")
        kg5 = 20
        total5 = kg5 * number5
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total5}</p>', unsafe_allow_html=True)

 # browne peace
 with col1:
        st.markdown('<p style="font-size:25px">browne cake peace <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number6 = st.number_input(label="1 peace browne", step=1.0, format="%.1f")
        kg6 = 50
        total6 = kg6 * number6
 with col3:
        st.write(f'<p style="font-size:25px">amount <br /> {total6}</p>', unsafe_allow_html=True)

 # blackforest peace
 with col1:
        st.markdown('<p style="font-size:20px">blackforest 1 peace <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number7 = st.number_input(label="blackforest 1 peace", step=1.0, format="%.1f")
        kg7 = 80
        total7 = kg7 * number7
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total7}</p>', unsafe_allow_html=True)

 # cupcake
 with col1:
        st.markdown('<p style="font-size:20px">cup cake 1 peace <br /> 1kg=240</p>', unsafe_allow_html=True)

 with col2:
        number8 = st.number_input(label="cup cake 1 peace", step=1.0, format="%.1f")
        kg8 = 30
        total8 = kg8 * number8
 with col3:
        st.write(f'<p style="font-size:20px">amount <br /> {total8}</p>', unsafe_allow_html=True)
 grand_total = total1 + total2 + total3 + total4 + total + total5 + total6 + total7 + total8
 st.markdown(f'<p style="font-size:20px">over all total price={grand_total}</p>',unsafe_allow_html=True)
 if st.button("Reset"):
    pyautogui.hotkey("ctrl", "F5")

 data={"cakes":['plum','plain','cream','birthday_cake','blackforest',
               'plum piece','browny peace','blackforest peace','cup cake peace'],
   "1kg_price":[kg,kg1,kg2,kg3,kg4,kg5,kg6,kg7,kg8],
      "buy_kg":[number,number1,number2,number3,number4,number5,number6,number7,number8],
      "total each":[total,total1,total2,total3,total4,total5,total6,total7,total8],
      "total":[grand_total],
       "date=":[date]}
 df = pd.DataFrame.from_dict(data, orient='index')
 st.dataframe(df)
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