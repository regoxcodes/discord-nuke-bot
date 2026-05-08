# 🔥 Discord Nuke Bot

A powerful Discord bot that can nuke a server by deleting all channels and roles, then recreating it with a custom name. Perfect for exploring new configurations or testing!

## ⚠️ WARNING

This bot has destructive capabilities. Use it responsibly and only on servers you own or have explicit permission to modify.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- A Discord bot token from [Discord Developer Portal](https://discord.com/developers/applications)

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup your bot token:**
   - Rename `.env.example` to `.env`
   - Open `.env` and paste your bot token:
     ```
     DISCORD_TOKEN=your_actual_token_here
     ```

4. **Run the bot:**
   
   **Windows:** Double-click `start.bat`
   
   **Mac/Linux:** 
   ```bash
   python bot.py
   ```

## 📖 Getting Your Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application or select an existing one
3. Go to the **Bot** section
4. Click **Add Bot**
5. Under **TOKEN**, click **Copy** (copy this to your `.env` file)
6. Scroll down to **GATEWAY INTENTS** and enable:
   - Message Content Intent
   - Guild Intents
7. Save changes

## 🔐 Adding Bot to Your Server

1. In Developer Portal, go to **OAuth2** → **URL Generator**
2. Select scopes: `bot`
3. Select permissions: `Administrator`
4. Copy the generated URL and open it in your browser
5. Select your server and authorize

## 📝 Commands

### `!nuke <server_name>`
Nukes the server and renames it to your choice.

**What it does:**
- Deletes ALL channels
- Deletes ALL roles (except @everyone)
- Renames the server
- Creates a welcome channel

**Example:**
```
!nuke MyAwesomeServer
```

**Confirmation:** You'll need to react with ✅ to confirm (30 seconds timeout)

### `!help`
Shows available commands and usage

## ⚡ Features

✅ Delete all channels
✅ Delete all roles
✅ Rename server
✅ Confirmation system (react with ✅/❌)
✅ Error handling
✅ Beautiful embed messages
✅ Owner-only protection (only server owner can use `!nuke`)

## 🛠️ Troubleshooting

### Bot won't start
- Make sure Python is installed: `python --version`
- Check `.env` file exists and has your token
- Run `pip install -r requirements.txt` again

### "Bot is not responding"
- Make sure bot is added to server with Admin permissions
- Check Discord Developer Portal → Applications → Your Bot → OAuth2
- Verify GATEWAY INTENTS are enabled (Message Content Intent)

### "Only the server owner can use this command!"
- Only the server owner can execute the `!nuke` command for security

## 📄 File Structure

```
discord-nuke-bot/
├── bot.py              # Main bot code
├── start.bat           # Windows launcher
├── .env.example        # Token template (rename to .env)
├── .env                # Your actual token (not committed)
├── requirements.txt    # Python dependencies
├── .gitignore          # Protects .env file
└── README.md           # This file
```

## 🔒 Security

- Your `.env` file is protected by `.gitignore` - never commit it!
- Never share your bot token
- Only the server owner can use the nuke command
- The bot requires Administrator permissions

## 📞 Support

If you encounter issues:
1. Check that your bot token is correct
2. Verify the bot has Administrator permissions
3. Make sure you're the server owner
4. Check Python and dependencies are installed correctly

## 📜 License

Use responsibly. This tool is for educational and authorized use only.

---

**Enjoy exploring with your Discord nuke bot!** 🚀
