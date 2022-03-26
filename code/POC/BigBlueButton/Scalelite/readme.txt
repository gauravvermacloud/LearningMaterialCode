Do not use this, this installs scalelite inside docker

https://medium.com/@jesusfederico_39370/scalelite-lazy-deployment-745a7be849f6

Use this

https://github.com/blindsidenetworks/scalelite

Notes from Bharat Garg


Skip to content
Using Kranti Tech Services Pvt. Ltd. Mail with screen readers
Meet
Start a meeting
Join a meeting
Hangouts

8 of many
Scalelite doc

Bharat Garg
Attachments
Tue, Aug 18, 1:44 PM (1 day ago)
to me

Hi GV

Please find the attachment.

Regards
Bharat Garg
Attachments area
Received, thank you.Thanks a lot.Thanks for the mail.

Create BBB server:

wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s bbb.example.com -e info@example.com -g
wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s meetings.mel-jol.com -e mel-jol@startupglide.com -g

wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s bbb.example.com -e info@example.com -g -c turn.example.com:1234abcd

wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -c turn.example.com:1234abcd -e info@example.com



for turn server:

wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -c turn.mel-jol.in:Kranti@123 -e mel-jol@startupglide.com

for bbb server:

wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s dev1.mel-jol.in -e mel-jol@startupglide.com -g -c turn.mel-jol.in:Kranti@123
wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s dev2.mel-jol.in -e mel-jol@startupglide.com -g -c turn.mel-jol.in:Kranti@123


Scalelite:


https://github.com/blindsidenetworks/scalelite

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22

644223ca9d8498424e94f21d3c2819dc3c23a99de09f70c45cc2e8197dbbe8d5



bbb server:
# Create a new group with GID 2000
groupadd -g 2000 scalelite-spool
# Add the bigbluebutton user to the group
usermod -a -G scalelite-spool bigbluebutton

On the Scalelite server:
# Create the spool directory for recording transfer from BigBlueButton
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/spool
chown 1000:2000 /mnt/scalelite-recordings/var/bigbluebutton/spool
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/spool

# Create the temporary (working) directory for recording import
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite
chown 1000:1000 /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite

# Create the directory for published recordings
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/published
chown 1000:1000 /mnt/scalelite-recordings/var/bigbluebutton/published
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/published

# Create the directory for unpublished recordings
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/unpublished
chown 1000:1000 /mnt/scalelite-recordings/var/bigbluebutton/unpublished
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/unpublished


postgres:

psql -h 3.7.151.82 -U postgres
password:Kranti@123




redis:
redis-cli -h 3.7.151.82  -a kranti@123
sudo systemctl restart redis.service


set up user bbb server:

1. sudo useradd -m bigbluebutton
2. sudo groupadd -g 2000 scalelite-spool
3. sudo usermod -a -G scalelite-spool bigbluebutton
4. sudo passwd bigbluebutton
	---password is Kranti@123
5. mkdir -p ~/.ssh
6. chmod 0700 ~/.ssh
7. ssh-keygen(without pass phrase)
9. chmod 400 ~/.ssh/id_rsa
10. cat ~/.ssh/id_rsa.pub
	--paste on scalsalelite server
11. ~/.ssh/config   create file and channge as below
12. Host scalelite-recording.example.com
        User scalelite-spool
        IdentityFile ~/.ssh/id_rsa
13. wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s dev1.mel-jol.in -e mel-jol@startupglide.com -g -c turn.mel-jol.in:Kranti@123
    wget -qO- https://ubuntu.bigbluebutton.org/bbb-install.sh | bash -s -- -v xenial-220 -s dev2.mel-jol.in -e mel-jol@startupglide.com -g -c turn.mel-jol.in:Kranti@123

14. scalelite_post_publish.rb: install to the directory /usr/local/bigbluebutton/core/scripts/post_publish
    scalelite.yml: install to the directory /usr/local/bigbluebutton/core/scripts
    ---- sudo chmod +x scalelite_post_publish.rb 

set up scalelite:

1. sudo useradd -m scalelite-spool
2. sudo passwd scalelite-spool
	---password is Kranti@123
3. mkdir -p ~/.ssh
4. echo "key from bbb server" >> ~/.ssh/authorized_keys
5. chmod -R go= ~/.ssh
6. exit
7. sudo usermod -s /bin/bash scalelite-spool to change the shell
8. On the Scalelite server:
# Create the spool directory for recording transfer from BigBlueButton
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/spool
chown 1001:2000 /mnt/scalelite-recordings/var/bigbluebutton/spool
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/spool

# Create the temporary (working) directory for recording import
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite
chown 1001:1000 /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/recording/scalelite

# Create the directory for published recordings
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/published
chown 1001:1000 /mnt/scalelite-recordings/var/bigbluebutton/published
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/published

# Create the directory for unpublished recordings
mkdir -p /mnt/scalelite-recordings/var/bigbluebutton/unpublished
chown 1001:1000 /mnt/scalelite-recordings/var/bigbluebutton/unpublished
chmod 0775 /mnt/scalelite-recordings/var/bigbluebutton/unpublished


sudo chown scalelite-spool: /mnt/scalelite-recordings/var/bigbluebutton/spool

9. install docer :   https://docs.docker.com/install/linux/docker-ce/ubuntu/

-----uuid 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88

10.docker network create scalelite
------0108288b26bde3c90347944d07e359509096b93ac492460bcbc82a680b094bb6
    URL_HOST='mel-jol.in'
    SECRET_KEY_BASE='851fbf212cf00529b142c32f6483a1d10643bbd077f6e9111fb12e90a2d33101b8927c591d33204e10b9d2639ae678d41dfc1006c0dee7d2623abb4f3104a971'
    LOADBALANCER_SECRET='e78fdde529bd6ed8c374cc04dad78843fcf2a724ce5fc39eaee96ea69614d3b5'
    DATABASE_URL='postgresql://postgres:Kranti123@3.7.151.82'
    REDIS_URL='redis://:Kranti123@3.7.151.82'

https://dev2.mel-jol.in/bigbluebutton/api
3jW0CwikgEwI6ziYfZMPHzGLCvJKRjSIoXEIe0A
./bin/rake servers:add[https://dev2.mel-jol.in/bigbluebutton/api,3jW0CwikgEwI6ziYfZMPHzGLCvJKRjSIoXEIe0A]

17e2bed6-01a0-4483-ac11-a411d25fd0ab ./bin/rake servers:enable[17e2bed6-01a0-4483-ac11-a411d25fd0ab]
05f9f7be-1464-4ff2-a7fa-d2f93aff9a8d ./bin/rake servers:enable[05f9f7be-1464-4ff2-a7fa-d2f93aff9a8d]


Didnt work *****
            sudo docker run -d -P --name scalelite-nginx -v /etc/nginx/ssl/live/mel-jol.in/fullchain.pem:/etc/nginx/ssl/live/mel-jol.in/fullchain.pem nginx

            sudo docker run --name=nginx -d -v /etc/nginx/ssl/live/mel-jol.in/fullchain.pem:/etc/nginx/ssl/live/mel-jol.in/fullchain.pem nginx

            sudo docker run -d -P --name scalelite-nginx -v /etc/letsencrypt:/etc/letsencrypt nginx
Didnt work *****

            sudo docker exec -i scalelite-api bundle exec rake status


Show configured server details
./bin/rake servers

Add a server
./bin/rake servers:add[url,secret,loadMultiplier]

Remove a server
./bin/rake servers:remove[id]

Disable a server
./bin/rake servers:disable[id]

Enable a server
./bin/rake servers:enable[id]

Poll all servers
./bin/rake poll:all






scalelite.txt
Displaying scalelite.txt.

