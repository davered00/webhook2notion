from typing import TypedDict

from api import notion_client
from metadata import channel_metadata


class CreateTaskResponse(TypedDict):
    url: str

def create_notion_task(
    channel_id: str,
    title: str,
) -> CreateTaskResponse:
    metadata = channel_metadata.get(channel_id)
    database_id = metadata["notion_task_db_id"] if metadata is not None else None

    return notion_client.request(
        path="pages",
        method="POST",
        body={
            "parent": {"database_id": database_id},
            "properties": {
                "Name": {
                    "title": [
                        {"text": {"content": title}},
                    ],
                },
            },
            # "children": [
            #     {
            #         "object": "block",
            #         "type": "paragraph",
            #         "paragraph": {
            #             "text": [
            #                 {
            #                     "type": "text",
            #                     "text": {"content": "Test comment"}
            #                 },
            #             ],
            #         },
            #     },
            # ],
        },
    )