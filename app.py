import streamlit as st
from PIL import Image
import re

# --- CONFIG ---
st.set_page_config(page_title="Sipx Chatbot", page_icon="💧", layout="wide")
# --- CSS FIXED for WHITE SIDEBAR ---
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] input {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)
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



# --- LOGO & USER INFO ---
with st.sidebar:
    logo = Image.open("logo.png")
    st.image(logo, use_container_width=True)
    st.title("Welcome to Sipx 💧")
    user_name = st.text_input("🧑‍💼 Your Name")
    user_email = st.text_input("📧 Your Email")
    if user_name and user_email:
        st.success(f"Hello, {user_name} 👋")

# --- BOT TITLE ---
st.markdown("<h1 style='text-align: center;'>💬 Sipx Virtual Assistant</h1>", unsafe_allow_html=True)

# --- PRICING DATA ---
prices = {
    "1l": {"carton_price": 130, "bottles_per_carton": 12, "per_bottle": 10.83},
    "500ml": {"carton_price": 165, "bottles_per_carton": 24, "per_bottle": 6.8},
    "300ml": {"carton_price": 150, "bottles_per_carton": 24, "per_bottle": 5.0},
}

# --- PRICE CALCULATION LOGIC ---
def calculate_price(text):
    text = text.lower().replace(" ", "")
    size_match = None
    for size in prices:
        if size in text:
            size_match = size
            break

    if size_match:
        carton_match = re.search(r'(\d+)(carton|cotton)', text)
        if carton_match:
            qty = int(carton_match.group(1))
            carton_price = prices[size_match]["carton_price"]
            total_price = qty * carton_price
            bottles = qty * prices[size_match]["bottles_per_carton"]
            return f"🧾 {qty} cartons of {size_match.upper()} contains {bottles} bottles. Total cost: ₹{total_price}."

        bottle_match = re.search(r'(\d+)bottles?', text)
        if bottle_match:
            qty = int(bottle_match.group(1))
            per_bottle = prices[size_match]["per_bottle"]
            total_price = round(qty * per_bottle, 2)
            return f"🧾 {qty} {size_match.upper()} bottles will cost ₹{total_price}."

    return None

# --- MAIN CHAT INTERFACE ---
question = st.text_input("How can I assist you today?")

if question:
    q_lower = question.lower()

    if "what is sipx" in q_lower:
        st.write("💧 Sipx is a packaged drinking water brand that delivers clean, safe, and sustainable water. We offer 1L, 500ml, and 300ml bottles with a focus on community impact and health.")
    elif "contact" in q_lower:
        st.write("📞 Contact us:\n- Phone: +91 8309620108\n- Email: sipxofficial@gmail.com")
    elif "certificates" in q_lower or "report" in q_lower:
        st.write("📄 Sipx is certified with NABL, ISI, ISO, BIS, and FSSAI. You can find our reports on the website.")
    elif any(x in q_lower for x in ["price", "cost", "carton", "cotton", "bottle"]):
        response = calculate_price(q_lower)
        if response:
            st.write(response)
        else:
            st.write(
                "💧 Our Pricing:\n"
                "- 1L: ₹130/carton (12 bottles) — ₹10.83/bottle\n"
                "- 500ml: ₹165/carton (24 bottles) — ₹6.80/bottle\n"
                "- 300ml: ₹150/carton (24 bottles) — ₹5.00/bottle\n"
                "*Prices may vary based on order quantity.*"
            )
    else:
        st.info("🤖 Sorry, I don't have an answer for that yet. Try asking about our products, prices, or contact info.")








