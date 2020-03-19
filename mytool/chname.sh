#!/bin/bash

for file in $(ls)
do
	if [ `echo $file | grep '.mp3'` ] ; then
 		 rm $file
		#lame -V2 $file ${file%.*}.mp3
	fi
done
