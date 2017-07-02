#!/usr/bin/env sh

dnf remove gnome-boxes gnome-contacts gnome-maps gnome-weather gnome-software libreoffice-* evolution rhythmbox firefox -y
dnf update -y
pip3 install --upgrade pip
dnf install python3-tkinter jre java-devel nano -y
#cat res/user > /home/vampy/.config/dconf/user
echo "alias espeak='echo With great power comes great responsibility.'" >> /home/vampy/.bashrc
