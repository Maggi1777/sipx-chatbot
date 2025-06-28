import streamlit as st
from PIL import Image

# --- Set page config ---
st.set_page_config(page_title="Sipx Virtual Assistant", page_icon="💧", layout="centered")

# --- Custom CSS Styling ---
# --- Custom CSS Styling ---
st.markdown("""
    <style>
        /* Make sidebar white */
        [data-testid="stSidebar"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }

        /* Input text (name, email) to black */
        [data-testid="stSidebar"] input {
            color: black !important;
        }

        /* Change "Hello" message text color */
        .hello-text {
            color: black;
            font-weight: bold;
            font-size: 18px;
        }

        /* Force button text to black */
        [data-testid="stSidebar"] button {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar content ---
with st.sidebar:
    try:
        logo = Image.open("logo1.svg")
        st.image(logo, use_container_width=True)
    except:
        st.warning("Logo not found. Upload 'logo.png' to display branding.")

    st.title("Sipx Assistant 🤖")
    user_name = st.text_input("👤 Your Name")
    user_email = st.text_input("📧 Your Email")

# --- Welcome Message ---
if user_name:
    st.markdown(f"<p class='hello-text'>Hi {user_name}, how can I help you today?</p>", unsafe_allow_html=True)
else:
    st.markdown("<p class='hello-text'>Hi there! Ask me anything about Sipx 💧</p>", unsafe_allow_html=True)

# --- FAQ + Smart Price Calculator ---
question = st.text_input("💬 Ask a question about our products or pricing")

# Bottle pricing
pricing = {
    "1l": {"carton_price": 130, "bottles": 12, "unit_price": 10.83},
    "500ml": {"carton_price": 165, "bottles": 24, "unit_price": 6.80},
    "300ml": {"carton_price": 150, "bottles": 24, "unit_price": 5.00}
}

def calculate_cost(bottle_type, cartons):
    try:
        carton_price = pricing[bottle_type]["carton_price"]
        total = cartons * carton_price
        return f"💰 {cartons} carton(s) of {bottle_type.upper()} will cost ₹{total:.2f}"
    except:
        return "❌ I couldn't calculate that. Please try again."

if question:
    q = question.lower()

    if "what is sipx" in q:
        st.write("💧 Sipx is a packaged water bottle company delivering trust, health, and sustainability in every drop.")
    
    elif "sizes" in q or "available" in q:
        st.write("📦 We offer 3 bottle sizes: 1L, 500ml, and 300ml.")

    elif "certificates" in q:
        st.write("📜 We’re certified with NABL, ISI, ISO, FSSAI, and BIS lab reports.")

    elif "contact" in q:
        st.write("📞 You can contact Sipx at:\n- Phone: +91 8309620108\n- Email: sipxofficial@gmail.com")

    elif "price" in q or "cost" in q:
        found = False
        for size in pricing:
            if size in q:
                # Check if cartons mentioned
                import re
                match = re.search(r"(\d+)\s*(carton|cotton|cartons)", q)
                if match:
                    cartons = int(match.group(1))
                    st.write(calculate_cost(size, cartons))
                else:
                    p = pricing[size]
                    st.write(f"💧 {size.upper()}: ₹{p['carton_price']}/carton ({p['bottles']} bottles) — ₹{p['unit_price']}/bottle")
                found = True
                break
        if not found:
            st.write("💧 Our Pricing:\n\n"
                     "1L: ₹130/carton (12 bottles) — ₹10.83/bottle\n"
                     "500ml: ₹165/carton (24 bottles) — ₹6.80/bottle\n"
                     "300ml: ₹150/carton (24 bottles) — ₹5.00/bottle\n\n"
                     "Prices may vary based on order quantity.")
    
    else:
        st.info("🤖 Sorry, I don't have an answer for that yet. Try asking something about our products, pricing, or contact info.")


