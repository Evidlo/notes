#!/bin/bash
#Evan Widloski - 2015-01-17
#Search for markdown files and build them

find * -name "*.md" -exec "find_call" {} \;
