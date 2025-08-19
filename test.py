import streamlit as st
import random

# 페이지 기본 세팅
st.set_page_config(page_title="오늘의 운세 ✨", page_icon="🔮", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align: center; color: purple;'>🔮 오늘의 운세 보러 가기 🔮</h1>", unsafe_allow_html=True)
st.write("")

# 이름 입력
name = st.text_input("✨ 이름을 입력하세요 ✨")

# 운세 리스트
fortunes = [
    "오늘은 웃는 일이 가득해요 😆🍀",
    "작은 행운이 다가오고 있어요 🌈✨",
    "새로운 기회가 찾아올 거예요 🚀🌟",
    "친구와 즐거운 하루를 보내게 돼요 🎉👯",
    "기분 좋은 소식을 듣게 될 거예요 💌🎶",
    "오늘은 집중력이 최고예요 📚🔥",
    "뜻밖의 선물을 받을 수도 있어요 🎁💖",
    "하루 종일 에너지가 넘쳐요 ⚡🏃‍♂️",
    "사랑이 다가오고 있어요 💘🌹",
    "노력한 만큼 결실을 맺게 돼요 🌱🌸",
]

# 버튼 클릭 시 운세 출력
if st.button("✨ 오늘의 운세 보기 ✨"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요 🙏")
    else:
        fortune = random.choice(fortunes)
        score = random.randint(1, 100)  # 오늘의 운세 점수

        # 카드 모양 스타일 적용
        st.markdown(
            f"""
            <div style="
                background-color: #fdf2ff;
                border-radius: 15px;
                padding: 25px;
                margin-top: 20px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
                text-align: center;
                ">
                <h2 style="color: purple;">🌟 {name}님의 오늘의 운세 🌟</h2>
                <p style="font-size: 20px; color: #333;">👉 {fortune}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 운세 점수 표시
        st.subheader("✨ 오늘의 운세 점수 ✨")
        st.progress(score / 100)  # 프로그레스바
        st.write(f"💯 점수: **{score}점**")

