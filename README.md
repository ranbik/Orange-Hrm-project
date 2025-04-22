## Orange HRM Automation Project 🧪

   This project automates the different functionality of the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/) using Python, Selenium, and unittest framework.


 ## File List

   Orange3.py :        Script for add employee test. 
 
   Orange2.py :        Main script for login automation. 
 
   orange_POM_DDT.py:  Data-driven tests using POM. 
 
   XLUtils.py  :       Excel utility functions for test data. 
 
   MOCK_DATA.xlsx :    Test data file for orange orange_POM_DDT.py 
   
## Getting Started

 To view the details of each project, simply click on the project name in the table above. The project page will contain a brief description of the project as well as a list of tools used to complete the project.


## Orange 3:  #  OrangeHRM: Add Employee Automation (with Faker)

This project automates the process of adding new employees to the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) demo system using Selenium WebDriver and Python's `faker` library for dynamic test data.

## 📁 Project Files
Orange-Hrm-project/ ├── add_employee_faker.py # Main automation script using Faker ├── Screenshot.png # Profile image used during upload ├── README.md # Project documentation

 ## Features

- Automated login to OrangeHRM as Admin
- Random employee details generated via the `faker` library
- Form automation for adding new employees
- Profile photo upload
- Verification that the "Personal Details" page appears after saving

  ## Tools

- Python
- Selenium WebDriver
- faker (for generating random names and employee IDs)
- Firefox browser with [geckodriver](https://github.com/mozilla/geckodriver/releases)

## orannge 2 : OrangeHRM Login Automation Test

This project automates the login and logout functionality of the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/) using Selenium WebDriver with Python's `unittest` framework.

## 📁 Project Structure 

Orange-Hrm-project/ ├── login_test.py # Script to test login/logout flow ├── README.md # This documentation



## feature

- Opens the OrangeHRM login page
- Logs in with valid admin credentials
- Navigates to the user dropdown
- Logs out of the session
- Verifies that the login page

##  Tools

- Python 
- Selenium WebDriver
- Firefox browser
- unittest (Python's built-in testing framework)
- [geckodriver](https://github.com/mozilla/geckodriver/releases)

Orange_POM_DDT.py:  OrangeHRM Add Employee Automation

This project automates the process of adding new employees in the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) system using Selenium WebDriver and data-driven testing via Excel files.

## 📂 Project Structure

Orange-Hrm-project/ ├── Orange3.py # Login automation script ├── orange_POM_DDT.py # Data-driven test using Page Object Model ├── XLUtils.py # Utility functions for Excel reading/writing ├── MOCK_DATA (4).xlsx # Excel file containing employee data ├── README.md # 

##  Features

- Logs into OrangeHRM as Admin
- Reads employee data from an Excel sheet
- Automatically fills in and submits the "Add Employee" form
- Uploads a profile picture
- Enables login creation for each employee
- Logs test results (pass/fail) back to Excel

## Tools

- Python 3.x
- Selenium
- Firefox & [geckodriver](https://github.com/mozilla/geckodriver/releases)
- openpyxl  library for Excel reading/writing











 Contributing

If you have any feedback or suggestions for improvements, please feel free to open an issue or pull request.









