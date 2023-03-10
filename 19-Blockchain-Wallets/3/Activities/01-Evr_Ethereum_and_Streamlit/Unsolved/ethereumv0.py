# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
################################################################################

# Create a function called `generate_account` that automates the Ethereum
def generate_account(w3):
    # account creation process
    # Access the mnemonic phrase from the `.env` file
    mnemonic = os.getenv("MNEMONIC")
    
    # Create Wallet object instance
    wallet = Wallet(mnemonic)
    
    # Derive Ethereum private key
    private, public = wallet.derive_account('eth')
    
    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)
    
    # Return the account from the function
    return account