import streamlit as st
import google.generativeai as genai

# ================= CẤU HÌNH =================
st.set_page_config(
    page_title="Trợ lý GVCN THPT",
    page_icon="🎓",
    layout="centered"
)

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
MODEL_NAME = "gemini-2.5-flash-lite"

SYSTEM_PROMPT = """
Bạn là TRỢ LÝ GIÁO VIÊN CHỦ NHIỆM LỚP THPT 
được xây dựng để hỗ trợ giáo viên chủ nhiệm có nhiều năm kinh nghiệm.

Nguyên tắc:
- Tôn trọng vai trò và quyết định của giáo viên
- Giải pháp mang tính sư phạm, thực tiễn, nhân văn
- Không thay thế giáo viên, chỉ hỗ trợ tham vấn

Luôn trình bày rõ ràng, chừng mực, phù hợp quy định Bộ GD&ĐT.
Luôn kết thúc bằng một gợi ý ngắn để giáo viên cân nhắc.
"""

# ================= STYLE (CSS NHẸ – TRANG TRỌNG) =================
st.markdown("""
<style>
    .main-title {
        font-size: 34px;
        font-weight: 700;
        text-align: center;
        color: #2c3e50;
    }
    .sub-title {
        text-align: center;
        font-size: 16px;
        color: #555;
        margin-bottom: 30px;
    }
    .box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
    }
    textarea {
        font-size: 15px !important;
    }
</style>
""", unsafe_allow_html=True)

# ================= TIÊU ĐỀ =================
st.markdown("<div class='main-title'>🎓 Trợ lý Giáo viên Chủ nhiệm THPT</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Ứng dụng Trí tuệ Nhân tạo Gemini hỗ trợ công tác chủ nhiệm</div>", unsafe_allow_html=True)

# ================= THANH BÊN =================
with st.sidebar:
    st.header("📌 Chức năng hỗ trợ")
    st.markdown("""
    - Soạn kế hoạch chủ nhiệm  
    - Nhận xét học sinh  
    - Xử lý tình huống sư phạm  
    - Soạn thông báo phụ huynh  
    - Tổng hợp báo cáo lớp  
    """)
    st.markdown("---")
    st.caption("💡 AI chỉ đóng vai trò trợ lý – quyết định cuối cùng thuộc về giáo viên.")

# ================= KHUNG NHẬP =================
st.markdown("<div class='box'>", unsafe_allow_html=True)

user_input = st.text_area(
    "📘 Nhập yêu cầu của giáo viên chủ nhiệm:",
    placeholder="Ví dụ: Soạn kế hoạch chủ nhiệm tháng 10 cho lớp 10A...",
    height=160
)

col1, col2 = st.columns([1, 3])
with col1:
    submit = st.button("📤 Gửi yêu cầu")

st.markdown("</div>", unsafe_allow_html=True)

# ================= XỬ LÝ AI =================
if submit:
    if user_input.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung yêu cầu.")
    else:
        with st.spinner("🤖 Trợ lý AI đang hỗ trợ giáo viên..."):
            try:
                model = genai.GenerativeModel(MODEL_NAME)
                response = model.generate_content(
                    SYSTEM_PROMPT + "\n\nYÊU CẦU GIÁO VIÊN:\n" + user_input
                )

                st.markdown("### 📄 Kết quả hỗ trợ")
                st.markdown("<div class='box'>", unsafe_allow_html=True)
                st.write(response.text)
                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"❌ Có lỗi xảy ra: {e}")

# ================= CHÂN TRANG =================
st.markdown("---")
st.caption(
    "© Ứng dụng phục vụ công tác giáo viên chủ nhiệm THPT | "
    "Phát triển theo định hướng chuyển đổi số giáo dục"
)
