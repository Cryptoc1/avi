#!/bin/bash

echo "Moving some shit around..."

mkdir -p ~/.config/avi
cp -R images ~/.config/avi
cp avi.py /usr/local/bin/avi

echo "Done moving shit."

echo "Installing tweepy..."
pip install -U tweepy
echo "Done installing tweepy."
