#!/bin/bash

DESKTOP_EXE_INSTALLDIR="/usr/share/applications"
DESKTOP_EXE_FILENAME="myapp.desktop"  ###modify this to set a custom name for your .desktop file

ICON_INSTALLDIR="/usr/share/icons"
ICON_FILENAME=                   ###modify this to the name of what you called your desktop icon


installme() {

createGUITEMS
###DO YOUR CUSTOM INSTALL CODE HERE
#Normally just copy your need program files to the appropriate directories
#probably just /usr/bin , /bin , /usr/local/bin ,...etc directories 
## however i cannt account for all OS and directories where things should go 
#for your individual programs so i give you a place to do it yourself 

###Currently this function just creates startup menu icons for your application with a call to
### createGUITEMS function!!!

}


uninstallme() {

destroyGUITEMS
###UNDO what you did in install() function exactly
###So you dont have any left over clutter on anybodies system!!!!

###Currently this function just destroys the startup menu icons for your application 
###with a call to createGUITEMS function!!!
### Add your code as needed!

}


function createGUITEMS()
{

###function used for making executable desktop and menu icons for your program!!!
### called when installing your program

echo "Your Desktop executable clickable created! " ;
echo "Filename: $DESKTOP_ICON_FILENAME" ;

cat > $DESKTOP_EXE_FILENAME <<'DESKTOP_ICON_FILE'
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Testing
Comment=A sample application
Exec=gedit
Icon=/home/nate/Desktop/Solomon_Golomb_2014.jpg
Terminal=false
GenericName[en_US.UTF-8]=Testing Applicationsss
Name[en_US]=Test  !
DESKTOP_ICON_FILE

echo "Installing Desktop executable clickable! " ;
chmod +x $DESKTOP_EXE_FILENAME ;
mv $DESKTOP_EXE_FILENAME $DESKTOP_EXE_INSTALLDIR ;
echo "Done! " ;
echo "Installing custom icon..."



if [ -f "$ICON_FILENAME" ] 
then
	cp $ICON_FILENAME $ICON_INSTALLDIR ;
	echo "Done! " ;
else
	echo "no custom icon detected using default system icons for your app!!!" ;
fi



}


function destroyGUITEMS()
{

### function that removes your executable desktop and menu icons for your program!!!
### called when uninstalling your program

if [ -f "$DESKTOP_EXE_INSTALLDIR/$DESKTOP_EXE_FILENAME" ] 
then
	echo "removing $DESKTOP_EXE_INSTALLDIR/$DESKTOP_EXE_FILENAME" ;
	rm $DESKTOP_EXE_INSTALLDIR/$DESKTOP_EXE_FILENAME ;
	echo "done !" ;
else
	echo "was already removed $DESKTOP_EXE_INSTALLDIR/$DESKTOP_EXE_FILENAME" ;
fi

if [ -f "$ICON_INSTALLDIR/$ICON_FILENAME" ] 
then
	echo "removing $ICON_INSTALLDIR/$ICON_FILENAME" ;
	rm "$ICON_INSTALLDIR/$ICON_FILENAME"
	echo "done !" ;
else
	echo "was already removed $ICON_INSTALLDIR/$ICON_FILENAME" ;
fi


}


### called to install your program
if [ $1 == 'install' ]
then
installme ;
echo "installer program finished!" 
fi

### called to uninstall your program
if [ $1 == 'uninstall' ]
then
uninstallme ;
echo "uninstaller program finished!" 
fi

