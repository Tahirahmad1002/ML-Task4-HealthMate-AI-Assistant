import streamlit as st
import sys
import os

# Link to our project logic
sys.path.append("/content/drive/MyDrive/HealthMateAI_Project")
from chatbot_logic import get_health_response

# 1. Page Configuration & Theme
st.set_page_config(page_title="HealthMate AI", page_icon="🏥", layout="wide")

# 2. Professional Sidebar (Branding Tahir)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/387/387561.png", width=100)
    st.title("Developer Info")
    st.markdown("---")
    st.write("**Created by:** Tahir")
    st.write("**Role:** AI Developer Intern")
    st.write("**Project:** HealthMate AI v1.0")
    st.markdown("---")
    st.info("This AI provides general health information. For emergencies, please contact local medical services.")
    
    if st.button("🗑️ Clear Conversation"):
        st.session_state.chat_history = []
        st.rerun()

# 3. Main Interface
st.title("🏥 HealthMate AI Assistant")
st.markdown("#### *Your Intelligent Path to Wellness*")
st.caption(f"Developed by Tahir | Powered by Llama-3.2")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display conversation
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Chat Input
if user_input := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # AI logic call
    response = get_health_response(user_input, st.session_state.chat_history)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response})
