# Overview

{Important!  Do not say in this section that this is a college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description of the software that you wrote and how it integrates with a Cloud Database.  Describe how to use your program.}

My purpose of writing this software was to gain a better understanding of how to use a cloud database, and how to connect it to somewhere where I can access the database and modify it the way I want. I also wrote this to get my feet wet with cloud programming to hopefully get into bigger cloud programming projects that involve AWS, Azure, and more.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

I am using a Realtime Database that is based on Google Firebase. Within this database, you can integrate it with Python, and use a Python program to create, modify, read, and delete. If you want to know more about how to get started with a Firebase database look for the link titled How to Get Started with Firebase Using Python in the [Useful Websites](#useful-websites) section.

In my Realtime Database on Firebase, the data is set up in a table called 'Users'. Inside 'Users', there will be names of users, with their corresponding passwords. That is the structure of the database so far, but I have plans to add more functionality to the program to add more things to the users as time goes on.

# Development Environment

I used Visual Studio Code to develop my software, Firebase Realtime Database to house my cloud database, and GitHub to host the code publicly so all can see the work I have done here on my cloud database.

The programming language I used for this project was Python 3.10 and the library I used for this project was firebase admin.

You can download the latest version of Python for your OS [here](https://www.python.org/downloads/), and you can find the installation process for the library in the [Useful Websites](#useful-websites) link titled How to Get Started With Firebase using Python.

You can create a free account for Firebase [here](https://firebase.google.com/). Follow the [Useful Websites](#useful-websites) link mentioned above to get started with doing that.

You can download the latest version of Visual Studio Code for your OS [here](https://code.visualstudio.com/Download) and can find the GitHub main website [here](https://github.com/). Feel free to create an account and fork the repo if you would like!

# Useful Websites

* [How to Get Started with Firebase Using Python](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)
* [How to Obtain Your Firebase (Data) Url?](https://www.appypie.com/faqs/how-to-obtain-your-firebase-data-url)

# Future Work
* When modifying users, check the levels of access the user has, and see if they can make changes or not
* Adding account classification to each user such as Admin, Normal, and others for the reason above
* Adding more options to add other things to the accounts, like bank info, id numbers, etc.
