<h1 align="center"> PC Remote Control </h1>
This is a Telegram bot through which you can control your computer remotely.

## Getting Started

### Prerequisites

- Python 3.10+
- A Telegram Bot token
- Internet connection

### Instalation
Install the required packages:
```
 pip install -r requirements.txt 
```
Set the configuration parameters in `settings.yml`:
| Parameter | Description | Note
| --- | --- | --- |
| bot_token | Telegram Bot token |
| password | Your password |
| os | Your os type | valid inputs : windows - linux

Run `bot.py`:
```
python core/bot.py
```

## Commands

| Command | Description | Note
| --- | --- | --- |
| /start | Start bot |
| /login | Login | You must enter your password after this command
| /shutdown | Shutdown pc |

## Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
