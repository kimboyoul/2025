
import streamlit as st

st.set_page_config(page_title="MBTI 탐험", page_icon="🧠", layout="wide")

st.title("🧠 MBTI 16가지 유형 탐험")
st.write("각 MBTI 유형을 클릭하면 설명이 나옵니다.")

mbti_data = {
    "ISTJ": "책임감 있고 체계적이며 신뢰할 수 있는 성향.",
    "ISFJ": "헌신적이고 세심하며 배려심이 깊음.",
    "INFJ": "통찰력과 이상주의를 바탕으로 깊은 관계를 중시.",
    "INTJ": "전략적이고 독창적이며 목표 지향적.",
    "ISTP": "현실적이고 문제 해결 능력이 뛰어남.",
    "ISFP": "온화하고 유연하며 감성적인 성향.",
    "INFP": "가치 중심적이며 창의적인 이상주의자.",
    "INTP": "분석적이고 논리적이며 호기심이 많음.",
    "ESTP": "활동적이고 모험심이 강하며 적응력이 뛰어남.",
    "ESFP": "사교적이고 즉흥적이며 긍정적.",
    "ENFP": "열정적이고 창의적이며 자유로운 영혼.",
    "ENTP": "재치 있고 도전적이며 다재다능.",
    "ESTJ": "조직적이고 현실적이며 리더십이 강함.",
    "ESFJ": "친근하고 협력적이며 배려심이 깊음.",
    "ENFJ": "사교적이고 지도력이 뛰어나며 사람 중심.",
    "ENTJ": "결단력과 추진력이 강하며 목표 중심."
}

col1, col2, col3, col4 = st.columns(4)

cols = [col1, col2, col3, col4]
types = list(mbti_data.keys())

for i, mbti_type in enumerate(types):
    with cols[i % 4]:
        if st.button(mbti_type):
            st.session_state["selected_type"] = mbti_type

if "selected_type" in st.session_state:
    st.subheader(f"🔍 {st.session_state['selected_type']} 유형 설명")
    st.write(mbti_data[st.session_state['selected_type']])

