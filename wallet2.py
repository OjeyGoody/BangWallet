WALLET_ADDRESSES = {
    "1": {"name": "Bitcoin (BTC)", "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"},
    "2": {"name": "Ethereum (ETH)", "address": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"},
    "3": {"name": "Solana (SOL)", "address": "HN7cABqLq46Es1jh92dQQisAq662SmxELLLsHHe4YWrH"},
    "4": {"name": "USDC (ERC-20)", "address": "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"}
}


def clear_screen():
    print("\n" * 50)


while True:
    clear_screen()
    print("=== CRYPTO WALLET RECEIVE ===")
    print("Select an asset to receive funds:\n")

    # Print the "dropdown" menu options
    for key, data in WALLET_ADDRESSES.items():
        print(f"[{key}] {data['name']}")
    print("[Q] Quit")

    print("-" * 30)
    choice = input("Enter a number: ").strip().upper()

    if choice == 'Q':
        print("Exiting wallet...")
        break

    if choice in WALLET_ADDRESSES:
        selection = WALLET_ADDRESSES[choice]
        print(f"\n✅ {selection['name']} Receive Address:")
        print(f"--> {selection['address']}")

        input("\nPress Enter to return to the main menu...")
    else:
        input("\nInvalid selection. Press Enter to try again...")