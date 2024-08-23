import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyCakY0wA7DId2sWc7LOUQBR1tE8hgc3J8E") 
model = genai.GenerativeModel('gemini-1.5-flash')

if "chats" not in st.session_state:
    st.session_state.chats = []
# if "loop" not in st.session_state.loop:
#     st.session_state.loop = 0
# loop = st.session_state.loop
st.set_page_config( 
    page_title= "My Bujji",
    page_icon = "💬"
)


st.title("Hi I'm :violet[Bujji]")
st.write("Small Clone of Gemini API")
# loop = 1
# for chat in st.session_state.chats:
#     # st.warning(len(st.session_state.chats))
#     usr = chat['user']
#     ai = chat['response']
#     st.write(f'**User:** {usr}')
#     st.write(f'**Bujji:** {ai}')
#     loop -=1
#     break


user_query = st.text_input("Enter Your Query",key='userinput')
if user_query:
    # del st.session_state.userinput
    res = model.generate_content(user_query)
    # user_query = None
    print(res)
    st.warning("This Page and :blue[Bujji's Response] will not be for longer Time \n So You can save page as :red[PDF] by :red[Printing] is you want response ")
    st.write(f'*:blue[You]* :  {user_query}')
    st.write(f'*:orange[BUJJI]* :',  f'\n{res.text}')
    # res_text = res.text
    # st.session_state.loop +=1
    # st.session_state.chats.append({'user':user_query, 'response':res_text})
    # st.experimental_rerun()

