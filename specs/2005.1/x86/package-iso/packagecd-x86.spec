subarch: x86
version_stamp: 2005.1
target: grp
rel_type: default
profile: default-linux/x86/2005.1
snapshot: current
source_subpath: default/stage3-x86-2005.1_pre1
grp: src cd2

grp/use: 
	bonobo 
	esd 
	gtkhtml 
	mozilla
	ruby
	tcltk
	ldap
	dvd
	dvdr
	cdr
	socks5
	fbcon

grp/src/type: srcset
grp/src/packages:
	dhcpcd
	slocate
	udev
	gentoo-sources
	vanilla-sources
	coldplug
	fxload
	syslog-ng
	logrotate
	raidtools
	nfs-utils
	jfsutils
	xfsprogs
	e2fsprogs
	reiserfsprogs
	rp-pppoe
	penggy
	iputils
	lvm2
	evms
	pptpclient
	mdadm
	ethtool
	wireless-tools
	prism54-firmware
	wpa_supplicant
	genkernel
	lilo
	grub
	dante
	tsocks
	splashutils
	splash-themes-livecd
	pcmcia-cs
	speedtouch
	slmodem
	globespan-adsl
	hostap-driver
	hostap-utils
	ipw2100
	ipw2200
	fritzcapi
	fcdsl
	acpid
	cryptsetup
	nvidia-kernel
	nvidia-glx
	ati-drivers
	alsa-lib
	alsa-oss
	alsa-utils
	alsa-driver

grp/cd2/type: pkgset
grp/cd2/packages:
	xorg-x11
	gentoo-sources
	irssi
	gpm
	parted
	links
	dosfstools
	ntfsprogs
	screen
	mirrorselect
	vim
	xscreensaver
	ide-smart
	netcat
	gpart
	gnupg
	sys-apps/eject
	minicom
	whois
	tcpdump
	cvs
	zip
	unzip
	partimage
	app-admin/sudo
	app-cdr/cdrtools
	gnome
	emacs
	dev-lang/ruby
	enlightenment
	kde-meta
	mozilla-firefox
	mozilla-thunderbird
	xfce4
	openbox
	fluxbox
	sylpheed
	openoffice-bin
	xemacs
	xmms
	abiword
	gaim
	xchat
	pan
	tetex
	k3b
	koffice
	samba
	nmap
	gradm
	ettercap
	mplayer
