import streamlit as st 
import qrcode


st.title('test title')

url = st.text_input('type url')
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image(fill_color="black", black_color="white")
img.save("qrcode.png")

if st.button('this is button'):
    st.image("qrcode.png")
