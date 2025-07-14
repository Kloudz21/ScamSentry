
import streamlit as st

# Title and robot image
st.title("🤖 Scam Detector AI")
st.image("Sentry.png", caption="ScamSentry, Your AI Assistant To Counter Scams!")

# Input message
message = st.text_input("Paste your message here for safety verification:")

# Keyword list
scam_keywords = [
    "win money", "click here", "password", "urgent",
    "free iphone", "credit card", "act now",
    "login", "verify", "limited offer", "bank", "lottery", "free money", 
    "free robux", "robux", "iphone", "free", "claim your free prize", 
    "please give us your OTP", "we have sent you an OTP", "claim your prize now", 
]

# Check button
if st.button("Scan Message"):
    is_scam = any(word in message.lower() for word in scam_keywords)

    if is_scam:
        st.error("⚠️ Warning: This message might be a scam!")
    else:
        st.success("✅ This message looks safe!")
