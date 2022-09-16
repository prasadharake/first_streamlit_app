import streamlit as  st
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError

st.title('My MOMs New Healthy Diner')
st.header('Breakfast Menu')
st.text('🥣Omega 3 & Blueberry Oatmeal')
st.text('🥗Kale, Spinach & Rocket Smoothie')
st.text('🐔Hard-Boiled Free-Range Egg')
st.text('🥑🍞Avocado Toast')

   
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
         fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
         return fruityvice_normalized         
         
st.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
      st.error("Please enter fruit to get information.")
   else:
      back_from_function=get_fruityvice_data(fruit_choice)
      st.dataframe(back_from_function)

except URLError as e:
   st.error()

#Dont run anything past here till ew troubleshoot
st.stop()

st.header("The Fruit load list contains:")

def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()

if st.button('Get Fruit load list')
   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   st.dataframe(my_data_rows)


#Allow the end user to add fruit to the list 
add_my_fruit=st.text_input("What fruit would you like to add?")
st.write('Thanks for adding  ', add_my_fruit)

my_cur.execute("Insert into pc_rivery_db.public.FRUIT_LOAD_LIST values ('from st')")
