#! /usr/bin/env bash
echo "publication"
cd ~/Public/mon_site/
# publication
make publish
make rsync_upload
