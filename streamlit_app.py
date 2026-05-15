import streamlit as st

st.set_page_config(page_title="나의 소개 페이지", page_icon="🧑‍💼", layout="centered")

st.title("안녕하세요! 👋")
st.subheader("나의 자기소개 페이지에 오신 것을 환영합니다")

st.write("여기에서 간단한 나의 소개, 관심사, 경험 등을 정리할 수 있습니다.")

st.markdown("---")

st.header("📌 기본 정보")
st.markdown(
    "- 이름: 이유경\n"
    "- 직무/전공: 초등교육\n"
    "- 위치: 기숙사\n"
)

st.header("🎯 관심 분야")
st.markdown(
    "- 관심 분야 1: 여행\n"
    "- 관심 분야 2: 주식투자\n"
    "- 관심 분야 3: 다이어트\n"
)

st.markdown("---")

st.header("💬 자기소개 한 줄")
st.write("방학 중에 여행을 갈 예정이라 요즘엔 여행계획을 짜느라 바빠요.")

