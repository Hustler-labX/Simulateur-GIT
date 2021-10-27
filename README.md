# Simulateur-GIT
This project is similar to git system. We have different users and each users have access to the main Data Base. The user has two possibilities : be Online or Offline.
So we need a certain system of synchronization to resolve this kind of problem. If the user is Offline, the point in which he gets back Online the Algorithm which I have implement will solve the conflits.
If two or more of users have changed the same data, it will occurs a certain of discussion already to choose the correct data to be committed to the main server.
I used the example of hospital database, in which the doctor and his assistant have access to the same database.

I choose to work with Python3 and Sqlite3 as DataBase system.
Also, I have used the bibliothec PyQt5 to get a Graphic Interface to facilitate using the application.
You need to Import your PyQt5, if you are using ubento: sudo apt install python3-pip and then pip install PyQt5.
