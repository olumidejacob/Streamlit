import streamlit as st

st.set_page_config(page_title="MyBank App", layout="centered", initial_sidebar_state="expanded")


st.markdown("""
    <style>
    .main-header {
        font-size: 3.5em;
        color: #4CAF50; /* A nice green */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .subheader {
        font-size: 1.8em;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
    }
    .stPageLink {
        border-radius: 10px;
        padding: 15px 25px;
        margin: 10px auto;
        display: block;
        width: fit-content;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
    }
    .stPageLink:hover {
        transform: translateY(-5px);
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🏦 Welcome to MyBank</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Your trusted partner for financial growth.</p>", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1579621970563-ed028cac7b77?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
         caption="Secure and Convenient Banking", use_column_width=True)

st.subheader("Choose an account type to proceed:")

# Use columns for better layout of page links
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.page_link(page="pages/current_account_page.py", label="Current Account", icon="💼", use_container_width=True)
    st.page_link(page="pages/savings_account_page.py", label="Savings Account", icon="💰", use_container_width=True)
    st.page_link(page="pages/loan_application_page.py", label="Apply for a Loan", icon="💸", use_container_width=True)
    st.page_link(page="pages/contact_us_page.py", label="Contact Us", icon="📞", use_container_width=True)

st.sidebar.title("Quick Actions")
if st.sidebar.button("Home"):
    st.session_state.current_page = "home" # A hypothetical way to navigate back if we were using state for page management

st.sidebar.info("🚀 New Feature: Check out our financial calculators in the 'Tools' section!")

# Footer
st.markdown("---")
st.markdown("© 2025 MyBank. All rights reserved.")
