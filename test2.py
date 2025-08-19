import streamlit as st
import random
import time

# 페이지 세팅
st.set_page_config(page_title="오늘의 운세 ✨", page_icon="🔮", layout="centered")

# 연보라빛 배경 적용 (CSS)
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f3e8ff;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 타이틀
st.markdown("<h1 style='text-align: center; color: purple;'>🔮 오늘의 운세 보러 가기 🔮</h1>", unsafe_allow_html=True)
st.write("")

# 이름 입력
name = st.text_input("✨ 이름을 입력하세요 ✨")

# 운세 카테고리별 리스트
fortune_categories = {
    "💖 애정운": [
        "사랑이 다가오고 있어요 💘🌹",
        "소중한 인연과 가까워질 거예요 🌟💑",
        "뜻밖의 고백을 받을 수도 있어요 😳💌"
    ],
    "📚 공부운": [
        "오늘은 집중력이 최고예요 📚🔥",
        "노력한 만큼 결실을 맺게 돼요 🌱🌸",
        "새로운 아이디어가 떠오를 거예요 💡✨"
    ],
    "💰 재물운": [
        "뜻밖의 선물을 받을 수도 있어요 🎁💖",
        "금전적으로 기분 좋은 일이 생겨요 💵🌟",
        "절약하면 큰 보상이 따를 거예요 🏦🍀"
    ],
    "😀 전체운": [
        "웃는 일이 가득해요 😆🍀",
        "작은 행운이 다가오고 있어요 🌈✨",
        "새로운 기회가 찾아올 거예요 🚀🌟"
    ]
}

# 행운의 아이템 리스트
lucky_items = ["🍎 사과", "☂️ 우산", "🎧 이어폰", "📱 휴대폰", "🎒 가방", 
               "🐱 고양이", "🌸 꽃", "🍫 초콜릿", "🕶️ 선글라스", "⌚ 시계"]

# 버튼 클릭 시 결과 출력
if st.button("✨ 오늘의 운세 보기 ✨"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요 🙏")
    else:
        with st.spinner("🔮 운세를 점치는 중..."):
            time.sleep(2)  # 긴장감 연출 2초 기다림

        # 랜덤 카테고리와 운세 선택
        category = random.choice(list(fortune_categories.keys()))
        fortune = random.choice(fortune_categories[category])
        score = random.randint(1, 100)  
        item = random.choice(lucky_items)

        # 점수에 따른 등급
        if score >= 80:
            grade = "🌟 대운 🌟"
            grade_color = "#ffd700"  # 금색
            st.balloons()  # 풍선 효과
        elif score >= 50:
            grade = "😊 보통 운 😊"
            grade_color = "#87ceeb"  # 하늘색
            # 보통 운일 때는 별도 효과 없음
        else:
            grade = "⚠️ 조심 ⚠️"
            grade_color = "#ff6961"  # 빨강
            st.snow()  # 눈 내리는 효과

        # 카드 출력
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #f8eaff, #e0bbff);
                border-radius: 20px;
                padding: 25px;
                margin-top: 20px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
                text-align: center;">
                <h2 style="color: purple;">🌟 {name}님의 오늘의 운세 🌟</h2>
                <h3 style="color: #555;">운세 카테고리: {category}</h3>
                <p style="font-size: 22px; color: #333;">👉 {fortune}</p>
                <h3 style="color:{grade_color};">오늘의 등급: {grade}</h3>
                <p style="font-size:18px;">🎁 행운의 아이템: <b>{item}</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

        # 운세 점수 표시
        st.subheader("✨ 오늘의 운세 점수 ✨")
        st.progress(score / 100)
        st.write(f"💯 점수: **{score}점**")
