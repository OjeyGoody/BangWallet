import tkinter as tk
from tkinter import ttk

# Dictionary storing public receive addresses for your wallet
WALLET_ADDRESSES = {
    "Bitcoin (BTC)": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
    "Ethereum (ETH)": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
    "Solana (SOL)": "HN7cABqLq46Es1jh92dQQisAq662SmxELLLsHHe4YWrH",
    "USDC (ERC-20)": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
}


def show_receive_address(event):
    """Updates the label with the address of the selected cryptocurrency."""
    selected_crypto = dropdown.get()
    address = WALLET_ADDRESSES.get(selected_crypto, "Address not found")

    # Update the text on the screen
    address_label.config(text=f"{selected_crypto} Receive Address:\n\n{address}")


# 1. Set up the main application window
root = tk.Tk()
root.title("Receive Crypto")
root.geometry("450x250")

# 2. Create UI instructions
instruction_label = tk.Label(root, text="Select an asset to receive funds:", font=("Arial", 12))
instruction_label.pack(pady=20)

# 3. Create the Dropdown (Combobox)
dropdown = ttk.Combobox(root, values=list(WALLET_ADDRESSES.keys()), state="readonly", width=35)
dropdown.set("Click to select cryptocurrency...")
dropdown.pack(pady=5)

# Trigger the 'show_receive_address' function whenever the dropdown value changes
dropdown.bind("<<ComboboxSelected>>", show_receive_address)

# 4. Create the area where the wallet address will appear
address_label = tk.Label(root, text="Waiting for selection...", font=("Consolas", 10, "bold"), fg="darkgreen")
address_label.pack(pady=30)

# 5. Run the application
if __name__ == "__main__":
    root.mainloop()