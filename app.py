import streamlit as st
import re

st.set_page_config(page_title="Sipx Virtual Assistant", page_icon="💧")
st.title("💬 Sipx Virtual Assistant")

# Sidebar for user details
with st.sidebar:
    st.title("Welcome to Sipx 💧")
    st.subheader("Please enter your details")

    user_name = st.text_input("👤 Your Name")
    user_email = st.text_input("📧 Your Email")

    if user_name and user_email:
        st.success(f"Welcome, {user_name}!")
    else:
        st.warning("Please fill out your name and email to begin.")

# Pricing and quantities
prices_per_bottle = {
    "1l": 10.83,
    "500ml": 6.80,
    "300ml": 5.00
}

prices_per_carton = {
    "1l": 130,      # 12 bottles
    "500ml": 165,   # 24 bottles
    "300ml": 150    # 24 bottles
}

bottles_per_carton = {
    "1l": 12,
    "500ml": 24,
    "300ml": 24
}

def extract_number(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None

if user_name and user_email:
    question = st.text_input("How can I help you today?")

    if question:
        question_lower = question.lower()

        if "price" in question_lower and "1l" in question_lower:
            st.write("🧾 1L Bottle: ₹130 per carton (12 bottles) — ₹10.83 each")

        elif "price" in question_lower and "500" in question_lower:
            st.write("🧾 500ml Bottle: ₹165 per carton (24 bottles) — ₹6.80 each")

        elif "price" in question_lower and "300" in question_lower:
            st.write("🧾 300ml Bottle: ₹150 per carton (24 bottles) — ₹5.00 each")

        elif "price" in question_lower or "cost" in question_lower:
            st.write("""💧 Our Pricing:

- 1L: ₹130/carton (12) — ₹10.83/bottle  
- 500ml: ₹165/carton (24) — ₹6.80/bottle  
- 300ml: ₹150/carton (24) — ₹5.00/bottle""")

        elif "contact" in question_lower:
            st.write("""📞 You can contact Sipx at:

- Phone: +91 8309620108  
- Email: sipxofficial@gmail.com""")

        elif "certificate" in question_lower or "report" in question_lower:
            st.write("📄 We offer NABL, ISI, ISO, FSSAI certificates, and BIS lab reports (monthly, quarterly, annually).")

        elif "composition" in question_lower or "minerals" in question_lower:
            st.write("""🧪 Water Composition:
- Magnesium – Strength & Energy  
- Sulfate – Detox & Digestion  
- Potassium – Heart & Hydration  
- Bicarbonate – pH Balance  
- Calcium – Bone Strength  
- Chloride – Fluid Balance""")

        elif "what is sipx" in question_lower or "who are you" in question_lower:
            st.write("""💧 Sipx is a premium packaged drinking water brand. We deliver safe, clean, and sustainable hydration with every bottle. Our mission is to make clean water a basic right for everyone.""")

        elif "sustainability" in question_lower or "eco" in question_lower:
            st.write("♻️ Our packaging is 100% recyclable. We support waste management and drought relief efforts.")

        elif "mission" in question_lower or "goal" in question_lower:
            st.write("🌍 Our mission: bring pure, life-changing water to everyone. Every Sipx bottle fuels health and hope.")

        # 👉 Carton Calculation
        elif "carton" in question_lower and "cost" in question_lower or "price" in question_lower:
            amount = extract_number(question_lower)
            if amount:
                if "1l" in question_lower:
                    total = prices_per_carton["1l"] * amount
                    st.write(f"🧾 {amount} × 1L cartons = ₹{total} ({amount * bottles_per_carton['1l']} bottles)")
                elif "500" in question_lower:
                    total = prices_per_carton["500ml"] * amount
                    st.write(f"🧾 {amount} × 500ml cartons = ₹{total} ({amount * bottles_per_carton['500ml']} bottles)")
                elif "300" in question_lower:
                    total = prices_per_carton["300ml"] * amount
                    st.write(f"🧾 {amount} × 300ml cartons = ₹{total} ({amount * bottles_per_carton['300ml']} bottles)")
                else:
                    st.warning("Mention size (1L, 500ml, 300ml) to calculate carton cost.")
            else:
                st.warning("Couldn’t find number of cartons.")

        # 👉 Bottle Quantity Cost
        elif any(x in question_lower for x in ["cost of", "price of", "total for", "how much for", "how many"]) and any(x in question_lower for x in ["bottle", "carton", "bottles", "cartons", "₹", "rs"]):
            amount = extract_number(question_lower)

            if amount:
                if "1l" in question_lower or "1 l" in question_lower:
                    if "₹" in question_lower or "rs" in question_lower:
                        count = int(amount / prices_per_bottle["1l"])
                        st.write(f"💧 For ₹{amount}, you get approx **{count} × 1L bottles**.")
                    else:
                        total = round(amount * prices_per_bottle["1l"], 2)
                        st.write(f"🧾 {amount} × 1L bottles = ₹{total}")
                elif "500" in question_lower:
                    if "₹" in question_lower or "rs" in question_lower:
                        count = int(amount / prices_per_bottle["500ml"])
                        st.write(f"💧 For ₹{amount}, you get approx **{count} × 500ml bottles**.")
                    else:
                        total = round(amount * prices_per_bottle["500ml"], 2)
                        st.write(f"🧾 {amount} × 500ml bottles = ₹{total}")
                elif "300" in question_lower:
                    if "₹" in question_lower or "rs" in question_lower:
                        count = int(amount / prices_per_bottle["300ml"])
                        st.write(f"💧 For ₹{amount}, you get approx **{count} × 300ml bottles**.")
                    else:
                        total = round(amount * prices_per_bottle["300ml"], 2)
                        st.write(f"🧾 {amount} × 300ml bottles = ₹{total}")
                else:
                    st.warning("⚠️ Please mention bottle size (1L / 500ml / 300ml).")
            else:
                st.warning("⚠️ Couldn’t detect a valid number in your question.")

        else:
            st.warning("🤖 Sorry, I don't have an answer for that yet. Try asking about pricing, bottles, or contact info.")

else:
    st.info("Please enter your name and email to start chatting.")
