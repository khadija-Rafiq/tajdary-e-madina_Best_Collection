# import streamlit as st
# from PIL import Image
# import streamlit.components.v1 as components
# import webbrowser

# # Website Title & Config
# st.set_page_config(page_title="Tajdary Madina Collection", layout="wide")

# # Custom CSS for styling (ONLY HEADER & BUTTONS STYLED, NOTHING ELSE CHANGED)
# st.markdown("""
#     <style>

#     body, .stApp {
#             background-color: #f8f9fa; /* Light Grey Background */
#         }
#         /* Header Styling */
#         .main-header {
#             text-align: center; 
#             font-size: 55px; 
#             font-weight: bold; 
#             color: white; 
#             background: linear-gradient(to right,rgb(14, 10, 12), #C71585);
#             padding: 15px; 
#             border-radius: 15px;
#             box-shadow: 0px 4px 10px rgba(199, 21, 133, 0.5);
#         }

#         .sub-header {
#             text-align: center; 
#             font-size: 20px; 
#             color: #555;
#         }

#         .collection-title {
#             font-size: 25px; 
#             font-weight: bold; 
#             color: #C71585;
#         }


        
#         .footer {
#             text-align: center; 
#             font-size: 14px; 
#             color: gray; 
#             margin-top: 50px;
#         }

#         /* Button Styling */
#         .stButton>button {
#             background: linear-gradient(to right, #FF1493, #C71585);
#             color: white;
#             font-size: 18px;
#             font-weight: bold;
#             padding: 12px 24px;
#             border-radius: 25px;
#             border: none;
#             transition: 0.3s ease-in-out;
#             box-shadow: 0px 4px 10px rgba(199, 21, 133, 0.5);
#         }
        
#         .stButton>button:hover {
#             background: linear-gradient(to right, #C71585, #FF1493);
#             transform: scale(1.05);
#             box-shadow: 0px 6px 15px rgba(255, 20, 147, 0.7);
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header Section
# st.markdown("<div class='main-header'>✨ Tajdar-e-Madina Collection ✨</div>", unsafe_allow_html=True)
# st.markdown("<div class='sub-header'>All Top Brands | Latest Fashion Trends | Online Shopping Available</div>", unsafe_allow_html=True)

# st.markdown(
#     """
#     <div style="display: flex; justify-content: center;">
#         <img src="./images/tm.png" />
#         style="width: 60%; height: auto; border-radius: 10px;">
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Slider for Featured Collection
# st.markdown("## Featured Collections")
# components.html(
#     """
#     <div style="display: flex; overflow-x: scroll; gap: 10px; white-space: nowrap;">
#         <img src='https://i.pinimg.com/736x/44/6c/e5/446ce5af853218ef156038c302a65e91.jpg' width='250'>
#         <img src='https://i.pinimg.com/736x/28/b4/41/28b441c4990271334a1ba68ec2cd9ea8.jpg' width='250'>
#         <img src='https://i.pinimg.com/736x/a0/9e/9a/a09e9aae5167320bd6cb4e042463c64e.jpg' width='250'>
#         <img src='https://i.pinimg.com/736x/36/28/7f/36287f03327321f59a33e80652b2a4e1.jpg' width='250'>
#     </div>
#     """, height=300
# )

# # Dress Collection Section
# st.markdown("## Shop by Category")
# col1, col2, col3 = st.columns(3)

# if 'orders' not in st.session_state:
#     st.session_state.orders = []

# with col1:
#     st.image("https://bridalcollection.pk/wp-content/uploads/2025/01/a-34-360x480.jpg")
#     st.markdown("<div class='collection-title'>Party Wear</div>", unsafe_allow_html=True)
#     if st.button("Shop Now", key="partywear"):
#         st.session_state.orders.append("Party Wear")

# with col2:
#     st.image("https://www.junaidjamshed.com/media/wysiwyg/23-Festive3PCS/J._Festive_Unstitched_Collection_3_Piece51.jpg")
#     st.markdown("<div class='collection-title'>Casual Wear</div>", unsafe_allow_html=True)
#     if st.button("Shop Now", key="casualwear"):
#         st.session_state.orders.append("Casual Wear")

# with col3:
#     st.image("https://www.dressyzone.com/cdn/shop/files/p14229-embroidered-net-maxi-dress-update_580x.jpg?v=1719991384")
#     st.markdown("<div class='collection-title'>Fancy Wear</div>", unsafe_allow_html=True)
#     if st.button("Shop Now", key="Fancy wear"):
#         st.session_state.orders.append("Fancy Wear")

# # Display Orders
# st.markdown("## Orders Received")
# if st.session_state.orders:
#     for order in st.session_state.orders:
#         st.write(f"✅ {order} ordered!")
# else:
#     st.write("No orders yet.")

# # Online Shopping & Contact
# st.markdown("## Order Online")
# st.write("📦 Fast Delivery | 💳 Secure Payment | 🛒 Easy Shopping Experience")

# if st.button("Place Order", key="order"):
#     order_form_url = "https://forms.gle/BNDJKQ7HA8CKa2mC9"
#     webbrowser.open_new_tab(order_form_url)
#     st.success("Redirecting to Order Form...")

# # Contact & Location
# st.markdown("## Visit Our Store")
# st.write("📍 Shop no# g 15, Karimabad mina bazar shop g 15 tajdar-e-madina karachi Market, Karachi")
# st.write("📞 Call us: 0318-1266595")
# st.write("📩 Email: tajdarymadina@gmail.com")

# # Footer
# st.markdown("<div class='footer'>© 2025 Tajdary Madina Collection. All rights reserved.</div>", unsafe_allow_html=True)









import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import webbrowser

# Website Title & Config
st.set_page_config(page_title="Tajdary Madina Collection", layout="wide")

# Custom CSS for styling (ONLY HEADER & BUTTONS STYLED, NOTHING ELSE CHANGED)
st.markdown("""
    <style>
    body, .stApp {
            background-color: #f8f9fa; /* Light Grey Background */
        }
        .main-header {
            text-align: center; 
            font-size: 55px; 
            font-weight: bold; 
            color: white; 
            background: linear-gradient(to right,rgb(14, 10, 12), #C71585);
            padding: 15px; 
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(199, 21, 133, 0.5);
        }

        .sub-header {
            text-align: center; 
            font-size: 20px; 
            color: #555;
        }

        .collection-title {
            font-size: 25px; 
            font-weight: bold; 
            color: #C71585;
        }

        .footer {
            text-align: center; 
            font-size: 14px; 
            color: gray; 
            margin-top: 50px;
        }

        .stButton>button {
            background: linear-gradient(to right, #FF1493, #C71585);
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 25px;
            border: none;
            transition: 0.3s ease-in-out;
            box-shadow: 0px 4px 10px rgba(199, 21, 133, 0.5);
        }
        
        .stButton>button:hover {
            background: linear-gradient(to right, #C71585, #FF1493);
            transform: scale(1.05);
            box-shadow: 0px 6px 15px rgba(255, 20, 147, 0.7);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<div class='main-header'>✨ Tajdar-e-Madina Collection ✨</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>All Top Brands | Latest Fashion Trends | Online Shopping Available</div>", unsafe_allow_html=True)

# ✅ Show local image properly
image = Image.open("./images/tm.png")
st.image(image, use_container_width=True)

# Slider for Featured Collection
st.markdown("## Featured Collections")
components.html(
    """
    <div style="display: flex; overflow-x: scroll; gap: 10px; white-space: nowrap;">
        <img src='https://i.pinimg.com/736x/44/6c/e5/446ce5af853218ef156038c302a65e91.jpg' width='250'>
        <img src='https://i.pinimg.com/736x/28/b4/41/28b441c4990271334a1ba68ec2cd9ea8.jpg' width='250'>
        <img src='https://i.pinimg.com/736x/a0/9e/9a/a09e9aae5167320bd6cb4e042463c64e.jpg' width='250'>
        <img src='https://i.pinimg.com/736x/36/28/7f/36287f03327321f59a33e80652b2a4e1.jpg' width='250'>
    </div>
    """, height=300
)

# Dress Collection Section
st.markdown("## Shop by Category")
col1, col2, col3 = st.columns(3)

if 'orders' not in st.session_state:
    st.session_state.orders = []

with col1:
    st.image("https://bridalcollection.pk/wp-content/uploads/2025/01/a-34-360x480.jpg")
    st.markdown("<div class='collection-title'>Party Wear</div>", unsafe_allow_html=True)
    if st.button("Shop Now", key="partywear"):
        st.session_state.orders.append("Party Wear")

with col2:
    st.image("https://www.junaidjamshed.com/media/wysiwyg/23-Festive3PCS/J._Festive_Unstitched_Collection_3_Piece51.jpg")
    st.markdown("<div class='collection-title'>Casual Wear</div>", unsafe_allow_html=True)
    if st.button("Shop Now", key="casualwear"):
        st.session_state.orders.append("Casual Wear")

with col3:
    st.image("https://www.dressyzone.com/cdn/shop/files/p14229-embroidered-net-maxi-dress-update_580x.jpg?v=1719991384")
    st.markdown("<div class='collection-title'>Fancy Wear</div>", unsafe_allow_html=True)
    if st.button("Shop Now", key="fancywear"):
        st.session_state.orders.append("Fancy Wear")

# Display Orders
st.markdown("## Orders Received")
if st.session_state.orders:
    for order in st.session_state.orders:
        st.write(f"✅ {order} ordered!")
else:
    st.write("No orders yet.")

# Online Shopping & Contact
st.markdown("## Order Online")
st.write("📦 Fast Delivery | 💳 Secure Payment | 🛒 Easy Shopping Experience")

if st.button("Place Order", key="order"):
    order_form_url = "https://forms.gle/BNDJKQ7HA8CKa2mC9"
    webbrowser.open_new_tab(order_form_url)
    st.success("Redirecting to Order Form...")

# Contact & Location
st.markdown("## Visit Our Store")
st.write("📍 Shop no# g 15, Karimabad mina bazar shop g 15 tajdar-e-madina karachi Market, Karachi")
st.write("📞 Call us: 0318-1266595")
st.write("📩 Email: tajdarymadina@gmail.com")

# Footer
st.markdown("<div class='footer'>© 2025 Tajdary Madina Collection. All rights reserved.</div>", unsafe_allow_html=True)
