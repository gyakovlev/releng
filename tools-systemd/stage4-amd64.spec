subarch: SARCH
target: CSTAGE
version_stamp: systemd
rel_type: systemd/SARCH
profile: default/linux/PARCH/17.1/systemd
snapshot: current
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
source_subpath: systemd/SARCH/PSTAGE-SARCH-systemd
portage_confdir: @REPO_DIR@/tools-musl/portage.amd64.hardened.stage4

stage4/use:
	bash-completion
	bindist
	bzip2
	idm
	ipv6
	mmx
	sse
	sse2
	urandom

stage4/packages:
	net-misc/dhcp
	net-misc/iputils
	sys-boot/grub
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-devel/bc
	sys-power/acpid
	app-crypt/gentoo-keys
stage4/fsscript: @REPO_DIR@/releases/weekly/scripts/cloud-prep.sh
stage4/rcadd:
	acpid|default
	net.lo|default
	netmount|default
	sshd|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: @REPO_DIR@/releases/weekly/kconfig/amd64/cloud-amd64-gentoo.config
boot/kernel/gentoo/extraversion: openstack
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules

# all of the cleanup...
stage4/unmerge:
	sys-devel/bc
	sys-kernel/genkernel
	sys-kernel/gentoo-sources

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
	/var/cache/portage/distfiles
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz
