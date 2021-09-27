#!/bin/bash

# Premises: This script is ran on the operator computer
ROBOT_USERNAME= #... complete
ROBOT_IP= # ... complete
TEAM_NAME= # ... complete

# copy script to robot
scp topic-recorder.py ${ROBOT_USERNAME}@${ROBOT_IP}:~/
# copy topic config to robot
scp topic-record-robot.yml ${ROBOT_USERNAME}@${ROBOT_IP}:~/topic-record.yml
# install operator topic config
sudo cp topic-record-operator.yml ~/topic-record.yml
# start recording on operator
screen -S topic-record-operator -d -m ./topic-recorder.py -t $TEAM_NAME -l operator
# start recording on robot
ssh ${ROBOT_USERNAME}@${ROBOT_IP} "source /opt/ros/melodic/setup.bash && screen -S topic-record-robot -d -m ./topic-recorder.py -t $TEAM_NAME -l robot"
