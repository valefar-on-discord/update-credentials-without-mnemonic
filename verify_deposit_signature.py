from web3 import Web3
from eth_account.messages import encode_defunct
from eth_account import Account

def verify_deposit_signature(message: str,
                             signature: str,
                             signer_address:str) -> bool:
    message_encoded = encode_defunct(text=message)

    recovered_address = Account.recover_message(message_encoded, signature=signature)

    return Web3.to_checksum_address(recovered_address) == Web3.to_checksum_address(signer_address)

