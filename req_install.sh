#!/bin/bash
echo "PATH: $PATH"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
echo ">>>>>>>>>>>>>>>>>>Installing dependency packages from requirements file"
pip install -r requirements.txt
echo ">>>>>>>>>>>>>>>>>>>> Running tests"
pytest -v -k lastName tests/
echo ">>>>>>>>>>>>>>>>>>>> Generating test report"
allure serve output/allure/
#deactiavte
