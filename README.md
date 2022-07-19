<!-- TABLE OF CONTENTS -->
# Table of Contents
- [Habit Tracker](#habit-tracker)
  * [Habit Tracker's Core Functionality](#habit-tracker-s-core-functionality)
    + [Progress and Streak Tracker](#progress-and-streak-tracker)
- [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installing](#installing)
    + [Packages for running tests](#packages-for-running-tests)
  * [How To Run the Program](#how-to-run-the-program)
- [Usage](#usage)
  * [Add/Remove Habit OR Category](#add-remove-habit-or-category)
      - [1. Adding a habit](#1-adding-a-habit)
      - [2. Remove Habit](#2-remove-habit)
      - [3. Delete Category](#3-delete-category)
      - [4. Back to Main Menu](#4-back-to-main-menu)
  * [Modify Habit's Periodicity](#modify-habit-s-periodicity)
  * [Mark Habit as Completed](#mark-habit-as-completed)
  * [Show Habits (All or Sort by Periodicity)](#show-habits--all-or-sort-by-periodicity-)
      - [1. View All Habits](#1-view-all-habits)
      - [2. View Daily Habits](#2-view-daily-habits)
      - [3. View Weekly Habits](#3-view-weekly-habits)
      - [4. View Monthly Habits](#4-view-monthly-habits)
      - [5. Back to Main Menu](#5-back-to-main-menu)
  * [Analytics](#analytics)
      - [1. View All Habit's Streaks](#1-view-all-habit-s-streaks)
      - [2. View Longest Streak of Specific Habit](#2-view-longest-streak-of-specific-habit)
      - [3. View Streak Log of Specific Habit](#3-view-streak-log-of-specific-habit)
      - [4. Back to Main Menu](#4-back-to-main-menu-1)
  * [Exit](#exit)
  * [Contributing](#contributing)
  * [Contact](#contact)

# Habit Tracker

Having good habits leads to a healthy and successful lifestyle. However, developing and maintaining good habits is indeed a challenge hence, a good habit tracker can serve as an assistant for maintaining, keeping track of, and principally viewing your progress.

This Habit Tracker will take all your data and progress headache away giving you more time to work on your habits. The program is a part of *IU University's* *DLBDSOOFPP01* course and uses Python 3.8 as the backend of the program.


## Habit Tracker's Core Functionality
The habit tracker essentially allows a user to:

* Add habit 
* Remove habit or category 
* Define Periodicity of habits (Daily, weekly, and monthly)
* Add Habit Category for habit reference
* Mark your habit as completed

### Progress and Streak Tracker
Additionally, the user can view:
* View all of their created habits
* View all of their created habits for a specific period
* View streaks of all habits
* View the longest streak of specific habit
* View streak history of specific habit



# Getting Started
**Important**: Make sure that Python 3.7+ is installed on your OS. You can download the latest version of Python from [this link.](https://www.python.org/downloads/)

## Dependencies
* Python 3.8 +
* Questionary 1.10.0 +

## Installing
You can download the latest version of Python from [this link.](https://www.python.org/downloads/) <br>
<br>[Questionary](https://www.python.org/downloads/) - Questionary is a Python library for building pretty command line interfaces. 
<br>Install by running the below command:<br>
```
pip install questionary
```

### Packages for running tests
Name the packages and instruction here - TOTOTO

## How To Run the Program
After installing the dependencies, download the files from this repository (if not downloaded already) and store them in a separate folder. Open your command/terminal window and [cd](https://www.alphr.com/change-directory-in-cmd/) to your downloaded folder. After that, type the following command to execute the program:
```
python main.py
```
For Python 3.10+
```
python3 main.py
```
Doing so will launch the CLI and then you'll be able to see and choose from the following options in your Habit Tracker:

```
*** Welcome to the Habit Tracker ***

What do you want to do? (Use arrow keys)
 » Add/Remove Habit OR Category
   Modify Habit's Periodicity
   Mark Habit as Completed
   Show Habits (All or Sort by Periodicity)
   Analytics
   Exit
```



# Usage
## Add/Remove Habit OR Category
#### 1. Adding a habit
Your first action should start by creating an habit and you can do so by launching the program and selecting:
```
 Add/Remove Habit OR Category
```
It will further expose the user to a sub-menu, where you'll have to choose *Add habit* and enter the required information:
```
Would you like to Add, Remove Habit or Category? (Use arrow keys)
 » Add Habit
   Remove Habit
   Delete Category
   Back to Main Menu

```
https://user-images.githubusercontent.com/48772669/179855439-e20830dc-1c75-41cf-aa57-a2c7b0c12a7a.mp4

#### 2. Remove Habit
This option will show you a list of habits that you have created, user will have to simply choose the habit you want to delete and press enter.

#### 3. Delete Category
Similar to removing habit; a list of created categories will be shown for the user to select.

#### 4. Back to Main Menu
Takes the user back to main menu.

## Modify Habit's Periodicity
User will have to select the habit they'd like to change the periodicity of and then a new prompt will ask the user to select the new periodicity for the habit.

## Mark Habit as Completed
User can select this option mark their habit as completed, if they have a completed the habit within the specified period.

https://user-images.githubusercontent.com/48772669/179856460-19a87cb4-4750-413c-89fa-16bd2b85be7d.mp4

## Show Habits (All or Sort by Periodicity)

#### 1. View All Habits
Lists all the created habits along with their information like *Name, Periodicity, Category and Date/Time*.

https://user-images.githubusercontent.com/48772669/179857285-921aea0b-e517-4e7b-a58a-0d83e9cefbe6.mp4

#### 2. View Daily Habits
Lists all the habits in the daily period.
#### 3. View Weekly Habits
Lists all the habits in the weekly period.
#### 4. View Monthly Habits
Lists all the habits in the monthly period.
#### 5. Back to Main Menu
Obvious function.



## Analytics
#### 1. View All Habit's Streaks
Lists all the habits and their streaks.

https://user-images.githubusercontent.com/48772669/179857969-61c3de26-bb0f-4624-a075-7f407d971547.mp4

#### 2. View Longest Streak of Specific Habit
Lists the longest streak ever achieved by a specific habit.
#### 3. View Streak Log of Specific Habit
Shows the streak history of the specific habit.
#### 4. Back to Main Menu
And menu it is!

## Exit
Exits the program.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Contact

Izaan Zubair - [Email](mailto:izkidy@yahoo.com)

Project Link: [https://github.com/izaanz/habit_tracker](https://github.com/izaanz/habit_tracker)

<p align="right">(<a href="#top">back to top</a>)</p>


