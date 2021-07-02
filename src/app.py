import traceback
from logging import Logger
from slack_bolt import Ack, BoltResponse
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from api import slack_app
from env import SLACK_APP_TOKEN
from utils import create_notion_task, post_chat_message


@slack_app.command("/create_task")
def create_task(
    ack: Ack,
    body: BoltResponse,
    client: WebClient,
    logger: Logger
) -> None:
    title = body["text"]

    try:
        response = create_notion_task(
            channel_id=body["channel_id"],
            title=title,
        )
        task_url = response["url"]
        response_msg = f"Task added: {task_url}"
    except Exception as err:
        traceback.print_exc()
        logger.error(f"Error adding task: {err}")
        response_msg = f"Could not add a new task (check logs)."

    ack(response_msg)


@slack_app.command("/create_event")
def create_event(
    ack: Ack,
    body: BoltResponse,
    client: WebClient,
    logger: Logger
) -> None:
    ack()

    user_id = body["user_id"]
    title = body["text"]

    # client.views_open

    post_chat_message(
        client=client,
        logger=logger,
        channel=body["channel_id"],
        text=f"Create event for <@{user_id}> with title: '{title}'!"
    )


if __name__ == "__main__":
    SocketModeHandler(slack_app, SLACK_APP_TOKEN).start()
