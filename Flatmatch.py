from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#Import streamlit library and other useful libraries to import "toolbox" script
import streamlit as st
import subprocess
import sys

subprocess.run([f"{sys.executable}", "toolbox.py"])
import toolbox as t

# Add a title and subtitle (markdown)
st.title('Welcome to')
st.image('/Users/katharinaboelling/Desktop/Project_2477/logo.png')     #### NEEDS TO BE RELATIVE!!
st.subheader('Just enter your details and get started')

# Collect input
purpose = st.radio('Pick one (*)', ['Landlord', 'Tenant'])
name = st.text_input('Your name (*)')
city = st.selectbox('Your city (*)', ['London', 'Paris', 'Lisbon', 'Madrid', 'Rome', 'Berlin'])

age = st.slider('Your age', 20, 35)
own_gender = st.radio('Your gender', ['Female', 'Male', 'Other'])
search_gender = st.radio('Your preferred gender', ['Female', 'Male', 'Other', 'Indifferent'])
function = st.selectbox('Your job function', ['IT', 'HR', 'Sales', 'Finance', 'Medicine', 'Management','Marketing'])
hobbies = st.multiselect('Your interests', ['Sports', 'Cooking', 'Party', 'Reading', 'Games', 'Beach','Mountains'])
price = st.slider('Your maximum monthly budget', 500, 5000, step = 100)
cleanliness = st.slider('Your cleanliness preference', 1, 5)
smoking = st.radio('Your smoking preference', ['Yes', 'No', 'Do not care'])


# Start matching
button = st.button('Find Flat Match!')


# Import python script with results



#create result page
def show_result():
	st.title('Result')
	st.text(t.dict_landlord)
	col1, col2, col3 = st.columns(3)



 
if button:
	
	t.create_profile(purpose, name, city, age, own_gender, search_gender, function, hobbies, price, cleanliness, smoking)

	t.match_all(new_user)

	show_result()
# reset input fields - states?


# Reminder: How to open app
# streamlit run /Users/katharinaboelling/Desktop/Project_2477/app.py      #### NEEDS TO BE ACCESSIBLE!!

