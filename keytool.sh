#!/bin/bash

cert_loc=$1
if [ -z $cert_loc ]
then
cert_loc="."
fi

ks=$2
if [ -z $ks ]
then
ks='$cert_loc'/new_ks.jks
fi

ts=$3
if [ -z $ks ]
then
ks='$cert_loc'/new_ts.jks
fi

echo $cert_loc

for file in "$cert_loc"/*
do

ext="${file##*.}"

basename=$(basename $file)
filename="${basename%.*}" 
lc_filename=$(echo $filename | tr 'A-Z' 'a-z')
alias="${lc_filename// /_}"

echo $alias
echo $ext
echo "++++++++++++++++++++++++++++"

if [[ "$ext" == "cer" ]]
then
keytool -import -file "$file" -alias $alias -storepass Qqyopta -storetype JKS -keystore "$ks"
keytool -import -v -trustcacerts -file "$file" -alias "$alias" -storepass Qqyopta -storetype JKS -keystore "$ts"
fi
done
