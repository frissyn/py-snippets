#!/bin/bash

echo -n "Snippet Name >> "; read name

if python "snippets/$name.py"; then
    printf "\n\nSnippet '$name.py' run successfully.\n"
else
    printf "\n\nAn error occured while running '$name.py'\n"
    exit 1
fi
