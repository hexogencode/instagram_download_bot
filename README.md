# Instagram Downloader Bot

This is a Telegram bot built with [aiogram](https://github.com/aiogram/aiogram) that allows users to download Instagram videos and posts without watermarks.

## Features

- **Download Instagram Posts and Reels**: Users can simply paste the link to an Instagram Post or Reel, and the bot will provide a downloadable version of the content.
- **Inline Menu**: The bot provides an interactive inline menu for easy navigation and interaction.
- **State Control**: By controlling states bot will function as the user personally wants
- **Error Handling**: Handles incorrect URLs gracefully and provides appropriate error messages to users.
- **Parser**: By parsing links bot can get actual URLs of video and send them as media without download

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your_username/instagram-downloader-bot.git
   ```

2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Obtain a Telegram Bot Token from [BotFather](https://core.telegram.org/bots#6-botfather).

4. Add your token in a `TOKEN.py` file in the root directory of the project:

   ```python
   TOKEN = "your_token_here"
   ```

**Do not forget to update chromedriver.exe if the version does not match your browser!**

## Usage

1. Start the bot by running:

   ```
   python bot.py
   ```

2. Open Telegram and start a conversation with the bot.

3. Paste the link to an Instagram Reel to download it.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to open a pull request or create an issue.
