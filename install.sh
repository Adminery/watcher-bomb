#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${RED}"
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                    Watcher Bomb Installer                        ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[!] Python3 not found. Installing...${NC}"
    if command -v apt &> /dev/null; then
        sudo apt update && sudo apt install python3 python3-pip -y
    elif command -v pkg &> /dev/null; then
        pkg update && pkg install python3 python3-pip -y
    elif command -v pacman &> /dev/null; then
        sudo pacman -S python python-pip --noconfirm
    fi
fi

echo -e "${GREEN}[*] Installing requirements...${NC}"
pip3 install -r requirements.txt

echo -e "${GREEN}[✓] Installation Complete!${NC}"
echo -e "${RED}[*] Run: python3 watcher.py${NC}"
