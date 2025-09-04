import streamlit as st
import numpy as np
import pickle

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

#1st option->asking the customer which brand of laptop he needs
Company_Name = st.selectbox('Brands',df['Company'].unique())

#2nd option->asking the customer which Type of laptop he needs
type =st.selectbox('Types',df['TypeName'].unique())

#3rd option ->ram
Ram =st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#4th weight
weight = st.number_input('Weight Of the Laptop')

#5th ->Touchscreen
touchScreen = st.selectbox('TouchScreen',['No','Yes'])

#6th ->IPS panel
ips_panel = st.selectbox('IPS PANEL',['No','Yes'])

# 7th -> Screen Size (minimum 10 inches)
screen_size = st.number_input('Screen Size (in inches)', min_value=10.0, step=0.1)

#8th resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1640x900','3440x2160'])

#9th CPU
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0,128,256,512,1024,2048])

ssd =st.selectbox('SSD(in GB)', [0,8,128,256,512,1024])

gpu = st.selectbox('GPU', df['Gpu brand'].unique())

os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price '):
    ppi = None
    if touchScreen == 'Yes':
        touchScreen = 1
    else:
        touchScreen=0    
    
    if ips_panel == 'Yes':
        ips_panel = 1
    else:
         ips_panel =0

X_res= int(resolution.split('x')[0])
Y_res= int(resolution.split('x')[1])

    # Prevent division by zero
if screen_size > 0:
        ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
else:
        st.error("Please enter a valid Screen Size (greater than 0).")
        st.stop()
query = np.array([Company_Name , type , Ram, weight, touchScreen,ips_panel,ppi,cpu,hdd,ssd,gpu,os])

query = query.reshape(1,12)
#since hmne log me convert kr diya tha price ko ..yha hme exponent krna pdega to get actual value
st.title("The Predicted price of this configuration is:" + str(int(np.exp(pipe.predict(query)))))
                 
