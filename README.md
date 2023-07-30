# its_test_task

1 run the test
python -m tests.addition_test
pytest tests/addition_test.py --deviceName=emulator


sh test_run.sh test_add.py emulator

sh test_run.sh 

sh test_run.sh emulator


pytest --deviceName=emulator --alluredir=/tmp/my_allure_results


for installing allure comand lina
https://docs.qameta.io/allure/

get report
allure serve /tmp/my_allure_results