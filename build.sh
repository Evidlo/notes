#!/bin/bash
#Evan Widloski - 2015-01-17
#Search for markdown files and build them

find ./content -regex ".*\(org\|png\|jpg\|css\|js\|ttf\)" -not -path "*ltxpng*" -exec "find_call" {} \;
