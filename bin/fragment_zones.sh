#!/bin/bash

cd `dirname $BASH_SOURCE`/..

rm -f results/words/* 
rm -f results/meta/*

python src/fragment_zones.py tests/Mnatobi-009-cropped.png
#python src/fragment_zones.py tests/gray.png

