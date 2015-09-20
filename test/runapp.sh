docker run -d -p 32809:5000 -e WINDOW_SIZE=2560x1440x24 -v /srv/app/tinycell_test:/srv/app arkii/ghost.py
#docker run  --rm=true -p 32809:5000 -e WINDOW_SIZE=2560x1440x24 -v /srv/app/tinycell_test:/srv/app arkii/ghost.py
#docker run -it --rm=true -p 80:5000 -w /srv/app/tinycell_test:/srv/app arkii/ghost.py
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app arkii/ghost.py:v0 /bin/bash
#docker run -it --rm=true -p 5000  -v /root/build:/root/build arkii/ghost.py:v0 /bin/bash
#docker run -it --rm=true -P -v /root/build:/root/build centos:7 /bin/bash
