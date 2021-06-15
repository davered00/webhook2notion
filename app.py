
import os
# from notion.client import NotionClient
# from notion.block import TextBlock
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# def createNotionTask(token, collectionURL, title, content):
#     # notion
#     client = NotionClient(token)
#     cv = client.get_collection_view(collectionURL)
#     row = cv.collection.add_row()
#     row.title = title
#     row.children.add_new(TextBlock,title=content)


# @app.route('/create_todo', methods=['GET'])
# def create_todo():

#     title = request.args.get('title')
#     content = request.args.get('content')
#     token_v2 = os.environ.get("TOKEN")
#     url = os.environ.get("URL")
#     createNotionTask(token_v2, url, title, content)
#     return f'added {title} to Notion'


def post_chat_message(
    client: app.client,
    logger: app.logger,
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


@app.command("/create_task")
def create_task(
    ack,
    body: dict[str, str],
    client: app.client,
    logger: app.logger
) -> None:
    ack()

    user_id = body["user_id"]
    description = body["text"]

    post_chat_message(
        client=client,
        logger=logger,
        channel=body["channel_id"],
        text=f"Create event for <@{user_id}> with title: '{description}'!"
    )


@app.command("/create_event")
def create_event(
    ack,
    body: dict[str, str],
    client: app.client,
    logger: app.logger
) -> None:
    ack()

    user_id = body["user_id"]
    title = body["text"]

    post_chat_message(
        client=client,
        logger=logger,
        channel=body["channel_id"],
        text=f"Create event for <@{user_id}> with title: '{title}'!"
    )


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
