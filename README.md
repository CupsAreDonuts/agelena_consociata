Note: I originally built this project for myself and the current state fulfills my current needs. For now this project 
is closed until I need more features in my daily life.
Feel free to take and change the code and build upon what I have started.

---

Welcome to Agelena Consociata,
this application is a user interface that will help you keep track of your friends' preferences, birthdays, addresses, phone numbers and a couple other things.
The intention of this app is to help the user be a better friend and to not forget important details, meetings, holidays or birthdays.

The current features are:

- Keep track of your friends' addresses, preferences, goals and how you and your friends help or hinder each other's goals.
- Get an overview of your friends' birthdays and never forget a birthday ever again.
- Keep track of meetings and talks you had with your friends

Future features:

- Automatically message people custom messages via WhatsApp, Email or Signal
- Reminders to keep in touch with selected people if you haven't contacted them for a predefined time
- more will come

How to use:

- Setup MongoDB on your local machine
- Setup a database in mongoDB called: 'social_database'
- In this database set up two collections called 'people' and 'meetings'
- Your local address for MongoDB should be: mongodb://localhost:27017/ this is already coded, change it if you want to access your database somewhere else.

It is recommended to keep this social database on a local machine over which you have total control. 
The information you collect is sensitive, and only you should be able to access it.
