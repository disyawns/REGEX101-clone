#Regex101 Clone
This project is a simplified clone of the website regex101.com. It allows users to input a test string and a regular expression (regex) and displays all the matches found.

Table of Contents
Features
Getting Started
Prerequisites
Installation
Usage
Deployment
Built With
License
Features
Input a test string and a regex pattern.
Display all matches found in the test string for the given regex pattern.
Validate if a given email address is valid or not.
Getting Started
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
Flask
Git (for deployment to GitHub)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/regex101-clone.git
Navigate into the project directory:

bash
Copy code
cd regex101-clone
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Flask application:

bash
Copy code
python app.py
Open a web browser and navigate to http://localhost:5000 to access the application.

Input test strings and regex patterns to see matches found or validate email addresses.

Deployment
To deploy the application on AWS:

Set up an AWS account if you haven't already.
Install and configure the AWS CLI.
Initialize Elastic Beanstalk with eb init.
Create an environment with eb create.
Deploy the application with eb deploy.
Access your application through the provided URL.
For detailed instructions on deploying to AWS, refer to the deployment section in the README.

Built With
Flask - Python web framework
AWS Elastic Beanstalk - Deployment platform
License
This project is licensed under the MIT License - see the LICENSE file for details.
