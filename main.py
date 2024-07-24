import streamlit as st
st.title('나의 첫 번째 웹 서비스')
name = st.text_input('이름을 입력해 주세요 :')
menu = st.selectbox('좋아하는 과일을 선택하세요!', ['수박', '복숭아', '사과'])
if st.button('인사말 생성') :
   st.write(f'안녕하세요, {name}님! 당신의 좋아하는 음식은 {menu}입니다. 오늘도 좋은 하루 보내세요!')
