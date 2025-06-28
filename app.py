import streamlit as st
from PIL import Image
import re

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sipx Virtual Assistant", layout="wide")

# --- SIDEBAR STYLING ---
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] .stButton > button {
        background-color: #d1f0d1 !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
try:
    logo = Image.open("logo.png")
    st.sidebar.image(logo, use_container_width=True)
except:
    st.sidebar.warning("Logo not found. Please upload logo.png.")

# --- USER INPUT FORM ---
st.sidebar.markdown("## Welcome to Sipx 💧")
name = st.sidebar.text_input("\U0001F464 Your Name")
email = st.sidebar.text_input("\U0001F4F7 Your Email")

if name and email:
    st.sidebar.markdown(f"<p style='color:black;'>Hello, {name}! 👋</p>", unsafe_allow_html=True)

# --- MAIN TITLE ---
st.markdown("""
    <h1 style='text-align: center;'>💬 Sipx Virtual Assistant</h1>
""", unsafe_allow_html=True)

# --- USER QUERY ---
user_input = st.text_input("How can I assist you today?")

# --- Pricing Info ---
pricing = {
    "1l": {"cost_per_carton": 130, "bottles_per_carton": 12},
    "500ml": {"cost_per_carton": 165, "bottles_per_carton": 24},
    "300ml": {"cost_per_carton": 150, "bottles_per_carton": 24}
}

# --- Chatbot Response ---
if user_input:
    user_input_lower = user_input.lower()
    response = ""

    match = re.search(r"(\d+)\s+cartons?\s+of\s+(\d+ml|1l)", user_input_lower)
    if match:
        num_cartons = int(match.group(1))
        size = match.group(2)

        if size in pricing:
            cost_per_carton = pricing[size]["cost_per_carton"]
            bottles_per_carton = pricing[size]["bottles_per_carton"]
            total_bottles = num_cartons * bottles_per_carton
            total_cost = num_cartons * cost_per_carton

            response = f"📦 {num_cartons} cartons of {size.upper()} contain {total_bottles} bottles. Total cost: ₹{total_cost}."
        else:
            response = "❌ Sorry, I couldn't identify that bottle size. Please ask about 1L, 500ml, or 300ml."

    elif "what is sipx" in user_input_lower or "about sipx" in user_input_lower:
        response = (
            "💧 **Sipx** is a packaged drinking water company delivering clean, safe, and pure water.\n"
            "We believe every drop can change a life.\n\n"
            "- 1L, 500ml, and 300ml bottles available\n"
            "- Sustainability and health in every sip\n"
            "- Supporting communities with clean water access"
        )

    elif "contact" in user_input_lower or "reach" in user_input_lower:
        response = "📞 You can contact Sipx at +91 8309620108 or email sipxofficial@gmail.com"

    elif "sizes" in user_input_lower or "available" in user_input_lower:
        response = "📦 We offer 3 bottle sizes: 1L, 500ml, and 300ml."

    elif "certifications" in user_input_lower or "reports" in user_input_lower:
        response = "📑 We provide NABL, ISI, ISO, FSSAI, and BIS lab reports."

    elif "price" in user_input_lower or "cost" in user_input_lower:
        response = (
            "💧 Our Pricing:\n\n"
            "• 1L: ₹130/carton (12 bottles) — ₹10.83/bottle\n"
            "• 500ml: ₹165/carton (24 bottles) — ₹6.80/bottle\n"
            "• 300ml: ₹150/carton (24 bottles) — ₹5.00/bottle\n\n"
            "_Prices may vary based on order quantity._\n\n"
            "You can also ask something like 'Cost of 5 cartons of 500ml bottles' for an exact amount."
        )

    else:
        response = (
            "🤖 Sorry, I don't have an answer for that yet.\n\n"
            "Try asking about our pricing, bottle sizes, contact info, or certifications."
        )

    st.write(response)

# --- Contact Info ---
st.markdown("""
---
### 📞 You can contact Sipx at:
- **Phone**: +91 8309620108  
- **Email**: [sipxofficial@gmail.com](mailto:sipxofficial@gmail.com)
""")

        

