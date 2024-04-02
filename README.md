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

Command to run allure server in background
> nohup allure serve output/allure/ -p 8081 &

Command to stop the background running server
> ps aux | grep 'allure serve'

Pick the process id available next to username
Example:
> root       232  0.0  0.0   2880  1408 pts/0    S+   07:27   0:00 grep --color=auto allure serve

Here 232 is the process id

Close it by command:
> kill 232


# pytest flags
# -r ->  shows extra test summary
# -v -> verbose. use to get more information
# -n -> parallel count
# -m -> marker
# -k -> keyword driven
# -s -> console output
# -rE -> test summary with Error only. default flag

# important xdist commands
# --dist load -> send pending task to any available worker
# --dist loadscope -> tests are grouped by module/class/methods. Groups are distributed to available worker as whole unit.
# --dist loadfile -> Tests are grouped by their containing file. Groups are distributed to available worker as whole unit.
# --dist loadgroup -> Tests are grouped by given group/suite name. Groups are distributed to available worker as whole unit.
# --dist worksteal -> Tests are distributed evenly among all available workers.
# --dist no -> one by one execution. No distribution at all.