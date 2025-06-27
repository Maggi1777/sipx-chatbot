import streamlit as st

st.set_page_config(page_title="Sipx Assistant", page_icon="💧")

# Basic user info
with st.sidebar:
    st.title("💬 Sipx Virtual Assistant")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    st.markdown("---")
    st.info("Get instant answers about Sipx water bottles, services, and contact details.")

# Show welcome message
if name and email:
    st.success(f"Hi {name}! Ask me anything about Sipx 💧")

    # Q&A logic
    question = st.text_input("Type your question here")

    if question:
        # Basic hardcoded Q&A
        question_lower = question.lower()
        if "price" in question_lower and "500" in question_lower:
            st.write("💧 The 500ml bottle price is not listed online. Please contact us at +91 8309620108 for pricing.")
        elif "sizes" in question_lower:
            st.write("📦 We offer three sizes: 1L, 500ml, and 300ml.")
        elif "contact" in question_lower:
            st.write("""📞 You can contact Sipx at:
        - Phone: +91 8309620108
        - Email: sipxofficial@gmail.com
        """)        
        elif "certificate" in question_lower:
            st.write("✅ We hold NABL, ISI, ISO, FSSAI & BIS certifications.")
        elif "about" in question_lower or "mission" in question_lower:
            st.write("🌍 Sipx delivers clean, safe water with a mission of trust, health, and sustainability.")
        else:
            st.warning("🤖 Sorry, I don't have an answer for that yet. Try asking something about our products, contact info, or certifications.")
else:
    st.warning("Please enter your name and email to begin chatting.")
