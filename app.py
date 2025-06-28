import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sipx Virtual Assistant", layout="wide")

# --- SIDEBAR STYLING ---
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
    div[data-testid="stSidebarUserContent"] p {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- LOGO ---
logo = Image.open("logo.png")
st.sidebar.image(logo, use_container_width=True)

# --- SIDEBAR INPUT ---
st.sidebar.title("Welcome to Sipx💧")
user_name = st.sidebar.text_input("🧑 Your Name")
user_email = st.sidebar.text_input("📧 Your Email")

if user_name and user_email:
    st.sidebar.success(f"Hello, {user_name} 👋", icon="✅")

# --- MAIN UI ---
st.title("💬 Sipx Virtual Assistant")
query = st.text_input("How can I assist you today?")

# --- PRICING INFO ---
pricing = {
    "1L": {"carton_price": 130, "bottles_per_carton": 12},
    "500ml": {"carton_price": 165, "bottles_per_carton": 24},
    "300ml": {"carton_price": 150, "bottles_per_carton": 24}
}

def calculate_carton_cost(query):
    import re
    pattern = re.search(r'(\d+)\s+cartons?\s+of\s+(\d+)\s*ml', query.lower())
    if pattern:
        cartons = int(pattern.group(1))
        size = pattern.group(2) + "ml"
        if size in pricing:
            carton_price = pricing[size]["carton_price"]
            bottles = pricing[size]["bottles_per_carton"]
            total_bottles = cartons * bottles
            total_cost = cartons * carton_price
            return f"📦 {cartons} cartons of {size.upper()} contains {total_bottles} bottles. Total cost: ₹{total_cost}."
    return None

# --- RESPONSE ---
if query:
    calc_result = calculate_carton_cost(query)
    if calc_result:
        st.success(calc_result)
    else:
        st.markdown("💧 **Our Pricing:**")
        for size, info in pricing.items():
            per_bottle = info["carton_price"] / info["bottles_per_carton"]
            st.markdown(f"- {size}: ₹{info['carton_price']}/carton ({info['bottles_per_carton']} bottles) — ₹{per_bottle:.2f}/bottle")
        st.caption("Prices may vary based on order quantity.")
        

