𝔸𝕦𝕥𝕠𝕟𝕠𝕞𝕠𝕦𝕤 𝕍𝕖𝕙𝕚𝕔𝕝𝕖 𝔹𝕠𝕥 𝔸𝕀
project


# Introduction

Project milestone 3 for Code Institute Full-stack development program: Python Terminal.
Autonomous Vehicle Bot AI is a Python terminal bot, which runs in the Code Institute mock terminal on Heroku. The main goal of Autonomous Vehicle BOT AI is to recognise command and response quickly  in order to drive with comfort and efficiency plus with the word that the computer randomly selects. This project was inspired by The Fifth Element science fiction action film.

[Live Project Here](https://ai-auto.herokuapp.com/)

## User Experience - UX

### User Stories

* As an AI bot creator, I want to:
  
1. Build an easy app for the users to chat the bot.
2. Build an AI bot that is both enjoyable and challenging for the users.
   
* As a new autonomous vehicle bot AI owner, I want to:

1. Be able to understand the purpose of the AI chat and start drive a vechicle.
2. Be able to follow routine interacting daily with the vechicle, see the right letters appear once used right words.
3. Be able to drive and stop the car and immediatly keep moving forward if it is necessary.


## Features

### Logo and Intro Message

![Logo and Intro Message](./images/MAIN.png)
)
)

* When the users reach the website, they will see this feature. The Autonomous Vehicle Bot AI logo and the intro message are displayed here.

### Greeting message
![ Greeting message](./images/Greeting.png)
)

* When the users
## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
