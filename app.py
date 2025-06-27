import streamlit as st
from PIL import Image
import re

# --- CONFIG ---
st.set_page_config(page_title="Sipx Chatbot", page_icon="💧", layout="wide")

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
    text = text.lower()
    for size in prices:
        if size in text:
            # Check for cartons/cottons
            match_carton = re.search(r'(\d+)\s*(carton|cotton)', text)
            if match_carton:
                qty = int(match_carton.group(1))
                carton_price = prices[size]["carton_price"]
                total_price = qty * carton_price
                bottles = qty * prices[size]["bottles_per_carton"]
                return f"🧾 {qty} cartons of {size.upper()} contains {bottles} bottles. Total cost: ₹{total_price}."
            
            # Check for bottles
            match_bottles = re.search(r'(\d+)\s*bottles?', text)
            if match_bottles:
                qty = int(match_bottles.group(1))
                per_bottle = prices[size]["per_bottle"]
                total_price = round(qty * per_bottle, 2)
                return f"🧾 {qty} {size.upper()} bottles will cost ₹{total_price}."

    return None

# --- MAIN CHAT INTERFACE ---
question = st.text_input("How can I assist you today?")

if question:
    q_lower = question.lower()

    # --- Respond to FAQs ---
    if "what is sipx" in q_lower:
        st.write("💧 Sipx is a packaged drinking water brand that delivers clean, safe, and sustainable water. We offer 1L, 500ml, and 300ml bottles with a focus on community impact and health.")
    elif "contact" in q_lower:
        st.write("📞 Contact us:\n- Phone: +91 8309620108\n- Email: sipxofficial@gmail.com")
    elif "certificates" in q_lower or "report" in q_lower:
        st.write("📄 Sipx is certified with NABL, ISI, ISO, BIS, and FSSAI. You can find our reports on the website.")
    elif any(x in q_lower for x in ["price", "cost", "carton", "cotton", "bottle"]):
        response = calculate_price(question)
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






