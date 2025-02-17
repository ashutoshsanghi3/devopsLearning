#!/bin/bash
#Purpose: print the size of directory
print_size(){
    local directory="$1"
    local size=0
    size=$(ls -lh "$directory" | awk 'NR==1 {print $2}')
    echo "size of directory: $size"
}

echo "please enter directory path"
read -r directory
print_size "$directory"