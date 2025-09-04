import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model and dataframe
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("💻 Laptop Price Predictor")

# 1st option -> Brand
Company_Name = st.selectbox('Brands', df['Company'].unique())

# 2nd option -> Type of Laptop
TypeName = st.selectbox('Types', df['TypeName'].unique())

# 3rd option -> RAM
Ram = st.selectbox('RAM (in GB)', [2,4,6,8,12,16,24,32,64])

# 4th option -> Weight
Weight = st.number_input('Weight of the Laptop (in Kg)')

# 5th option -> Touchscreen
TouchScreen = st.selectbox('Touch Screen', ['No','Yes'])

# 6th option -> IPS Panel
IPS_Panel = st.selectbox('IPS Panel', ['No','Yes'])

# 7th option -> Screen Size
Screen_Size = st.number_input('Screen Size (in inches)')

# 8th option -> Resolution
Resolution = st.selectbox('Screen Resolution', 
                          ['1920*1080','1366*768','1600*900','3440*2160','2560*1440','2304*1440'])

# 9th option -> CPU
Cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# 10th option -> HDD
HDD = st.selectbox('HDD (in GB)', [0,128,256,512,1024,2048])

# 11th option -> SSD
SSD = st.selectbox('SSD (in GB)', [0,8,128,256,512,1024])

# 12th option -> GPU
Gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# 13th option -> OS
os = st.selectbox('OS', df['os'].unique())


# Function to calculate PPI
def calculate_ppi(resolution, screen_size):
    x_res, y_res = map(int, resolution.split('*'))
    ppi = ((x_res**2 + y_res**2) ** 0.5) / screen_size
    return ppi


if st.button('💰 Predict Price'):
    # Convert categorical Yes/No to 0/1
    TouchScreen_val = 1 if TouchScreen == 'Yes' else 0
    IPS_val = 1 if IPS_Panel == 'Yes' else 0

    # Calculate PPI
    ppi = calculate_ppi(Resolution, Screen_Size)

    # Prepare input query in correct column order
    query = pd.DataFrame([[Company_Name, TypeName, Ram, Weight, TouchScreen_val, IPS_val, ppi, Cpu, HDD, SSD, Gpu, os]],
                         columns=['Company','TypeName','Ram','Weight','TouchScreen','IPS Panel','ppi','Cpu brand','HDD','SSD','Gpu brand','os'])

    # Prediction
    prediction = np.exp(pipe.predict(query)[0])  # log-transform ka reverse
    st.success(f"💸 The predicted price of this laptop is: ₹ {int(prediction)}")
