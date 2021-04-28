
import os
from notion.client import NotionClient
from notion.block import TextBlock
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, title, content):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = title
    row.children.add_new(TextBlock,title=content)


@app.route('/create_todo', methods=['GET'])
def create_todo():

    title = request.args.get('title')
    content = request.args.get('content')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, title, content)
    return f'added {title} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
