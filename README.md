# Discord Bot Voting
This python script automates voting for a Discord bot.  This script utilizes Selenium WebDriver(a web automation API) and a single json file.

One of the projects for my summer 2019 internship at WealthPark was to help the QA team create automated tests for the company's web application using Selenium.
Understandably, all the work I did was pushed to a private repo, so I'm unable to show any of it.
But although this project doesn't match the complexity of what I had to work on, I thought it would be a good idea to show familiarity with web automation by using it for a lighthearted task I do often.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The only library you need to import is Selenium.

```
pip install selenium
```
More information is located on https://selenium-python.readthedocs.io/installation.html .

### Settings
Open the settings.json file in any text editor.
In the settings.json file, default values are set.  You must edit them in order for the script to properly work. 

First specify your browser. Only Safari, Firefox, and Chrome are supported.

```
"browser" : "safari
"browser" : "firefox
"browser" : "chrome
```

Specificy your e-mail

```
"email" : "myemail@domain.com"
```

Lastly specificy your password

```
"password" : "Passw0rd!"
```

After all of this, you should be ready to go!

## Future Improvements
- Specify which bot to vote for
