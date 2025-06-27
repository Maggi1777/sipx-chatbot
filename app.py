import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText

# Set page config
st.set_page_config(page_title="Sipx Virtual Assistant", page_icon="💧", layout="wide")

# Sidebar with logo and user input
with st.sidebar:
    logo = Image.open("SIP X  LOGO.png")
    st.image(logo, use_column_width=True)
    st.title("Welcome to Sipx 💧")
    st.markdown("Please enter your details")
    user_name = st.text_input("🧑‍💼 Your Name")
    user_email = st.text_input("📧 Your Email")

    if user_name and user_email:
        st.success(f"Welcome, {user_name}!")

# Title
st.markdown("<h1 style='text-align: center;'>💬 Sipx Virtual Assistant</h1>", unsafe_allow_html=True)

question = st.text_input("How can I help you today?")

def calculate_price(text):
    text = text.lower()
    prices = {
        "1l": {"carton_price": 130, "bottles_per_carton": 12},
        "500ml": {"carton_price": 165, "bottles_per_carton": 24},
        "300ml": {"carton_price": 150, "bottles_per_carton": 24},
    }

    for size in prices:
        if size in text:
            # Extract number of cartons
            import re
            match = re.search(r'(\d+)\s*carton', text)
            if match:
                num_cartons = int(match.group(1))
                total = num_cartons * prices[size]["carton_price"]
                return f"The cost of {num_cartons} cartons of {size} bottles is ₹{total}."
            # Extract number of bottles
            match = re.search(r'(\d+)\s*bottles?', text)
            if match:
                num_bottles = int(match.group(1))
                per_bottle_price = prices[size]["carton_price"] / prices[size]["bottles_per_carton"]
                total = num_bottles * per_bottle_price
                return f"The cost of {num_bottles} {size} bottles is ₹{round(total, 2)}."
    return None

def send_email(user_name, user_email, question):
    msg = MIMEText(f"User Name: {user_name}\nEmail: {user_email}\nQuestion: {question}")
    msg["Subject"] = "New Sipx Virtual Assistant Query"
    msg["From"] = "virtualassistant@sipx.in"
    msg["To"] = "meghanamaggi1777@gmail.com"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            # You must replace the login details below with your actual app password if using Gmail
            server.login("your_email@gmail.com", "your_app_password")
            server.send_message(msg)
    except Exception as e:
        st.error(f"Email failed: {e}")

if question:
    question_lower = question.lower()

    # Custom logic for known queries
    if "what is sipx" in question_lower:
        st.write("💧 Sipx is a premium packaged drinking water brand delivering clean, safe, and sustainable hydration.")
    elif "contact" in question_lower:
        st.write("📞 You can contact Sipx at:\n- **Phone**: +91 8309620108\n- **Email**: [sipxofficial@gmail.com](mailto:sipxofficial@gmail.com)")
    elif "price" in question_lower or "cost" in question_lower or "carton" in question_lower or "bottle" in question_lower:
        response = calculate_price(question)
        if response:
            st.write("🧾 " + response)
        else:
            st.write("💧 Our Pricing:\n- 1L: ₹130/carton (12) — ₹10.83/bottle\n- 500ml: ₹165/carton (24) — ₹6.80/bottle\n- 300ml: ₹150/carton (24) — ₹5.00/bottle\n*Prices may vary with bulk orders.")
    else:
        st.info("Sorry, I don't have an answer for that yet. Try asking something about our products, contact info, or certifications.")

    # Send email notification to Sipx
    if user_name and user_email:
        send_email(user_name, user_email, question)

