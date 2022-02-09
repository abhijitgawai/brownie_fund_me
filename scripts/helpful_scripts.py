from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


DECIMALS=18
STARTING_PRICE = 2000                                                       # in deploy_mocks() function used for constructor values of MockV3Aggregator

def get_account():
    if network.show_active()  in LOCAL_BLOCKCHAIN_ENVIRONMENTS:                              # Devlopment enviormnet will use ganache accounts
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])                  # For real networks we will use our real wallet (test wallet)


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from":get_account()})           # passing constructor values , from account to MockV3Aggregator.sol  //toWei adds 18 decimals
    price_feed_address = MockV3Aggregator[-1].address                                     # Getting lattest MockV3Aggregator address
    print("Mocks Deployed")