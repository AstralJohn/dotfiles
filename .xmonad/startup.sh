#!/bin/bash

expressvpn connect &
xflux -z 19382 -k 2500
playerctld daemon

while true ; do
    feh --bg-fill --randomize ~/Pictures/wallpapers/*
    sleep 60s
done
