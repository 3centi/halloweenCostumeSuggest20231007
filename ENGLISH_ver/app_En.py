import json
import streamlit as st
import time
import suggest_randomly
from ENGLISH_ver import suggest_by_chatgptEn

def app_en(ask_chatgpt_count):
    
    # タイトル.
    st.title('Halloween Costume Ideas！🎃')
    st.caption('ver0.0.3')
    st.caption('<a href="https://forms.gle/PrZb4MCu8uY3J5n48">Feedback</a>', unsafe_allow_html=True)

    #タブに分割
    suggest_randomly_tab, suggest_by_chatgpt_tab = st.tabs(['Suggest Ramdomely 👻','Ask ChatGPT 🤖'])

    # 仮装をランダムに提案.
    with suggest_randomly_tab:
        st.header('Suggest Randomly 👻')

        if "cos_list_r" not in st.session_state:
            st.session_state.cos_list_r = []

        ## halloween_cos.json の読み取り.
        json_path = 'ENGLISH_ver/halloween_cosEn.json'

        halloween_json = open(json_path , 'r')
        load_json= json.load(halloween_json)

        if st.button('Suggest! '):
            sug_r = suggest_randomly.Suggest_randomly(load_json)
            st.session_state.cos_list_r = sug_r.suggest_randomly()
            st.write(f'I suggest {len(st.session_state.cos_list_r)} costume ideas！Do you find any good idea？🧙‍♀️')

        for i, cos in enumerate(st.session_state.cos_list_r):
            st.write(f'{i+1}: {cos}')



    # 仮装をChatGPTに提案.
    with suggest_by_chatgpt_tab:
        st.header('Ask ChatGPT 🤖')

        ## chatgpt のAPIキー.
        # api_key = st.secrets['APIKEY']
        api_key = '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'

        if 'sug_count' not in st.session_state:
            st.session_state.sug_count = ask_chatgpt_count
        if 'gender' not in st.session_state:
            st.session_state.gender = None
        if 'last_year_cos' not in st.session_state:
            st.session_state.last_year_cos = None
        if 'budget' not in st.session_state:
            st.session_state.budget = None
        if 'sug' not in st.session_state:
            st.session_state.sug=''


        with st.expander("Add more infomation(optional)", expanded=False):
            
            st.session_state.gender = st.text_input('gender',max_chars = 8)
            st.session_state.last_year_cos = st.text_input('last year costume', max_chars = 25)
            st.session_state.budget = st.text_input('budget',max_chars = 15)

        if st.session_state.sug_count <= 3:
            if st.button('Let’s Ask！(It will take 30 sec)'):
                
                #if not st.session_state.sug:
                    #st.write('Please wait...It will take about 30 seconds 😞')

                #time.sleep(1)

                if st.session_state.gender == '':
                    gender = None
                if st.session_state.last_year_cos == '':
                    last_year_cos = None
                if st.session_state.budget == '':
                    budget = None

                sug_c = suggest_by_chatgptEn.Suggest_by_chatgpt(
                    api_key = api_key, 
                    gender = st.session_state.gender, 
                    last_year_cos = st.session_state.last_year_cos, 
                    budget = st.session_state.budget
                )
                try:
                    sug_c.make_content()

                    with st.spinner('Please wait...It will take about 30 seconds 😞'):
                        time.sleep(1)
                        st.session_state.sug = sug_c.request_chatgpt()

                    st.session_state.sug = f'The answer from ChatGPT🤖！: {st.session_state.sug}'
                    st.session_state.sug_count += 1
                except:
                    st.write('Sorry！Something is wrong. Push "Let’s Ask！" again！🔧')

        st.write(st.session_state.sug)