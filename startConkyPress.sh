#!/bin/bash
#
# Run this script to start conkyPress
#
folderPath=$(dirname $0)
cd "$folderPath"
conky -d -c conkyPressRc

exit 0
