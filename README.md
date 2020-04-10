# amazon-aw-bot
A selenium bot that beeps if an Amazon Fresh availability window opens. It's not very sophisticated but it'll get you snacks and sugary sodas.

# Setup
1. Install `brew` if you don't have it already.
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install `git` if you don't have it already.
```
git --version
```
3. Clone the repository.
```
git clone https://github.com/Aaron-Benson/amazon-aw-bot.git
```
4. Install `python3`.
```
brew install python3
```
5. Install `chromedriver`.
```
brew cask install chromedriver
```
6. Install `python3` dependencies.
```
pip3 install selenium
pip3 install simpleaudio
```

# Usage Guide
1. Go into amazon fresh and load up your cart with snacks and sugary sodas.
2. Crank up the volume on your machine to max.
3. Run this script, make sure you `cd` into your `amazon-aw-bot` directory.
```
python3 amazon_aw_check.py
```
4. A chrome window should pop up, put in your username and password, clicking through the prompts and stop when you are logged in all of the way.
5. The script will start refreshing your cart every 2 minutes and will beep if an availabilty window opens. Don't navigate away from the page, keep it focused on the machine otherwise it won't work and will beep for no reason. I couldn't be bothered to fix this issue.
