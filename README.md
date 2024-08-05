# update-credentials-without-mnemonic
Validator claiming process to update withdrawal credentials without mnemonic

## Create Keystore signature

- Grab [bls_change_with_keystore branch](https://github.com/valefar-on-discord/ethstaker-deposit-cli/tree/bls_change_with_keystore)
- Follow setup instructions
- Run `generate-bls-to-execution-change-keystore`
- This will output a `bls_to_execution_change_keystore_transaction-*-*.json` file in the `bls_to_execution_changes_keystore` directory
- You will need the `signature` value later


## Create Deposit signature

- Go to [Etherscan Verified Signatures](https://etherscan.io/verifiedSignatures)
- Click on `Sign Message`
- Make sure to select the account you originally deposited from
- For message, provider a version similar to `Signature message format` described below
- You will need the `Signature Hash` value


## Create signature json file

- After creating signatures, create a json file using the validator index as the name such as `5426.json`
- Put this file in the `signatures` folder
- Review the `Signature file format` section below for the contents of the file
- Create a pull request where the signatures will be manually verified


## Keystore file format
```
{
  "message": {
    "to_execution_address": "${to_execution_address}",
    "validator_index": ${validator_index}
  },
  "signature": "${keystore_signature}"
}
```

As an example:

```
{
    "message": {
      "to_execution_address": "0xcd60a5f152724480c3a95e4ff4daceef4074854d",
      "validator_index": 1
    },
    "signature": "0xa1ec43ffefc87d8a55749d98bcac87f2cb8e2969fdf12131eb171ffd49b46046c1c7ca1e22d6da7074d6303780aa17cc0af875536170bda53029450e4ad21e16a3a9b69d540a1e35313d637010c1ab3b3e43511162721c78e7fb382d682ad622"
}
```


## Signature message format
```
{"to_execution_address":"${to_execution_address}","validator_index":${validator_index}}
```

As an example:

```
{"to_execution_address":"0xcd60A5f152724480c3a95E4Ff4dacEEf4074854d","validator_index":1}
```


## Signature file format
```
{
  "to_execution_address": "${to_execution_address}",
  "validator_index": ${validator_index},
  "deposit_signature": "${deposit_signature}",
  "keystore_signature": "${keystore_signature}"
}
```

As an example:

```
{
  "to_execution_address": "0xcd60A5f152724480c3a95E4Ff4dacEEf4074854d",
  "validator_index": 1,
  "deposit_signature": "0x5c60eeb5e2f03c4e740c646f356e2940321e559e83339b6b344d9a40f8dbe520552dd51470dc30f805520bbb59a54dded024b6fdbde1ec7dcc08909e4233f5b41c",
  "keystore_signature": "0xa1ec43ffefc87d8a55749d98bcac87f2cb8e2969fdf12131eb171ffd49b46046c1c7ca1e22d6da7074d6303780aa17cc0af875536170bda53029450e4ad21e16a3a9b69d540a1e35313d637010c1ab3b3e43511162721c78e7fb382d682ad622"
}
```
