import streamlit as st
st.write("ユーザー個人情報暴露ページ")

if 'user_name' in st.session_state and st.session_state.user_name:
    
    # st.success(f"名前:{st.session_state.user_name}")
    # st.success(f"学年:{st.session_state.grade}")
    # st.success(f"趣味:{st.session_state.hobbies}")
    # st.write("メインページで入力した情報は、ちゃんと暴露されています。")
    col1 ,col2 = st.columns(2)

    with col1:
        st.metric("名前",st.session_state.user_name)
        st.metric("学年",st.session_state.grade)

    with col2:
        if st.session_state.get("hobbies"):
            st.write("**趣味:**")
            for hobby in st.session_state.hobbies:
                st.write(f"・{hobby}") 
        else:
            st.write("**趣味:** 未設定")              

    st.balloons()

else:
    st.error("✘　暴露する情報が設定できていません。")
    st.write("メインページで情報を入力してください。")    
