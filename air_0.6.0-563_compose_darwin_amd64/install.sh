#!/bin/bash

# Check dependencies
check_dependencies(){
    #Docker dependency
    if ! command -v docker &> /dev/null
    then
        echo "Docker could not be found and is required, please install it."
        exit
    fi
    #Docker compose dependency
    if ! command -v docker-compose &> /dev/null
    then
        echo "Docker Compose could not be found and is required, please install it."
        exit
    fi
}
check_dependencies

original_path=$PWD

# Install air infrastructure
pushd ${original_path}/labs-air-charts/air-backend > /dev/null
./start.sh

# Install lightcrane
pushd ${original_path}/labs-lightcrane-services/oss > /dev/null
./start.sh

# Install edgex and simulators
pushd ${original_path}/labs-air-edgex/linux/basicdemo > /dev/null
./start.sh

