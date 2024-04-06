from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import requests

# Load our token and repo details from dotenv
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
REPO_OWNER: Final[str] = os.getenv('REPO_OWNER')
REPO_NAME: Final[str] = os.getenv('REPO_NAME')

# Load the username map from the .env file
username_map = dict(os.environ)

# Initialize the Discord client
intents = Intents.default()
intents.messages = True
client = Client(intents=intents)


def get_discord_username(github_username):
    # Map GitHub usernames to Discord usernames
    return username_map.get(github_username, github_username)  


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: Message):
    print('Triggered on_message function')
    if message.author == client.user:
        return

    print('!get_backlog')
    backlog = get_backlog()
    if backlog:
        await message.channel.send(backlog)
    else:
        await message.channel.send('Error fetching backlog')


def get_backlog() -> str:
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    response = requests.get(url)
    print(response.text)  # Print the response for debugging
    if response.status_code == 200:
        issues = response.json()
        backlog = ''
        for issue in issues:
            assignees = ', '.join(get_discord_username(assignee['login']) for assignee in issue.get('assignees', []))
            backlog += f"Task: {issue['title']} - Assignees: {assignees}\n"
        return backlog
    else:
        print('Error fetching backlog')
        return None  # Return None instead of a string


client.run(TOKEN)