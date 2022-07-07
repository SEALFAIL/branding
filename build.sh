#!/bin/bash

# Resets the line
LINE_RESET='\e[2K\r'

# Terminal escape codes to color text
TEXT_GREEN='\e[032m'
TEXT_YELLOW='\e[33m'
TEXT_RED='\e[31m'
TEXT_RESET='\e[0m'

# Logs like systemd on startup, it's pretty
TEXT_INFO="[${TEXT_YELLOW}i${TEXT_RESET}]"
TEXT_FAIL="[${TEXT_RED}-${TEXT_RESET}]"
TEXT_SUCC="[${TEXT_GREEN}+${TEXT_RESET}]"

# Variables
LOGFILE="buildlog.txt"
PACKAGE_NAME="sealfail-branding"
SOURCE_FOLDER="${PACKAGE_NAME}"
SOURCE_ARCHIVE="${PACKAGE_NAME}.tar.xz"

# Print the banner
echo '   _____ _________    __    _________    ______ '
echo '  / ___// ____/   |  / /   / ____/   |  /  _/ / '
echo '  \__ \/ __/ / /| | / /   / /_  / /| |  / // /  '
echo ' ___/ / /___/ ___ |/ /___/ __/ / ___ |_/ // /___'
echo '/____/_____/_/  |_/_____/_/   /_/  |_/___/_____/'
echo "  ${PACKAGE_NAME}"
echo ' '



# Clear the build log file
echo "===Buildlog===" > ${LOGFILE}



# Build the .tar.xz
echo -n -e "${TEXT_INFO} Building the source archive..."
tar cfJ ${SOURCE_ARCHIVE} ${SOURCE_FOLDER}/* &>> ${LOGFILE}
if [ $? -ne 0 ]; then
	echo -n -e "${LINE_RESET}"
	echo -e "${TEXT_FAIL} Couldn't build the source archive"
	exit 255
else
	echo -n -e "${LINE_RESET}"
	echo -e "${TEXT_SUCC} Built the source archive"
fi

mv ${SOURCE_ARCHIVE} /home/${USER}/rpmbuild/SOURCES/${SOURCE_ARCHIVE}

# Build the RPM
echo -n -e "${TEXT_INFO} Building the RPM package..."
rpmbuild -ba ${SPECFILE} &>> ${LOGFILE}
if [ $? -ne 0 ]; then
        echo -n -e "${LINE_RESET}"
        echo -e "${TEXT_FAIL} Couldn't build the RPM package"
        exit 255
else
        echo -n -e "${LINE_RESET}"
        echo -e "${TEXT_SUCC} Built the RPM package"
fi
