from notion_client import Client as NotionClient
from slack_bolt import App

from env import NOTION_TOKEN, SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET


slack_app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
)

notion_client = NotionClient(auth=NOTION_TOKEN)