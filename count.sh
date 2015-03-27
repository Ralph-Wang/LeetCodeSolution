#!/usr/bin/env bash

count_dir()
{
    echo $(ls -F $1 |grep /|wc -l)
}

answer=0

for dir in $(ls -F|grep /);do
    let answer=$answer+$(count_dir $dir)
done

echo $answer
