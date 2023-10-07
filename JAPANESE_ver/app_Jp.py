import json
import streamlit as st
import time
import suggest_randomly
from JAPANESE_ver import suggest_by_chatgptJp


def app_jp(ask_chatgpt_count):

    # タイトル.
    st.title('ハロウィンの仮装を提案します！🎃')
    st.caption('ver0.0.3')
    st.caption('<a href="https://marked-jaborosa-40b.notion.site/6858ff8ef2ac437b856905448122dafa?pvs=4">使い方</a>、<a href="https://forms.gle/PrZb4MCu8uY3J5n48">フィードバック</a>', unsafe_allow_html=True)

    #タブに分割
    suggest_randomly_tab, suggest_by_chatgpt_tab = st.tabs(['仮装をランダムに提案 👻','ChatGPTにきく 🤖'])

    # 仮装をランダムに提案.
    with suggest_randomly_tab:
        st.header('仮装をランダムに提案 👻')

        if "cos_list_r" not in st.session_state:
            st.session_state.cos_list_r = []

        ## halloween_cos.json の読み取り.
        json_path = 'JAPANESE_ver/halloween_cosJp.json'

        halloween_json = open(json_path , 'r')
        load_json= json.load(halloween_json)

        if st.button('早速提案してもらう ! '):
            sug_r = suggest_randomly.Suggest_randomly(load_json)
            st.session_state.cos_list_r = sug_r.suggest_randomly()
            st.write(f'{len(st.session_state.cos_list_r)}個提案しました！いい仮装は見つかりましたか？🧙‍♀️')

        for i, cos in enumerate(st.session_state.cos_list_r):
            st.write(f'{i+1}: {cos}')



    # 仮装をChatGPTに提案.
    with suggest_by_chatgpt_tab:
        st.header('ChatGPTにきく 🤖')

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


        with st.expander("条件を入力(任意)", expanded=False):
            
            st.session_state.gender = st.text_input('性別',max_chars=5)
            st.session_state.last_year_cos = st.text_input('前回の仮装',max_chars=20)
            st.session_state.budget = st.text_input('予算',max_chars=15)

        if st.session_state.sug_count <= 3:
            if st.button('提案してもらう！(時間がかかります)'):
                
                #if not st.session_state.sug:
                    #st.write('少々お待ちください。回答が返ってくるまで20~30秒ほどかかります 😞')

                #time.sleep(1)

                if st.session_state.gender == '':
                    gender = None
                if st.session_state.last_year_cos == '':
                    last_year_cos = None
                if st.session_state.budget == '':
                    budget = None

                sug_c = suggest_by_chatgptJp.Suggest_by_chatgpt(
                    api_key = api_key, 
                    gender = st.session_state.gender, 
                    last_year_cos = st.session_state.last_year_cos, 
                    budget = st.session_state.budget
                )
                try:
                    sug_c.make_content()

                    with st.spinner('少々お待ちください。回答が返ってくるまで20~30秒ほどかかります 😞'):
                        time.sleep(1)
                        st.session_state.sug = sug_c.request_chatgpt()
                    
                    st.session_state.sug = f'ChatGPT 🤖からの回答です！: {st.session_state.sug}'
                    st.session_state.sug_count += 1
                except:
                    st.write('ごめんなさい！ちょっと失敗したので、もう一度提案のボタンを押してください！🔧')

        st.write(st.session_state.sug)

