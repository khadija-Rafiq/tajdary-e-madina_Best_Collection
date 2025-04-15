

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tajdary Madina Collection", layout="wide")

# ---------- PASSWORD PROTECTION ----------
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        with st.form("password_form", clear_on_submit=True):
            password = st.text_input("🔒 Enter password to continue:", type="password")
            if st.form_submit_button("Submit"):
                if password == "mysecretjanu":
                    st.session_state["password_correct"] = True
                else:
                    st.error("❌ Incorrect password")
        return False
    return True

if check_password():
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #fff0f5;
        }
        .main-header {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: white;
            background: linear-gradient(to right,#880e4f, #ad1457);
            padding: 15px;
            border-radius: 10px;
        }
        .sub-header {
            text-align: center;
            font-size: 18px;
            color: #333;
            margin-bottom: 20px;
        }
        .category-title {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
            color: #ad1457;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: gray;
            margin-top: 50px;
        }
        .order-btn {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .order-btn a {
            background: linear-gradient(to right, #d81b60, #ec407a);
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            padding: 10px 20px;
            text-decoration: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-header'>✨ Tajdar-e-Madina Collection ✨</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>All Top Brands | Latest Fashion Trends | Online Shopping Available</div>", unsafe_allow_html=True)

    st.image("./images/tm.png", use_container_width=True)

    st.markdown("### 🛍️ Featured Collections")
    
    st.image([
        'https://i.pinimg.com/736x/44/6c/e5/446ce5af853218ef156038c302a65e91.jpg',
        'https://i.pinimg.com/736x/28/b4/41/28b441c4990271334a1ba68ec2cd9ea8.jpg',
        'https://i.pinimg.com/736x/a0/9e/9a/a09e9aae5167320bd6cb4e042463c64e.jpg',
        'https://i.pinimg.com/736x/36/28/7f/36287f03327321f59a33e80652b2a4e1.jpg'
    ], use_container_width=True, caption=["1", "2", "3", "4"])

    st.markdown("### 🧵 Shop by Category")

    if "orders" not in st.session_state:
        st.session_state.orders = []

    categories = [
        ("Party Wear", "https://bridalcollection.pk/wp-content/uploads/2025/01/a-34-360x480.jpg"),
        ("Casual Wear", "https://www.junaidjamshed.com/media/wysiwyg/23-Festive3PCS/J._Festive_Unstitched_Collection_3_Piece51.jpg"),
        ("Fancy Wear", "https://www.dressyzone.com/cdn/shop/files/p14229-embroidered-net-maxi-dress-update_580x.jpg?v=1719991384")
    ]

    for title, img_url in categories:
        st.image(img_url, use_container_width=True)
        st.markdown(f"<div class='category-title'>{title}</div>", unsafe_allow_html=True)

    st.markdown("### 📦 Order Online")
    st.write("🚚 Fast Delivery | 💳 Secure Payment | 🛍️ Easy Shopping")

    # ✅ Working "Place Order" button (opens form in new tab)
    st.markdown("""
        <div class="order-btn">
            <a href="https://docs.google.com/forms/d/1i4kzA7WICq6TrbRD1pNX-0ff4M082muRsI6lAgIW5WE/viewform" target="_blank">
                📝 Place Your Order
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📍 Visit Our Store")
    st.write("📍 Shop no# G-15, Karimabad Mina Bazar, Tajdar-e-Madina, Karachi")
    st.write("📞 0318-1266595")
    st.write("📧 tajdarymadina@gmail.com")

    st.markdown("<div class='footer'>© 2025 Tajdary Madina Collection</div>", unsafe_allow_html=True)
