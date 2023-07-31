# Testing AdroidCalculator app`s addition operations at real device or emulator

This project testing simple addition operations at calculator app.

## Set up 0:
>1. Android Studio
> > https://developer.android.com/studio
>2. Appium
> >https://appium.io/docs/en/2.0/quickstart/install/
>3. Allure command-line 
> >https://docs.qameta.io/allure/#_installing_a_commandline

## Set up 1:
1. Run Adnroid Studio and create an emulator or plug real device.
2. Add your device capabilities to tests/config.py and Appium.
3. Run Appium.

## Set up 2:
1.Create virtual venv:
>python - m venv venv
2. Activate virtual venv:
>>source venv/Scripts/activate
3. Install requirements:
>>pip install -r requirements

###Run tests with pytest and save allure log:
Default device is an emulator.
1. Run all tests at the emulator:
>> pytest  --alluredir=/tmp/my_allure_results
2. Choose the device (emulator/real) for running tests
> pytest --deviceName=<device_name> --alluredir=/tmp/my_allure_results
>>pytest --deviceName=emulator --alluredir=/tmp/my_allure_results
3. Choose the test and the device:
> pytest tests/<test_name> --deviceName=<device_name> --alluredir=/tmp/my_allure_results
>>pytest tests/tests_addition.py --deviceName=emulator --alluredir=/tmp/my_allure_results

###Run tests with bash and get allure report:
1. Show all test`s names
>sh test_run.sh 
2. Choose the device (emulator/real) for running all tests
>sh test_run.sh device_name
>>sh test_run.sh emulator
3. Choose the test and the device:
>sh test_run.sh <test_name> <device_name>
>>sh test_run.sh test_addition.py emulator

###Run tests with python
>python -m tests.<name_test>
>>python -m tests.addition_test

### Get Allure report
>>> allure serve /tmp/my_allure_results