# Loan Service
A simple loan api for initiating loans, making payments and checking outstanding balances. The api is build using Djanog and Django rest framework

## Directory Structure
The directory structure has a modular approach for separation of concerns.

1. **App**: This directory contains app, core, payment, load, and balance subdirectories as follows:
  
    - App: This is the main directory used to run the app
    - Core: This subdirectory holds the shared business logic between various components of the services such as models, core unit tests and business logic.
    - Payment: This subdirectory holds the implementation of the payment api with its associated unit tests.
    - Loan: This subdirectory holds the implementation of the initiate loan api with its associated unit tests.
    - Balance: This subdirectory holds the implementation of the get balance api with its associated unit tests.

## Installation

### Prerequisites
1. Postgres: You need to have postgres installed on your local machine.
2. Python 3.9: You need to gave Python 3 installed on your local machine
3. Postman: You need postman installed.

### Procedure
1. Clone the project from this repository.
  ```
  git clone git@github.com:mwenechac/loan_service.git
  ```
2. Install virtualenv, create a virtual environment and activate it in your project directory.
   - Install virtualenv(a tool to create isolated Python environments) with the following command:
      ```
      python3 -m pip install --user virtualenv
      ```
   - Create a virtual environment with the following command:
      ```
      python3 -m venv env
      ```
    
   - Activate the virtual environment with the following command:
      ```
      source env/bin/activate
      ```
 3. Install packages:
 At the root of the project directory run the following command from the terminal to install packages from the requirements.txt file.
 
    ```
    pip3 install - r requirements.txt
    ```
 4. Set up a Postgres instance on your local machine and update connection credentials in the settings.py file in the app directory of the project.
 
    ```
      DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'loan_service',
          'USER': 'postgres',
          'PASSWORD': 'password',
          'HOST': 'localhost',
          'PORT': '5432',
          }
      }
    ```
 5. Run migrations.
 Navigate to the app direcroty from the root and the run the following command to run migrations and set up the database and the tables.
    - Navigate to the app directory.
      
        ```
        cd app
        ```
     - Run migrations.
     
          ```
          python manage.py makemigrations
          ```
     
 
 6. Run Unit Tests:
 From the app directory run the following command to run tests in the project.
     - Run the tests.
     
          ```
          python manage.py test
          ```
     If the tests run successfully, you will see an **OK** output on the terminal and you are good to go!
     
## Testing

 1. Use postman to interact with the apis.
    - Initiate loan: call the initiate loan api using the url: http://127.0.0.1:8000/loan/initiate. If you are not runing the project locally, subsitute the IP address with an applicable address. Make a post request with a request body similar to the one below. **The date format is yyyy-mm-dd.**
    
        ```
           {
              "amount": 1000,
              "interest": 10,
              "date": "2022-02-20"
           }
        ```
        If the Django server is running fine you should get a 200 HTTP response similar to:
        
        ```
          {
             "message": "A loan has been initiated"
          }
        ```
     - Make Payment: call the make payment api using the url: http://127.0.0.1:8000/payment/pay. If you are not runing the project locally, subsitute the IP            address with an applicable address. Make a post request with a request body similar to the one below. **The date format is yyyy-mm-dd.**
    
        ```
           {
              "amount": 500,
              "date": "2023-02-20"
           }
        ```
        If the Django server is running fine you should get a 200 HTTP response similar to:
        
        ```
          {
            "message": "An amount of 500.0 has been added successfully",
            "balance": 600.0
          }
        ```
    - Get balance: call get balance api using the url: http://127.0.0.1:8000/balance/get-balance?date=2023-01-26. The date is passed as a parameter in the url. **The date format is yyyy-mm-dd.** If you are not runing the project locally, subsitute the localhost IP address with an applicable address
   
        Make a get request and if the Django server is running fine you should get a 200 HTTP response similar to:
        
        ```
          {
            "data": {
                       "current_balance": 496.423
                     }
          }
        ```
 
