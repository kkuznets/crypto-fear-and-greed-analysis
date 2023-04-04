from prefect import flow, get_run_logger
from platform import node, platform


@flow
def test_flow(user_input: str = "World"):
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 🚀", user_input)
    logger.info("Network: %s. Instance: %s. Agent is healthy ✅️", node(), platform())


if __name__ == "__main__":
    test_flow()
