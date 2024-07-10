from hive_agent import HiveAgent
from tools.news_search import fetch_latest_news
from tools.txn_search import get_transaction_receipt

from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    my_agent = HiveAgent(
        name="General Purpose Agent",
        functions=[fetch_latest_news, get_transaction_receipt],
        config_path="./hive_config.toml",
        instruction="Use appropriate tools to answer the questions.",
    )

    my_agent.run()
