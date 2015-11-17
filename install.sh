#!/bin/bash

echo "Moving some shit around..."

mkdir -p ~/.config/avi
cp -R images ~/.config/avi
cp avi.py /usr/local/bin/avi

echo "Done moving shit."

echo "Checking config"
if [ -f ~/.config/avi/default.cfg ]; then
    echo "Config exists... Skipping"
else
    cp default.cfg ~/.config/avi/default.cfg
fi
echo "Done with the config..."

arg=("$@");
if [ "${arg[0]}" = "--with-tweepy" ]; then
    echo "Installing tweepy..."
    pip install -U tweepy
    echo "Done installing tweepy."
fi
