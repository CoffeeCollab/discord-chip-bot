# Discord Bot for GitHub Backlog

This Discord bot fetches the backlog of a specified GitHub repository and sends it to a Discord channel. It also mentions the appropriate Discord users based on their GitHub usernames.

## Setup

### Prerequisites

- Python 3 installed on your system
- Discord bot token
- GitHub repository details

### Installation

1. Clone this repository to your local machine:

2. Navigate to the project directory:

   ```
   cd discord_bot_project
   ```

3. Install the required Python packages using pip:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add the following environment variables:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   REPO_OWNER=github_repo_owner
   REPO_NAME=github_repo_name
   CHANNEL_ID=discord_channel_id
   GITHUB_USERNAME_1=DISCORD_USERNAME_1
   GITHUB_USERNAME_2=DISCORD_USERNAME_2
   GITHUB_USERNAME_3=DISCORD_USERNAME_3
   GITHUB_USERNAME_N=DISCORD_USERNAME_N
   ```

   Replace `your_discord_bot_token`, `github_repo_owner`, `github_repo_name`, and `discord_channel_id` with your actual values. Also, add mappings for GitHub usernames to Discord usernames.

### Usage

1. Run the bot using the following command:

   ```
   python main.py
   ```

2. Invite the bot to your Discord server using the bot's invite link generated from the Discord Developer Portal.

3. Interact with the bot in your Discord server by typing `!get_backlog` in any text channel.

### Contributing

Contributions are welcome! If you find any bugs or want to suggest improvements, feel free to open an issue or submit a pull request.

This video helped me a lot:
https://www.youtube.com/watch?v=UYJDKSah-Ww&t=791s
