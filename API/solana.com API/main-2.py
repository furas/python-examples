
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.19
#
# title: I would like to get all transactions given an address
# url: https://stackoverflow.com/questions/70028880/i-would-like-to-get-all-transactions-given-an-address

# [I would like to get all transactions given an address](https://stackoverflow.com/questions/70028880/i-would-like-to-get-all-transactions-given-an-address)


# https://michaelhly.github.io/solana-py/api.html

# https://docs.solana.com/clusters
# https://docs.solana.com/cluster/rpc-endpoints

from solana.rpc.api import Client

all_addresses = [
    ['2AQdpHJ2JpcEgPiATUXjQxA8QmafFegfQwSLWSprPicm', dict(before='89Tv9s2uMGaoxB8ZF1LV9nGa72GQ9RbkeyCDvfPviWesZ6ajZBFeHsTPfgwjGEnH7mpZa7jQBXAqjAfMrPirHt2')],
    ['Vote111111111111111111111111111111111111111', dict()],
    ['fake address', dict()]
]

#endpoint = 'https://api.devnet.solana.com'        # for `developing`
#endpoint = 'https://api.testnet.solana.com'       # for `testing`
endpoint = 'https://api.mainnet-beta.solana.com'   # real data
#endpoint = 'https://solana-api.projectserum.com'

solana_client = Client(endpoint)

for address, params in all_addresses:
    print('address:', address)
    print('params:', params)
    
    #result = solana_client.get_confirmed_signature_for_address2(address, limit=1)
    result = solana_client.get_signatures_for_address(address, **params)
    
    if 'result' in result:
        print('len:', len(result['result']))
        
        # `[:5]` to display only first 5 items
        for number, item in enumerate(result['result'][:5], 1):
            print(number, 'signature:', item['signature'])
            
        # check if there is "4SNQ4h1vL9GkmSnojQsf8SZyFvQsaq62RCgops2UXFYag1Jc4MoWrjTg2ELwMqM1tQbn9qUcNc4tqX19EGHBqC5u"
        for number, item in enumerate(result['result'], 1):
            if item['signature'].startswith('4SNQ'):
                print('found at', number, '>>>', item['signature'])
                
    else:
        # error
        print(result)

    print('---')

    #solana_client.get_account_info(address)
