import streamlit as st

st.title("ユーザー個人情報入力")

if 'user_name' not in st.session_state:
    st.session_state.user_name  = ""

if 'grade' not in st.session_state:
    st.session_state.grade  = ""

if 'hobbies' not in st.session_state:
    st.session_state.hobbies  = ""

name = st.text_input("名前")
grade = st.selectbox("学年",
    ['',"小5","小6","中1","中2","中3"]) 
hobbies =  st.multiselect("趣味",
    ["読書","スポーツ","ゲーム","音楽","絵画","他"])
    
if st.button('情報を永久保存'):
    st.session_state.user_name = name  
    st.session_state.grade = grade 
    st.session_state.hobbies = hobbies  
    st.success("名前を永久保存しました！")


