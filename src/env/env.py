from os import environ


NOTION_TOKEN = environ.get("NOTION_TOKEN")

SLACK_APP_TOKEN = environ.get("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = environ.get("SLACK_SIGNING_SECRET")