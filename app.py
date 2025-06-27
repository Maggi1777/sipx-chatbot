import streamlit as st
from PIL import Image

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
    section[data-testid="stSidebar"] .stAlert-success {
        background-color: #d1f0d1 !important;
        color: #000000 !important;
        border: 1px solid #a3e6a3 !important;
    }
    section[data-testid="stSidebar"] .stAlert-success div {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    logo = Image.open("logo.png")  # Make sure logo.png is in the same folder
    st.image(logo, use_column_width=True)
    st.title("Welcome to Sipx 💧")
    name = st.text_input("🧑‍💼 Your Name")
    email = st.text_input("📧 Your Email")
    if name and email:
        st.success(f"Hello, {name} 👋")

# --- MAIN AREA ---
st.title("💬 Sipx Virtual Assistant")
st.write("How can I assist you today?")

question = st.text_input("")

# --- PRICING DATA ---
pricing = {
    "1l": {"carton_price": 130, "bottles_per_carton": 12},
    "500ml": {"carton_price": 165, "bottles_per_carton": 24},
    "300ml": {"carton_price": 150, "bottles_per_carton": 24}
}

def calculate_carton_cost(q, bottle_type):
    import re
    match = re.search(r'(\d+)\s*cartons?', q)
    if match:
        count = int(match.group(1))
        bottle = pricing[bottle_type]
        total_bottles = count * bottle["bottles_per_carton"]
        total_cost = count * bottle["carton_price"]
        return f"📦 {count} cartons of {bottle_type.upper()} contains {total_bottles} bottles. Total cost: ₹{total_cost}."
    return None

if question:
    question_lower = question.lower()

    # Custom Questions
    if "what is sipx" in question_lower:
        st.write("💧 Sipx is a premium packaged drinking water brand that delivers clean, safe, and pure water to customers. We focus on sustainability, hydration tech, and community impact.")

    elif "contact" in question_lower or "phone" in question_lower or "email" in question_lower:
        st.markdown("📞 You can contact Sipx at:")
        st.write("- **Phone:** +91 8309620108")
        st.write("- **Email:** [sipxofficial@gmail.com](mailto:sipxofficial@gmail.com)")

    elif "price" in question_lower or "cost" in question_lower:
        bottle_found = False
        for key in pricing:
            if key in question_lower:
                answer = calculate_carton_cost(question_lower, key)
                if answer:
                    st.write(answer)
                else:
                    st.markdown(f"""
                    💧 **Our Pricing:**
                    - 1L: ₹130/carton (12 bottles) — ₹10.83/bottle  
                    - 500ml: ₹165/carton (24 bottles) — ₹6.80/bottle  
                    - 300ml: ₹150/carton (24 bottles) — ₹5.00/bottle  
                    \nPrices may vary based on order quantity.
                    """)
                bottle_found = True
                break
        if not bottle_found:
            st.markdown(f"""
            💧 **Our Pricing:**
            - 1L: ₹130/carton (12 bottles) — ₹10.83/bottle  
            - 500ml: ₹165/carton (24 bottles) — ₹6.80/bottle  
            - 300ml: ₹150/carton (24 bottles) — ₹5.00/bottle  
            \nPrices may vary based on order quantity.
            """)

    else:
        st.warning("Sorry, I don't have an answer for that yet. Try asking about our products, pricing, or contact info.")
