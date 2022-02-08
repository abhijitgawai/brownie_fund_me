from brownie import network, config, accounts

def get_account():
    if network.show_active() == "development":                              # Devlopment enviormnet will use ganache accounts
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])                  # For real networks we will use our real wallet (test wallet)