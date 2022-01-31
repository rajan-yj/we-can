#!/bin/bash

original_path=$PWD

# Stop edge x and simulators
pushd ${original_path}/labs-air-edgex/linux/basicdemo > /dev/null
./stop.sh

# Stop lightcrane
pushd ${original_path}/labs-lightcrane-services/oss > /dev/null
./stop.sh

# Delete air infrastructure
pushd ${original_path}/labs-air-charts/air-backend > /dev/null
./stop.sh

