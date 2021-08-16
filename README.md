
# Delivery Company
### About

Delivery company's automatization program is a Phyton terminal program, which runs in the Code Institute mock terminal on Heroku.
This program after input the number (the number is the suggested number of parcels coming in depo for delivery) doing the following operation:
- Split parcels between drivers.
- Calculate every driver's working hours.
- Calculate every driver's salary.
- Calculate total payment to drivers.
- Calculate the profit.
- Push all the data to delivery_company spreadsheets.

[Here is the live version of my project.](https://delivery-compane.herokuapp.com/)

![Responsice Mockup](static/images/mockup.png)

## Table of Contents
  - [How to use](#how-to-use)
  - [Project idea](#project-idea)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Content](#content)
## How to use

Delivery company automatization program is build to save time, money and increase efficiency in the company.

In this version, the user enters the number of parcels expected for delivery. A number has to be bigger than 10 and smaller than 2000 because less than 10 is not enough for 10 drivers and more than 2000 is too much for 10 drivers (capacity of delivering  parcels is max 200 parcels per driver).

The program is splitting equally the number of parcels between 10 drivers. Calculate every driver's working hours, salary, profit of the company and will push all the data to delivery_company spreadsheets.

## Project idea

Project idea I got from my workplace. I am working in the delivery company at a moment and I thought will be helpful to use automatization program to save time, money and increase efficiency in the company.

## Features

### Existing Features

- Welcome Message
 
  - Shows welcome message.
  - Ask the user to enter valid data.
  - Shows example of valid data.
  - Shows were to enter valid data.

![Feature1](static/images/pic1.png)

- Update worksheet
  
   - Calculate driver's parcels, hours, salary and company's profit.
   - Update delivery_company spreadsheet


![Feature2](static/images/pic2.png)

- Option
  
  - Give to a user the option if he\she wants to input new data again.
  - If yes, print instructions on what to do to input new data.
  - If no, print the 'Have a nice day' string.

![Feature3](static/images/pic3.png)

## Technologies Used

__Lucid Wireframe__

![Wireframe](static/images/wireframe.png)

 - [Lucid](https://lucid.app/)
   - To build the wireframe.
 - [Github](https://github.com/)
  
   - For the hosting and version control of the website and for storage media content.
 - [Gitpod](https://gitpod.io/)

   - The development enviroment used used for writing the code for the website.
 - [Heroku](https://dashboard.heroku.com/)
   
    - For deployment
## Testing
 ### Validator Testing
- PEP8
   - No errors were returned from PEP8online.com

![Validator](static/images/validator.png)
## Deployment
## Content
