#!/bin/bash

echo -n "Enter snippet name >> "; read name

if python "snippets/$name.py"; then
    printf "\n\nSnippet '$name' run successfully.\n"
else
    printf "\n\nAn error occured while running '$name'\n"
    exit 1
fi
