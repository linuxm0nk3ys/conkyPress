#!/bin/bash
#
# Run this script to start or stop conkyPress



#
# start conkyPress
#
start_cp()
{
	echo 'starting'
	folderPath=$(dirname $0)
	cd "$folderPath"
	conky -d -c conkyPressRc
}

#
# stop conkyPress
#
stop_cp()
{
	echo 'stopping'
	PID=$(ps -C conky a | grep 'conkyPress' | grep '\-d' | awk {'print $1'})
	if [ -z "$PID" ] 
	then
		echo "No running ConkyPress instances found"
	else	
		kill -9 $PID
	fi
}

#
# print the manual
#
echo_manual()
{
	echo 'Usage:'
	echo 'Starting conkyPress: ./conkyPress.sh start'
	echo 'Stopping conkyPress: ./conkyPress.sh stop'
}

if [ $1 ]; then
	if [ $1 = "start" ]; then
		start_cp
	elif [ $1 = "stop" ]; then
		stop_cp
	elif [ $1 = "restart" ]; then
		echo 'restarting'
		stop_cp
		start_cp
	else
		echo_manual
	fi
else
	echo_manual
fi

exit 0
