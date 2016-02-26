#!/bin/bash
#Evan Widloski - 2015-01-17
#Search for markdown files and build them

find . -regex ".*\(org\|png\|jpg\)" -not -path "*ltxpng*" -exec "find_call" {} \;
