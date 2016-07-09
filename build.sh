#!/bin/bash
#Evan Widloski - 2015-01-17
#Search for org files and build them
#Call `find_call` for each file

cd content
# iterate all content files, ignore emacs backups
find . -regex "[^#]*\(org\|png\|jpg\|css\|js\|ttf\)" -not -path "*ltxpng*" -exec "../find_call" {} \;
