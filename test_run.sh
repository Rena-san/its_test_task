#!/bin/bash

path_to=tests

files=($(ls $path_to | grep test_))
cd $path_to

if [ "$#" == 0 ];
then
  for file in ${files[@]}; do
    echo ${file}
  done
elif [ "$#" == 1 ];

then
  for file in ${files[@]}; do
    pytest ${file} --deviceName=$1 --alluredir=./my_allure_results
    done
  allure serve ./my_allure_results
else
  pytest $1 --deviceName=$2 --alluredir=./my_allure_results
  allure serve ./my_allure_results
fi



