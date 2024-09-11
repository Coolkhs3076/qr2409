import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 제목 설정
st.title("QR Code Generator")

# 사용자가 입력할 텍스트 또는 URL
data = st.text_input("Enter the text or URL to generate QR code:")

# 버튼을 눌렀을 때 QR 코드 생성
if st.button("Generate QR Code"):
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

        # QR 코드를 이미지로 변환
        img = qr.make_image(fill="black", back_color="white")

        # 이미지를 메모리 버퍼에 저장
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)

        # QR 코드 이미지를 화면에 표시
        st.image(img, caption="Generated QR Code", use_column_width=True)

        # QR 코드 이미지를 다운로드할 수 있는 링크 제공
        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.error("Please enter some text or a URL to generate a QR code.")
