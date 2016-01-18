#!/bin/bash

# find . -not -path "*/\.*" -type f -exec 'find_call' \;
find * -name "*.md" -exec "find_call" {} +
