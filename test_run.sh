#!/bin/bash
#path_to=tests/
#
#cd $path_to
#
#pytest $1 --deviceName=$2


path_to=tests
files=($(ls $path_to | grep test_))
cd $path_to

#rm -r my_allure_results
#
#for file in ${files[@]}; do
#    echo ${file}
##    pytest $1 --deviceName=$2
#done


if [ "$#" == 0 ];
then
  for file in ${files[@]}; do
    echo ${file}
  done
elif [ "$#" == 1 ];
then
  rm -r my_allure_results
  for file in ${files[@]}; do
    pytest ${file} --deviceName=$1 --alluredir=./my_allure_results
    done
  allure serve ./my_allure_results
else
  rm -r my_allure_results
  pytest $1 --deviceName=$2 --alluredir=./my_allure_results
  allure serve ./my_allure_results
fi

#allure serve ./my_allure_results

