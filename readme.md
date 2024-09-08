# Discord Message to Image Converter Bot

This Discord bot converts messages into Twitter-style images. It's perfect for creating shareable, visually appealing representations of Discord messages.

## Features

- Convert Discord messages to Twitter-style images
- Customizable appearance with dark mode aesthetics
- Includes user avatar, name, username, message content, and timestamp

## Requirements

```1:4:requirements.txt
discord.py==1.7.3
Pillow==8.3.1
python-dotenv==0.19.0
requests==2.26.0
```

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_token_here
   ```
4. Run the bot:
   ```
   python main.py
   ```

## Usage

The bot responds to the following commands:

- `!convert <message_link>`: Converts the linked message to an image
- `!ping`: Checks if the bot is responsive

To convert a message, right-click on it in Discord, copy the message link, and use the `!convert` command with the link.

## Project Structure

- `main.py`: Entry point of the application
- `bot/client.py`: Discord client setup
- `bot/commands.py`: Bot command definitions
- `utils/image_generator.py`: Image generation logic

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

- If you encounter any issues, please check the following:
  - Ensure your message link is correct
  - Make sure the bot has the necessary permissions to read messages in the channel
  - Go to https://discord.com/developers/applications select your application, go to the bot tab, and check the "Presence Intent", "Server Members Intent" and "Message Content Intent" permissions.
  - Verify that the bot token is correctly set in the `.env` file

## License

This project is open source and available under the [MIT License](LICENSE).
