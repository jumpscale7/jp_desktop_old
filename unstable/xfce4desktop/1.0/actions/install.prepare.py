def main(j,jp):
   
    #prepare the platform before copying the files

    #remove gnome first
    do.execute("aptitude purge `dpkg --get-selections | grep gnome | cut -f 1` -y")
    do.execute("aptitude -f install")
    do.execute("aptitude purge `dpkg --get-selections | grep deinstall | cut -f 1` -y")
    do.execute("aptitude -f install")

    # can happen by e.g. installing a debian package e.g. by
    names=["xfce4","scribus","firefox","gimp","tuxcmd","evolution","pidgin","evince","openpro","gnucash","inkscape"]
    for packagename in names:
        j.system.platform.ubuntu.install(packagename)
       
    #install found debs they need to be in debs dir of one or more of the platforms (all relevant platforms will be used)
    #args.qp.installUbuntuDebs()
    
    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #copying files from files section of jpackages is not done in this step
    
    pass