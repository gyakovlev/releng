subarch: amd64
target: stage3
version_stamp: hardened-selinux-@TIMESTAMP@
rel_type: hardened
profile: default/linux/amd64/17.1/hardened/selinux
snapshot: @TIMESTAMP@
source_subpath: hardened/stage2-amd64-hardened-selinux-@TIMESTAMP@
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng