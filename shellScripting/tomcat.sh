#!/bin/bash 
#Author: Ashutosh Sanghi
#Usage: ./tomcat.sh

#Purpose:
# Write a shell script to clone a git repo and deploy maven based java application on tomcat.
# 1. Download tomcat
# unzip
# webapps
# bin
# 2. write shell script
# input: git repo.
# clone the repo.
# get inside
# mvn clean package
# target folder - war file
# copy *.war to webapps of tomcat
# $tomcat/bin/catalina.bat start

TOMCAT_DIR="/tomcat"
GIT_REPO="../../Downloads/docker-k8s-master"
cd ${GIT_REPO} || return
mvn clean install
