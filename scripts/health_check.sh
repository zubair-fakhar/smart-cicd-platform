#!/bin/bash

response=$(curl -s http://localhost/health)

if [[ "$response" == "healthy" ]]
then
    exit 0
else
    exit 1
fi
