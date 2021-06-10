# P04_CHESS_CONTEST
Python app for create chess tournament

## About The Project

* Python chess contest is an app who allow an user to create a players, tournaments, turns and match. 
* the tournament is designed for 8 players.
* To generate the pairs, we use the suiss system

### Tested With
Python 3.8.5

### Built With

* [Python](https://www.python.org/)

## Getting Started

To start this project, you need to :
- clone the repo from this page.
- if you want to running the app on a virtual environnment, create it and launch it after installing packages :
 ```
python -m venv env
```
 ```
source env/bin/activate
```
 ```
pip install -r requirements.txt
```

- launch the app with python

#### Menu :

1. Create one on more players. You have to create at least 8 players to start a tournament. Each player have a unique ID. Follow the instruction in your terminal to complete all the required informations. 
2. Create a tournament. You can select players by ID to integrate them in the tournament.  Follow the instruction in your terminal to complete all the required informations. For the time control, you have 3 choices : "bullet", "blitz" or "coup rapide".
When the tournament is lauched, just follow the information in the terminal. You can quit the tournament when you want to resume later. 
3. Resume a tournament, you have to select a tournament by his ID for resume.
4. generate a report ( check the informations in the subsection "generate a report menu underneath" )
5. update player rank . You also have the possibility to update the rank player after each turn. Just select a player id and a tournament ID, then update the player rank. 

#### Generate report menu :

You can display the following informations in a report :
- list of all players by name
- list of all players by rank
- list of all tournament's players by name
- list of all tournament's players by rank
- list of all tournaments
- list of all tournament's turns
- list of all tournament's match

### Prerequisites

If they are not already installed on your system, you need to install all the package mentionned in requierement.txt :
  ```
pip install <package-name>
  ```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact
Dimitri hoareau - [https://twitter.com/dimitriHoareau1](https://twitter.com/dimitriHoareau1) - dimitrihoareau2@gmail.com

Project Link: [https://github.com/dimitri-hoareau/P02_scraper/](https://github.com/dimitri-hoareau/P02_scraper/)


