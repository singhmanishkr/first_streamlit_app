import streamlit
import pandas

streamlit.title("My parents new healthy dinner")
streamlit.header("Breakfast Favorites")
streamlit.text("Omega3 & Buleberry Oatmeal")
streamlit.text("Kale, Spanich & Rocket Smoothie")
streamlit.text("Hard-Boiled Free Range Egg")
streamlit.text("Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
