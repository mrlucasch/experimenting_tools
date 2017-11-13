#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Usage:"
	echo "$0 experiment_name"
	echo "Example:"
	echo "$0 test1 weight_20 trial-2 author-lucas"
	echo "This makes a directory: "
	echo "test1_weight_20_trial-2_author-lucas_2017-11-13_14-57-46"
	exit
fi

timestamp=$(date "+%Y-%m-%d_%H-%M-%S")

dirname=$1
shift

for var in "$@"
do
    echo "$var"
	dirname=${dirname}"_"${var}
done

mkdir ${dirname}_${timestamp}
