#!/usr/bin/env bash

X=718
Y1=869
Y2=554

sleep 1

while :
do
  xdotool mousemove $X $Y1 mousedown 1
  sleep 0.1
  xdotool mousemove $X $Y2 mouseup 1
  sleep 1
done
