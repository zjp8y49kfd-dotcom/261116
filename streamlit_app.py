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

st.header("🎓 학력 / 교육")
st.markdown(
    "- 학교/기관: 청주교육대학교\n"
    "- 전공/과정: 영어교육학과\n"
    "- 수료/예정: 1학년\n"
)

st.header("💼 경험 / 프로젝트")
st.markdown(
    "- 경험 1: 수영동아리 엔돌핀 열심히 하고 있어요\n"
    "- 경험 2: 중학생 과외를 하고 있어요\n"
)

st.header("🎯 목표 / 다짐")
st.markdown(
    "- 단기 목표: 학점을 잘 받고 싶어요\n"
    "- 장기 목표: 살을 빼고 싶어요...\n"
)

st.header("📌 추가 정보")
st.markdown(
    "- 좋아하는 취미: 수영\n"
    "- 추천 콘텐츠: 남프랑스 여행 추천해요\n"
    "- 한 줄 팁: 밀라노에 최후의 만찬을 보러 가려면, 분기별 오픈 시간을 잘 맞추세요...\n"
)

st.markdown("---")

st.header("💬 자기소개 한 줄")
st.write("방학 중에 여행을 갈 예정이라 요즘엔 여행계획을 짜느라 바빠요.")

