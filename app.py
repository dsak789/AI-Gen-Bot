import streamlit as st
import google.generativeai as genai


genai.configure(api_key=st.secrets['API_KEY']) 
model = genai.GenerativeModel('gemini-1.5-flash')

if "chats" not in st.session_state:
    st.session_state.chats = []
# if "loop" not in st.session_state.loop:
#     st.session_state.loop = 0
# loop = st.session_state.loop
st.set_page_config( 
    page_title= "Im Bujji",
    page_icon = "💬"
)


st.title("Hi..! I'm :green[Bujji]")
st.write(":orange[Single] Response Chat bot")
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
    st.warning("This Page and :blue[Bujji's Response] will not be for longer Time \n So You can save page as :red[PDF] by :red[Printing] If you want response ")
    st.write(f'*:blue[You]* :  {user_query}')
    st.write(f'*:violet[BUJJI]* :',  f'\n{res.text}')
    # res_text = res.text
    # st.session_state.loop +=1
    # st.session_state.chats.append({'user':user_query, 'response':res_text})
    # st.experimental_rerun()

