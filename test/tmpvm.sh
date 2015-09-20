docker run -it --rm=true -p 5000 -v /srv/app:/src -v /root:/root --entrypoint=/bin/bash arkii/casperjs
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app -v /root:/root arkii/ghost.py:v000 /bin/bash
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app -v /root:/root debian /bin/bash
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app busybox:ubuntu-14.04 /bin/sh
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app arkii/ghost.py:v0 /bin/bash
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app arkii/ghost.py:v1 /bin/bash
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app arkii/ghost.py:v2 /bin/bash
#docker run -it --rm=true -p 5000 -w /app/src -v /srv/app:/app arkii/ghost.py:v0 /bin/bash
#docker run -it --rm=true -p 5000  -v /root/build:/root/build arkii/ghost.py:v0 /bin/bash
#docker run -it --rm=true -P -v /root/build:/root/build centos:7 /bin/bash
