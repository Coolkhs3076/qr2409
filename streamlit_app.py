import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# QR 코드 생성기
st.title("QR Code Generator")

# 사용자로부터 입력을 받기
data = st.text_input("Enter data for the QR code:")

# QR 코드를 생성하고 다운로드 버튼 제공
if data:
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white").convert('RGB')  # 이미지를 RGB로 변환

    # 이미지를 메모리 버퍼에 저장
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    # 이미지 보여주기 (BytesIO 객체를 사용)
    st.image(buf, caption="Generated QR Code", use_column_width=True)

    # 다운로드 버튼
    st.download_button(
        label="Download QR Code",
        data=buf,
        file_name="qrcode.png",
        mime="image/png"
    )
