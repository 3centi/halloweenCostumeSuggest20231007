import streamlit as st
from JAPANESE_ver import app_Jp
from ENGLISH_ver import app_En

if 'langTo' not in st.session_state:
    st.session_state.langTo = 'English version'
if 'ask_chatgpt_count' not in st.session_state:
    st.session_state.ask_chatgpt_count = 0

if st.session_state.langTo == 'English version':
    if st.button(st.session_state.langTo):
        app_En.app_en(st.session_state.ask_chatgpt_count)
        st.session_state.langTo = '日本語版'
        st.experimental_rerun()
    else:
        app_Jp.app_jp(st.session_state.ask_chatgpt_count)

else:
    # st.session_state.langTo = '日本語版'.
    if st.button(st.session_state.langTo):
        app_Jp.app_jp(st.session_state.ask_chatgpt_count)
        st.session_state.langTo = 'English version'
        st.experimental_rerun()
    else:
        app_En.app_en(st.session_state.ask_chatgpt_count)