import streamlit as st
import secrets
import string


# 1. Function to generate realistic random addresses
def generate_address(crypto_name):
    if "Bitcoin" in crypto_name:
        # BTC Native Segwit addresses start with bc1q
        chars = string.ascii_lowercase + string.digits
        random_str = ''.join(secrets.choice(chars) for _ in range(38))
        return f"bc1q{random_str}"

    elif "Ethereum" in crypto_name or "USDC" in crypto_name:
        # ETH/ERC-20 addresses start with 0x and have 40 hex characters
        return f"0x{secrets.token_hex(20)}"

    elif "Solana" in crypto_name:
        # Solana uses base58 characters (no 0, O, I, or l)
        base58_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        return ''.join(secrets.choice(base58_chars) for _ in range(44))

    return "Unknown Address format"


# 2. Setup user session state
# This ensures that once a user is assigned an address, it doesn't change
# while they are using the app.
if 'user_wallets' not in st.session_state:
    st.session_state.user_wallets = {}

st.title("Bang Wallet")
st.write("Select an asset below to reveal your unique receive address.")

# 3. Dropdown Menu
crypto_options = ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "USDC (ERC-20)"]

selected_crypto = st.selectbox(
    "Choose Cryptocurrency:",
    options=crypto_options,
    index=None,
    placeholder="Select a token..."
)

# 4. Generate and display the address
if selected_crypto:
    # If this user hasn't generated this specific crypto address yet, create one
    if selected_crypto not in st.session_state.user_wallets:
        st.session_state.user_wallets[selected_crypto] = generate_address(selected_crypto)

    # Retrieve the user's specific address from their session
    user_address = st.session_state.user_wallets[selected_crypto]

    st.success(f"**Your {selected_crypto} Receive Address:**")
    st.code(user_address, language="text")