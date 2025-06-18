import streamlit as st
from current_account import CurrentAccount

if 'account' not in st.session_state:
    st.session_state.account = CurrentAccount(balance=10000)
if 'msg' not in st.session_state:
    st.session_state.msg = ""
if 'msg_type' not in st.session_state:
    st.session_state.msg_type = ""

st.set_page_config(page_title="Current Account", layout="centered")
st.title("Current Account")

# Show message at the top
if st.session_state.msg:
    if st.session_state.msg_type == "success":
        st.success(st.session_state.msg)
    elif st.session_state.msg_type == "error":
        st.error(st.session_state.msg)
    st.session_state.msg = ""
    st.session_state.msg_type = ""

balance_placeholder = st.empty()
balance_placeholder.subheader(f"Balance: ₦{st.session_state.account.balance}")

with st.form("current_account_form"):
    amount = st.number_input("Enter amount", min_value=1000, step=100)
    operations = st.selectbox("Deposit or withdraw", ("Deposit", "Withdraw"))
    submit = st.form_submit_button("Submit")

    if submit:
        try:
            if operations == "Deposit":
                st.session_state.account.deposit(amount)
                st.session_state.msg = f"✅Deposit of ₦{amount} successful!"
                st.session_state.msg_type = "success"
            elif operations == "Withdraw":
                if amount > st.session_state.account.balance:
                    st.session_state.msg = f"❌Error: Insufficient Funds"
                    st.session_state.msg_type = "error"
                else:
                    st.session_state.account.withdraw(amount)
                    st.session_state.msg = f"✅Withdrawal of ₦{amount} successful!"
                    st.session_state.msg_type = "success"
            st.rerun()
        except ValueError as e:
            st.session_state.msg = f"An error occurred: {e}"
            st.session_state.msg_type = "error"
            st.rerun
