import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyCakY0wA7DId2sWc7LOUQBR1tE8hgc3J8E") 
model = genai.GenerativeModel('gemini-1.5-flash')

chats = dict()

st.set_page_config( 
    page_title= "My Bujji",
    page_icon = "💬"
)


st.title("Hi Im Bujji")
st.header("Dummy Clone of Gemini API")

user_query = st.text_input("Enter Your Query")


# chats.update("aHelo")
# chats.update("b""Helo")

# for item in chats:
#     st.write(item)



if user_query:
    res = model.generate_content(user_query)
    print(res)
    st.write(res.text)