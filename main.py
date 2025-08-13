import streamlit as st

# 페이지 설정 🎯
st.set_page_config(
    page_title="🌈 MBTI 월드",
    page_icon="🧠",
    layout="wide"
)

# CSS 스타일 💅
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #ffecd2, #fcb69f);
    }
    .mbti-card {
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem 0;
        font-size: 1.2rem;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        background: white;
        transition: transform 0.2s ease-in-out;
    }
    .mbti-card:hover {
        transform: scale(1.05);
        background: #ffe8d6;
    }
    .emoji {
        font-size: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 앱 제목 🎉
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 16유형 대탐험 🧠</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>이모지 가득한 성격 탐험의 세계로 오신 것을 환영합니다! 🚀💫</p>", unsafe_allow_html=True)

# MBTI 데이터 📚
mbti_data = {
    "ISTJ": ("📋", "책임감 있고 체계적이며 신뢰할 수 있는 성향."),
    "ISFJ": ("🤝", "헌신적이고 세심하며 배려심이 깊음."),
    "INFJ": ("🔮", "통찰력과 이상주의를 바탕으로 깊은 관계를 중시."),
    "INTJ": ("♟️", "전략적이고 독창적이며 목표 지향적."),
    "ISTP": ("🛠️", "현실적이고 문제 해결 능력이 뛰어남."),
    "ISFP": ("🎨", "온화하고 유연하며 감성적인 성향."),
    "INFP": ("🌸", "가치 중심적이며 창의적인 이상주의자."),
    "INTP": ("🧩", "분석적이고 논리적이며 호기심이 많음."),
    "ESTP": ("🏄", "활동적이고 모험심이 강하며 적응력이 뛰어남."),
    "ESFP": ("🎉", "사교적이고 즉흥적이며 긍정적."),
    "ENFP": ("🚀", "열정적이고 창의적이며 자유로운 영혼."),
    "ENTP": ("⚡", "재치 있고 도전적이며 다재다능."),
    "ESTJ": ("📊", "조직적이고 현실적이며 리더십이 강함."),
    "ESFJ": ("💌", "친근하고 협력적이며 배려심이 깊음."),
    "ENFJ": ("🌟", "사교적이고 지도력이 뛰어나며 사람 중심."),
    "ENTJ": ("👑", "결단력과 추진력이 강하며 목표 중심.")
}

# 컬럼 구성 🖼️
col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

# 버튼 생성 🎯
for i, (mbti_type, (emoji, desc)) in enumerate(mbti_data.items()):
    with cols[i % 4]:
        if st.button(f"{emoji} {mbti_type}"):
            st.session_state["selected_type"] = (mbti_type, emoji, desc)

# 선택된 MBTI 표시 📝
if "selected_type" in st.session_state:
    mbti_type, emoji, desc = st.session_state["selected_type"]
    st.markdown(
        f"""
        <div class="mbti-card">
            <div class="emoji">{emoji}</div>
            <h2>{mbti_type}</h2>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
