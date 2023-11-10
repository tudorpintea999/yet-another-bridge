import os

ETH_RPC_URL = 'https://goerli.nodeguardians.io'
SN_RPC_URL = os.getenv('SN_RPC_URL')

ETH_CONTRACT_ADDR = os.getenv('ETH_CONTRACT_ADDR')
SN_CONTRACT_ADDR = os.getenv('SN_CONTRACT_ADDR')

ETH_PRIVATE_KEY = os.getenv('ETH_PRIVATE_KEY')
SN_WALLET_ADDR = os.getenv('SN_WALLET_ADDR')
SN_PRIVATE_KEY = os.getenv('SN_PRIVATE_KEY')

HERODOTUS_API_KEY = os.getenv('HERODOTUS_API_KEY')
HERODOTUS_ORIGIN_CHAIN = '5'
HERODOTUS_DESTINATION_CHAIN = 'SN_GOERLI'

MAX_RETRIES = 30
RETRIES_DELAY = 30 # 30 seconds, 30 tries within 15 minutes
