import streamlit as st

# Configure the web page
st.set_page_config(page_title="Demo Bank Portal", page_icon="🏦", layout="centered")

# Predefined demo user database
USER_DATABASE = {
    "demouser": {
        "password": "password123",
        "full_name": "Demo User",
        "account_num": "1234-5678-9012",
        "balance": 0.00
    }
}

# Keep track of login state so it remembers between clicks
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# --- SCREEN 1: LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("🔒 Demo Login Portal")
    st.info("💡 Try logging in with:\n\n**User ID:** demouser | **Password:** password123")
    
    username_input = st.text_input("Enter User ID")
    password_input = st.text_input("Enter Password", type="password")
    
    if st.button("Login"):
        if username_input in USER_DATABASE and USER_DATABASE[username_input]["password"] == password_input:
            st.session_state.logged_in = True
            st.session_state.username = username_input
            st.rerun()
        else:
            st.error("❌ Invalid credentials. Please try again.")

# --- SCREEN 2: BANK DASHBOARD ---
else:
    user_data = USER_DATABASE[st.session_state.username]
    
    st.title(f"🏦 WELCOME TO DEMO BANK, {user_data['full_name'].upper()}!")
    st.divider()
    
    # Display details cleanly
    st.markdown(f"**Account Holder:** {user_data['full_name']}")
    st.markdown(f"**Account Number:** {user_data['account_num']}")
    
    # Balance highlight
    st.metric(label="AVAILABLE BALANCE", value=f"${user_data['balance']:.2f}")
    
    st.divider()
    
    # Fake action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("Deposit Funds", disabled=True)
    with col2:
        st.button("Transfer", disabled=True)
    with col3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()
