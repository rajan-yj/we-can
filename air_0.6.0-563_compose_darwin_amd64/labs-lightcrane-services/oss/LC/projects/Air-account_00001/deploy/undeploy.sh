#!/bin/bash

Namespace=$1
DeployType=$2
ServiceName=$3
ProjectID=$4
InstanceID=$5
export ServiceVersion=0.1.0
export Arch="$(cut -d'/' -f2 <<<"$Platform")"

echo "Namespace    = $Namespace"
echo "DeployType   = $DeployType"
echo "ServiceName  = $ServiceName"
echo "ProjectID    = $ProjectID"
echo "InstanceID   = $InstanceID"
echo "Username     = $Username"
echo "TargetServer = $TargetServer"
echo "Port         = $Port"

echo "Working folder $(pwd)"
echo "source ./docker-compose.sh"

source ./docker-compose.sh

undeploy
