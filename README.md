Getting started

Prerequisite:
Must have installed python 3.8 or later

clone the repository on desire directory

Run:
> cd pytest_clean_slate 

Create VirtualEnv and start it to install all the required packages

On windows:
> python -m venv venv 
>
> venv\Scripts\activate

On linus/Mac:
> python3 -m venv venv
> 
> source venv/bin/activate

Upgrade the default pip version
> pip install --upgrade pip

Install the dependencies/packages
> pip install -r requirements.txt

Command to run test
> py.test -v -m "smoke" tests/ --browser edge --mode headless
 
Command to generate allure report
> allure serve output/allure/

