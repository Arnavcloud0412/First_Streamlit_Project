import streamlit as st
import google.generativeai as genai

st.title("Chat_Bot")
st.write("Your personal assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

def bot_response(user_input):
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text

def chat_display():
    for messages in st.session_state.messages:
        if messages["role"] == "user":
            st.chat_message("user").markdown(messages['content'])

        if messages["role"] == "assistant":
            st.chat_message("assistant").markdown(messages['content'])

user_input = st.chat_input("") 

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = bot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})

    chat_display()