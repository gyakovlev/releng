subarch: ppc64
target: stage1
version_stamp: 32ul-2008.0
rel_type: default
profile: default/linux/powerpc/ppc64/17.0/32bit-userland
snapshot: 2008.0
source_subpath: default/stage3-ppc64-32ul-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world --jobs 5 --load-average 5
chost: powerpc-unknown-linux-gnu
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
