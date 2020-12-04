#!/bin/bash

echo -n "Enter snippet name >> "
read name

python "snippets/$name.py"
