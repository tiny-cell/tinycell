#!/bin/bash
#/usr/bin/xvfb-run --server-args="-screen 0, 1024x768x24" python app.py
#/usr/bin/xvfb-run --server-args="-screen 0, 2560x1440x24" python app.py
/usr/bin/xvfb-run --server-args="-screen ${DISKPLAY_PORT:=0}, ${WINDOW_SIZE:=1024x768x24}" python app.py
