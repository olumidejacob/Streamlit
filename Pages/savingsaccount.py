import streamlit as st
from SavingsAccount import SavingsAccount
from Account import Account


def main():
    st.set_page_config(page_title="Savings Account", layout="centered")

    st.title("🏦 Savings Account")
    choice = st.selectbox("would you like to", ["Deposit", "Withdraw"])
    name = st.text_input("Enter Account Holder Name", "")
    amount = st.number_input("Enter amount", min_value=0, step=100)
    st.subheader(f"Welcome, {name}")

    if "msg" in st.session_state and st.session_state.msg:
        msg, msg_type = st.session_state.msg
        if msg_type == "success":
            st.success(msg)
        elif msg_type == "error":
            st.error(msg)
        st.session_state.msg = None  # Clear message after displaying

    # Initialize account in session state
    if "account" not in st.session_state or st.session_state.get("account_name") != name:
        st.session_state.account = SavingsAccount(0, 50000)
        st.session_state.account_name = name

    account = st.session_state.account

    balance_placeholder = st.empty()
    balance_placeholder.subheader(f"Balance: ${st.session_state.account.balance}")

    if st.button("Submit Transactions"):
        if choice == "Deposit":
            account.deposit(amount)
            st.session_state.msg = (f"Deposited ${amount:.2f} in your account", "success")
        elif choice == "Withdraw":
            # Check for withdrawal limit and balance separately
            if amount > getattr(account, 'withdrawal_limit', float('inf')):
                st.session_state.msg = (
                    f"❌ Withdrawal failed: Amount exceeds max withdrawal limit (${account.withdrawal_limit}).",
                    "error"
                )
            elif amount > account.balance:
                st.session_state.msg = (
                    f"❌ Withdrawal failed: Insufficient balance.",
                    "error"
                )
            else:
                success = account.withdraw(amount)
                if success:
                    st.session_state.msg = (f"Withdrew ${amount:.2f} from your account", "success")
                else:
                    st.session_state.msg = (
                        f"❌ Withdrawal failed: Unknown error.",
                        "error"
                    )
        st.rerun()

if __name__ == "_main_":
    main()
