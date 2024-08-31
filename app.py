import streamlit as st
import time
import google.generativeai as genai
import datetime

genai.configure(api_key= st.secrets['API_KEY']) 
model = genai.GenerativeModel('gemini-1.5-flash')

if "chats" not in st.session_state:
    st.session_state.chats = []
st.set_page_config( 
    page_title= "Im Bujji",
    page_icon = "💬"
)


st.title("Hi..! I'm :green[Bujji]")
st.write(":orange[Single] Response Chat bot")

current_date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
file_name_txt = f"bujji_response_{current_date}.txt"
file_name_md = f"bujji_response_{current_date}.md"

user_query = st.chat_input("Enter Your Query",key='userinput')
if user_query:
    res = model.generate_content(user_query)
    def res_stream():
        for word in res.text:
            yield word + ''
            time.sleep(0.01)
            
    st.warning("This Page and :blue[Bujji's Response] will not be for longer TIME \n So You can save Response as :red[TEXT] using below :red[Download Button] If you want response. ")
    with st.chat_message("user"):
        st.write(f'*:blue[You]* :  {user_query}')
    with st.chat_message("ai"):
        st.write_stream(res_stream)
        st.caption("You can Download this response either as Textfile or ReadmeFile")
        st.download_button(label="⬇️Text File", 
            data=res.text, 
            file_name=file_name_txt, 
            mime='text/plain')

        st.download_button(label="⬇️Readme File", 
            data=res.text, 
            file_name=file_name_md, 
            mime='text/plain')
    
