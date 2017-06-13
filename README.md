# simpleMastodonBot
A very, very simple Mastodon bot.  Uses the Mastodon.py wrapper for the Mastodon API.  

## Prerequisites (on linux): 
  * sudo apt install python-pip
  * pip install Mastodon.py

## Usage:
First, run ```simpleMastodonBot.py --cmd setup``` and follow the prompts to create the config files (files 
are created in your current working directory).  This will create three config files.

Keep the config files together, but feel free to place them whereever you like as long as they're readable.

Then, run ```simpleMastodonBot.py --cmd toot --cfg <path to .cfg file created with setup command> --text "<text of your toot>"``` 
to toot to your Mastodon account.
