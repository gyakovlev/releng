subarch: ia64
version_stamp: latest
target: stage1
rel_type: default
profile: default/linux/ia64/17.0
snapshot: latest
source_subpath: default/stage3-ia64-latest
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
portage_prefix: releng
