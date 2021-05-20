#!/usr/bin/env python3

from mastodon import Mastodon
import argparse
import os

_cfgFilePermissions=0o600

_completionString="Bot setup with Mastodon URL %s and email address %s.  Congrats!"

_cfgFile=""
_clientCredFile=""
_userCredFile=""

def main():
	parser = argparse.ArgumentParser(description='Simple Mastodon Bot Command Script')
	parser.add_argument('--cmd', help='Command, either "setup" or "toot"',required=True)
	parser.add_argument('--cfg', help='Location of config file produced by install step', required=False)
	parser.add_argument('--text', help='Text of toot to toot!',required=False)
	args = parser.parse_args()
	 
	if args.cmd == "setup":
		setupBot()
	elif args.cmd == "toot":
		if (args.cfg is not None and args.text is not None):
			### Strip .cfg from end of config file and create file names
			setConfigFiles(args.cfg[:-4])
			toot(args.text)
		else:
			print('If cmd passed is "toot", need --cfg and --text passed as well.')
	else:
		print('Command passed must be either "setup" or "toot".')

def setConfigFiles(botName):
	global _cfgFile
	global _clientCredFile
	global _userCredFile
	_cfgFile = botName + ".cfg"
	_clientCredFile = botName + ".client_id"
	_userCredFile = botName + ".access_token"

def setupBot():
	botName = raw_input('Enter a unique name for this bot: ')
	instanceURL = raw_input('Enter your mastodon URL: ')
	accountEmail = raw_input("Enter your bot's Email address: ")
	accountPW = raw_input("Enter your bot's password: ")

	setConfigFiles(botName)

	configFile = open(_cfgFile, "w")
	configFile.write(instanceURL)
	configFile.close()

	# Create app
	Mastodon.create_app(
		botName
		,to_file = _clientCredFile
		,api_base_url = instanceURL
	)

	# Get access tocket
	botAPI = Mastodon(
		client_id = _clientCredFile
		,api_base_url = instanceURL
	)

	botAPI.log_in(
		accountEmail
		,accountPW
		,to_file = _userCredFile
	)

	os.chmod(_cfgFile, _cfgFilePermissions)
	os.chmod(_clientCredFile, _cfgFilePermissions)
	os.chmod(_userCredFile, _cfgFilePermissions)

	print(_completionString % (instanceURL, accountEmail))

def toot(tootText):
	apiURLFile = open(_cfgFile, "r")
	apiURL = apiURLFile.read()
	apiURLFile.close()

	mastodon = Mastodon(
		client_id=_clientCredFile
		,access_token=_userCredFile
		,api_base_url=apiURL
	)

	mastodon.toot(tootText)

main()
