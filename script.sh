#!/usr/bin/env sh

dnf update -y
dnf remove gnome-boxes gnome-contacts gnome-maps gnome-weather gnome-software libreoffice-* evolution rhythmbox firefox -y
pip3 install --upgrade pip
dnf install python3-tkinter
cat res/user > /home/vampy/.config/dconf/user
