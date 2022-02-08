from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address

    # if we are on a persistant network(rinkeby), use the associated address(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e)
    # otherwise, deploy mocks (fake priceFeed)
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True
    )
    print(f"Contract deployed to {fund_me.address}")
    # return fund_me
    # fund_me  = FundMe.deploy({"from":account}, publish_source=True)         # To publish on etherscan
    # print(f"Contract deployed to {fund_me.address}")

def main():
    deploy_fund_me()