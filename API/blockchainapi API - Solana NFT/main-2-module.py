# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.21
# [blockchain - Get solana NFT on-chain data using python - Stack Overflow](https://stackoverflow.com/questions/71195145/get-solana-nft-on-chain-data-using-python/71199682#71199682)


# not all portals may have some NTFs
#
# https://explorer.solana.com/address/{mint_address}
# https://solanart.io/nft/{mint_address}
# https://hyperspace.xyz/collections/{mint_address}
# https://solsea.io/nft/{mint_address}


from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork
import pprint

BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id='MY_API_KEY_ID',
    api_secret_key='MY_SECRET_KEY'
)

nft_address = 'AC6JJcepC9hZzHGVDmx5F3LSGeRhdok1VkcLSZsHoy26'

nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
    mint_address=nft_address,
    network=SolanaNetwork.MAINNET_BETA
)

pprint.pprint(nft_metadata)

