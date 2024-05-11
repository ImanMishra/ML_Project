import streamlit as st
import pickle
st.title('MPG ML Project')
#displacement	horsepower	weight	acceleration
displacement = st.number_input('Displacement',value = 300,placeholder = 'Enter a value for displacement')
Horsepower = st.number_input('Horsepower',value = 130,placeholder = 'Enter a value for Horsepower')
weight = st.number_input('weight',value = 3000,placeholder= 'Enter a value for weight')
Acceleration = st.number_input('Acceleration',value = 12,placeholder = 'Enter a value for acceleration')

loaded_model = pickle.load(open('mpg_regression_sav','rb'))

prediction = loaded_model.predict([[displacement,Horsepower,weight,Acceleration]])
st.subheader(f'predicted MPG value for above parameter is {prediction[0]}')
# st.write(prediction)