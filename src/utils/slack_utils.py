from logging import Logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def post_chat_message(
    client: WebClient,
    logger: Logger,
    channel: str,
    text: str
) -> None:
    try:
        result = client.chat_postMessage(
            channel=channel,
            text=text
        )
        logger.info(result)
    except SlackApiError as err:
        logger.error(f"Error posting message: {err}")