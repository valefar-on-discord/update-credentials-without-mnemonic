import json
import sys

from verify_deposit_signature import verify_deposit_signature
from verify_keystore_signature import validate_bls_to_execution_change_keystore

validator_file = "./unset_validators.json"

def verify_json(json_file):
    try:
        with open(validator_file, 'r') as f:
            validators = json.load(f)

        with open(json_file, 'r') as f:
            data = json.load(f)

        # grab contents from signature file
        to_execution_address = data.get("to_execution_address")
        validator_index = data.get("validator_index")
        deposit_signature = data.get("deposit_signature")
        keystore_signature = data.get("keystore_signature")

        # search for validator by index and grab contents
        validator_data = next(filter(lambda item: item.get("index") == validator_index, validators), None)

        if validator_data == None:
            print(f"Unable to find validator of index {validator_index}")
            return False

        deposit_address = validator_data.get("deposit_address")
        validator_pubkey = validator_data.get("pubkey")


        valid_deposit_signature = verify_deposit_signature(
            message=f'{{"to_execution_address":"{to_execution_address}","validator_index":{validator_index}}}',
            signature=deposit_signature,
            signer_address=deposit_address
        )

        if not valid_deposit_signature:
            print("Invalid deposit signature")
            return False


        valid_keystore_signature = validate_bls_to_execution_change_keystore(
          validator_index=validator_index,
          to_execution_address=to_execution_address,
          signature=keystore_signature,
          pubkey=validator_pubkey
        )

        if not valid_keystore_signature:
            print("Invalid keystore signature")
            return False

        print("Valid signatures")
        return True
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    json_file = sys.argv[1]
    if verify_json(json_file):
        sys.exit(0)
    else:
        sys.exit(1)
