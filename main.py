from hive_agent import HiveAgent
from tools.news_search import fetch_latest_news

from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    my_agent = HiveAgent(
        name="General Purpose Agent",
        functions=[fetch_latest_news],
        config_path="./hive_config.toml",
        instruction="Use appropriate news sources to answer the questions.",
    )

    my_agent.run()
