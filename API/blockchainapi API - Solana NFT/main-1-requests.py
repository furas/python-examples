# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.21
# [blockchain - Get solana NFT on-chain data using python - Stack Overflow](https://stackoverflow.com/questions/71195145/get-solana-nft-on-chain-data-using-python/71199682#71199682)


# not all portals may have some NTFs
#
# https://explorer.solana.com/address/{mint_address}
# https://solanart.io/nft/{mint_address}
# https://hyperspace.xyz/collections/{mint_address}
# https://solsea.io/nft/{mint_address}


import requests
import pprint

headers = {
    'APIKeyId': 'API_KEY_ID',
    'APISecretKey': 'API_SECRET_KEY',
}

network = 'mainnet-beta'
mint_address = 'AC6JJcepC9hZzHGVDmx5F3LSGeRhdok1VkcLSZsHoy26'

url = f"https://api.blockchainapi.com/v1/solana/nft/{network}/{mint_address}"
response = requests.get(url, headers=headers)
data = response.json() 

pprint.pprint(data)

