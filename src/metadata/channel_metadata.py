
from typing import TypedDict


class ChannelMetadata(TypedDict):
    # Readable identifier for this channel
    name: str
    # Database ID to add tasks to when `create_task` is run in this channel.
    # NOTE:
    # - Get from URL: https://www.notion.so/nnjdsa/<DATABASE_ID>?v=<VIEW_ID>
    # - Page must be shared with the "DSA Slackbot" integration in Notion
    #   via the Share button in the top-right
    notion_task_db_id: str

channel_metadata: dict[str, ChannelMetadata] = {
    "C020740GTJ9": {
        "name": "Test Workspace General",
        "notion_task_db_id": "7ea61a8dedc94acfae021a432271981e",
    },
    "C95QCPHDW": {
        "name": "Tech Requests",
        "notion_task_db_id": "7ea61a8dedc94acfae021a432271981e",
    },
}