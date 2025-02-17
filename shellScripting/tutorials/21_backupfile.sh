#!/bin/bash 
#Author: Ashutosh Sanghi
#Purpose: Learning to backup file and error handling
#Usage: ./backupfile.sh

function backup {
    echo "enter the file name"
    read -r myfile
    if [ -f $myfile ]; then 
        echo "file exists"
        cp $myfile /tmp/backup.sh
    else 
        echo "file doesn't exists"
    fi
    
    #Error handling
    # cp $myfile /tmp/backup.sh
    # echo $? #error handling
    # if [ $? -ne 0 ]; then    
    #     echo "Backup failed"
    # fi
}

backup