import streamlit as st
import re

st.set_page_config(page_title="Sipx Virtual Assistant", page_icon="💧")
st.title("💬 Sipx Virtual Assistant")

st.sidebar.title("Welcome to Sipx")
st.sidebar.info("Ask me about our products, pricing, certifications, and more!")

question = st.text_input("How can I help you today?")

# Bottle prices per unit
prices_per_bottle = {
    "1l": 10.83,
    "500ml": 6.80,
    "300ml": 5.00
}

def extract_number(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None

if question:
    question_lower = question.lower()

    if "price" in question_lower and "1l" in question_lower:
        st.write("""🧾 1 Litre Bottle:
- ₹130 per carton (12 bottles)
- ₹10.83 per bottle

📌 *Prices may vary depending on the quantity ordered.*""")

    elif "price" in question_lower and "500" in question_lower:
        st.write("""🧾 500ml Bottle:
- ₹165 per carton (24 bottles)
- ₹6.80 per bottle

📌 *Prices may vary depending on the quantity ordered.*""")

    elif "price" in question_lower and "300" in question_lower:
        st.write("""🧾 300ml Bottle:
- ₹150 per carton (24 bottles)
- ₹5.00 per bottle

📌 *Prices may vary depending on the quantity ordered.*""")

    elif "price" in question_lower or "cost" in question_lower:
        st.write("""💧 Our Pricing (may vary by quantity):

- **1L:** ₹130/carton (12 bottles) — ₹10.83/bottle
- **500ml:** ₹165/carton (24 bottles) — ₹6.80/bottle
- **300ml:** ₹150/carton (24 bottles) — ₹5.00/bottle

📞 For bulk orders, contact: +91 8309620108""")

    elif "contact" in question_lower:
        st.write("""📞 You can contact Sipx at:

- Phone: +91 8309620108
- Email: sipxofficial@gmail.com""")

    elif "certificates" in question_lower or "report" in question_lower:
        st.write("""📄 We provide NABL, ISI, ISO, FSSAI certificates along with monthly, quarterly, and annual BIS lab reports.""")

    elif "composition" in question_lower or "minerals" in question_lower:
        st.write("""🧪 Our water includes:
- Magnesium – Strength & Energy
- Sulfate – Detox & Digestion
- Potassium – Heart & Hydration
- Bicarbonate – pH Balance
- Calcium – Bone & Teeth Strength
- Chloride – Fluid Balance""")

    elif "what is sipx" in question_lower or "who are you" in question_lower:
        st.write("""💧 Sipx is a premium packaged drinking water brand dedicated to delivering clean, safe, and sustainable hydration. We don’t just sell water — we deliver trust, health, and care in every bottle.""")

    elif "mission" in question_lower or "vision" in question_lower:
        st.write("""🌍 Our mission is to bring pure, life-changing water to every individual. Every Sipx bottle supports health, sustainability, and community upliftment.""")

    elif "values" in question_lower or "goal" in question_lower:
        st.write("""❤️ At Sipx, we value purity, sustainability, and community impact. Our water is 100% safe, our packaging is recyclable, and our mission is rooted in social good.""")

    elif "sustainability" in question_lower or "eco" in question_lower:
        st.write("""♻️ We use 100% recyclable packaging and support waste management and drought-relief efforts. Every bottle contributes to a greener planet.""")

    elif "technology" in question_lower or "how is your water purified" in question_lower:
        st.write("""⚙️ We combine advanced hydration technology with strict purification methods to ensure every drop meets the highest safety and mineral standards.""")

    elif "impact" in question_lower or "what change do you make" in question_lower:
        st.write("""💧 Sipx supports clean water initiatives, drought relief projects, and community donations — turning every purchase into a ripple of hope.""")

    elif "where are you located" in question_lower or "location" in question_lower:
        st.write("""📍 We are based in India and serve various regions, especially those affected by water scarcity. Contact us at +91 8309620108 for orders or collaborations.""")

    elif "order" in question_lower and "5" in question_lower and "1l" in question_lower:
        st.write("""🧾 5 Cartons of 1L Bottles:
- ₹130 × 5 = ₹650
- 60 bottles total (12 per carton)

📌 *Confirm final pricing and delivery with Sipx.*""")

    elif "cost" in question_lower and "60" in question_lower and "1l" in question_lower:
        st.write("""🧾 60 × 1L Bottles = ₹649.80 (₹10.83 each)
📦 Equals 5 cartons

📌 *Prices may vary slightly with bulk orders.*""")

    elif any(x in question_lower for x in ["cost of", "price of", "total for"]) and any(x in question_lower for x in ["bottle", "carton", "bottles", "cartons"]):
        amount = extract_number(question_lower)
        if "1l" in question_lower:
            total = round(amount * prices_per_bottle["1l"], 2)
            st.write(f"🧾 {amount} × 1L bottles = ₹{total}")
        elif "500" in question_lower:
            total = round(amount * prices_per_bottle["500ml"], 2)
            st.write(f"🧾 {amount} × 500ml bottles = ₹{total}")
        elif "300" in question_lower:
            total = round(amount * prices_per_bottle["300ml"], 2)
            st.write(f"🧾 {amount} × 300ml bottles = ₹{total}")
        else:
            st.warning("⚠️ Please mention bottle size (1L / 500ml / 300ml) to calculate cost.")

    elif "how many" in question_lower and "for ₹" in question_lower:
        amount = extract_number(question_lower)
        if "1l" in question_lower:
            count = int(amount / prices_per_bottle["1l"])
            st.write(f"💧 For ₹{amount}, you can get approximately {count} × 1L bottles.")
        elif "500" in question_lower:
            count = int(amount / prices_per_bottle["500ml"])
            st.write(f"💧 For ₹{amount}, you can get approximately {count} × 500ml bottles.")
        elif "300" in question_lower:
            count = int(amount / prices_per_bottle["300ml"])
            st.write(f"💧 For ₹{amount}, you can get approximately {count} × 300ml bottles.")
        else:
            st.warning("⚠️ Please mention bottle size (1L / 500ml / 300ml) to calculate quantity.")

    else:
        st.warning("🤖 Sorry, I don't have an answer for that yet. Try asking about our bottles, prices, or contact info.")
