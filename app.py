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
        background-color: #ffffff  !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO ---
logo = Image.open("logo.png")
st.sidebar.image(logo, use_container_width=True)

# --- USER INPUT FORM ---
st.sidebar.markdown("## Welcome to Sipx 💧")
name = st.sidebar.text_input("\U0001F464 Your Name")
email = st.sidebar.text_input("\U0001F4F7 Your Email")

if name and email:
    st.sidebar.success(f"Hello, {name}! 👋")

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

    elif "price" in user_input_lower or "cost" in user_input_lower:
        response = (
            "💧 Our Pricing:\n\n"
            "• 1L: ₹130/carton (12 bottles) — ₹10.83/bottle\n"
            "• 500ml: ₹165/carton (24 bottles) — ₹6.80/bottle\n"
            "• 300ml: ₹150/carton (24 bottles) — ₹5.00/bottle\n"
            "_Prices may vary based on order quantity._"
        )
    elif "what is sipx" in user_input_lower or "about sipx" in user_input_lower:
        response = (
              "💧 **Sipx** is a packaged drinking water company dedicated to delivering clean, safe, and pure water in every bottle. "
              "At Sipx, we believe:\n\n"
              "- Every drop can change a life\n"
              "- Clean water is a basic human right\n"
              "- Every Sipx bottle represents trust, health, and sustainability\n\n"
              "We offer three sizes: 1L, 500ml, 300ml.\n\n"
              "Each bottle supports our mission to bring hope, hydration, and health to the world's driest corners."
        
    )
      

    else:
        response = "🤖 I'm here to help with pricing, bottle sizes, certifications, and more. Try asking: 'What is the cost of 7 cartons of 300ml bottle?'"

    st.write(response)

# --- Contact Info ---
st.markdown("""
---
### 📞 You can contact Sipx at:
- **Phone**: +91 8309620108  
- **Email**: [sipxofficial@gmail.com](mailto:sipxofficial@gmail.com)
""")

        

