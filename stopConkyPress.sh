#!/bin/bash
#
# Run this script to stop all conkyPress instances
#
PID=$(ps -C conky a | grep 'conkyPress' | grep '\-d' | awk {'print $1'})
if [ -z "$PID" ] 
then
	echo "No running ConkyPress instances found"
else	
	kill -9 $PID
fi

exit 0
