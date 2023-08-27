
sudo apt update
sudo apt install python

python --version

sudo apt install default-jdk
sudo apt install xsltproc
sudo apt install make
sudo apt install ant
sudo apt-get install dash

download link: https://developer.cisco.com/fileMedia/download/119b2bc7-dbf6-49a1-974d-0a5610e41390/
file: nso-5.1.0.1.linux.x86_64.signed.bin


devnett@PC1 ~/devnet/DEVNET $ cd nso
devnet@PC1 ~/devnet/DEVNET/nso $ ls

lab01

devnet@PC1 ~/devnet/DEVNET/nso $ python3 -m venv nso
devnet@PC1 ~/devnet/DEVNET/nso $ source nso/bin/activate

(nso) devnet@PC1 ~/devnet/DEVNET/nso $ cd ..
(nso) devnet@PC1 ~/devnet/DEVNET $ ls
cisco_x509_verify_release.py  netconf  nso-5.1.0.1.linux.x86_64.installer.bin            README.md         webex
cucm                          nexus    nso-5.1.0.1.linux.x86_64.installer.bin.signature  README.signature
index.html                    nso      nso-5.1.0.1.linux.x86_64.signed.bin               tailf.cer
(nso) devnet@PC1 ~/devnet/DEVNET $ ls -ll
total 363520
-rw-r--r-- 1 devnet devnet     12381 Apr 14  2019 cisco_x509_verify_release.py
drwxr-xr-x 3 devnet devnet      4096 Aug 20 00:15 cucm
-rw-r--r-- 1 devnet devnet      6207 Aug 26 15:23 index.html
drwxr-xr-x 4 devnet devnet      4096 Aug 19 19:37 netconf
drwxr-xr-x 3 devnet devnet      4096 Aug 20 12:16 nexus
drwxr-xr-x 4 devnet devnet      4096 Aug 26 15:47 nso
-rwxr-xr-x 1 devnet devnet 186085011 Apr 14  2019 nso-5.1.0.1.linux.x86_64.installer.bin
-rw-r--r-- 1 devnet devnet       256 Apr 14  2019 nso-5.1.0.1.linux.x86_64.installer.bin.signature
-rw-r--r-- 1 devnet devnet 186095449 Aug 26 13:58 nso-5.1.0.1.linux.x86_64.signed.bin
-rw-r--r-- 1 devnet devnet      2162 Aug 21 02:49 README.md
-rw-r--r-- 1 devnet devnet      1832 Apr 14  2019 README.signature
-rw-r--r-- 1 devnet devnet      1383 Apr 14  2019 tailf.cer
drwxr-xr-x 3 devnet devnet      4096 Aug 26 15:23 webex

sh nso-5.1.0.1.linux.x86_64.signed.bin

(nso) devnet@PC1 ~/devnet/DEVNET $ sh nso-5.1.0.1.linux.x86_64.signed.bin
Unpacking...
Verifying signature...
Downloading CA certificate from http://www.cisco.com/security/pki/certs/crcam2.cer ...
Successfully downloaded and verified crcam2.cer.
Downloading SubCA certificate from http://www.cisco.com/security/pki/certs/innerspace.cer ...
Successfully downloaded and verified innerspace.cer.
Successfully verified root, subca and end-entity certificate chain.
Successfully fetched a public key from tailf.cer.
Successfully verified the signature of nso-5.1.0.1.linux.x86_64.installer.bin using tailf.cer

(nso) devnet@PC1 ~/devnet/DEVNET $ ls
cisco_x509_verify_release.py  netconf  nso-5.1.0.1.linux.x86_64.installer.bin            README.md         webex
cucm                          nexus    nso-5.1.0.1.linux.x86_64.installer.bin.signature  README.signature
index.html                    nso      nso-5.1.0.1.linux.x86_64.signed.bin               tailf.cer
(nso) devnet@PC1 ~/devnet/DEVNET $ ls -ll
total 363520
-rw-r--r-- 1 devnet devnet     12381 Apr 14  2019 cisco_x509_verify_release.py
drwxr-xr-x 3 devnet devnet      4096 Aug 20 00:15 cucm
-rw-r--r-- 1 devnet devnet      6207 Aug 26 15:23 index.html
drwxr-xr-x 4 devnet devnet      4096 Aug 19 19:37 netconf
drwxr-xr-x 3 devnet devnet      4096 Aug 20 12:16 nexus
drwxr-xr-x 4 devnet devnet      4096 Aug 26 15:47 nso
-rwxr-xr-x 1 devnet devnet 186085011 Apr 14  2019 nso-5.1.0.1.linux.x86_64.installer.bin
-rw-r--r-- 1 devnet devnet       256 Apr 14  2019 nso-5.1.0.1.linux.x86_64.installer.bin.signature
-rw-r--r-- 1 devnet devnet 186095449 Aug 26 13:58 nso-5.1.0.1.linux.x86_64.signed.bin
-rw-r--r-- 1 devnet devnet      2162 Aug 21 02:49 README.md
-rw-r--r-- 1 devnet devnet      1832 Apr 14  2019 README.signature
-rw-r--r-- 1 devnet devnet      1383 Apr 14  2019 tailf.cer
drwxr-xr-x 3 devnet devnet      4096 Aug 26 15:23 webex

# Install

sh nso-5.1.0.1.linux.x86_64.installer.bin $HOME/nso-5.1 --local-install

(nso) devnet@PC1 ~/devnet/DEVNET $ sh nso-5.1.0.1.linux.x86_64.installer.bin $HOME/nso-5.1 --local-install
INFO  Using temporary directory /tmp/ncs_installer.12357 to stage NCS installation bundle
INFO  Unpacked ncs-5.1.0.1 in /home/devnet/nso-5.1
INFO  Found and unpacked corresponding DOCUMENTATION_PACKAGE
INFO  Found and unpacked corresponding EXAMPLE_PACKAGE
INFO  Generating default SSH hostkey (this may take some time)
INFO  SSH hostkey generated
INFO  Environment set-up generated in /home/devnet/nso-5.1/ncsrc
INFO  NCS installation script finished
INFO  Found and unpacked corresponding NETSIM_PACKAGE
INFO  NCS installation complete

(nso) devnet@PC1 ~/devnet/DEVNET $ cd $home
(nso) devnet@PC1 ~ $ ls
devnet  lnx-terminal-color  nso-5.1  pipwin  yangsuite

(nso) devnet@PC1 ~ $ source nso-5.1/ncsrc
(nso) devnet@PC1 ~ $ ls
devnet  lnx-terminal-color  nso-5.1  pipwin  yangsuite
(nso) devnet@PC1 ~ $ pwd
/home/devnet

(nso) devnet@PC1 ~ $ cd nso-5.1/

(nso) devnet@PC1 ~/nso-5.1 $ ls
bin      doc     etc           include  lib      man    ncsrc.tcsh  packages  scripts  support  VERSION
CHANGES  erlang  examples.ncs  java     LICENSE  ncsrc  netsim      README    src      var

(nso) devnet@PC1 ~/nso-5.1 $ cd ..

(nso) devnet@PC1 ~ $ ls

devnet  lnx-terminal-color  nso-5.1  pipwin  yangsuite

cd $home
source nso-5.1/ncsrc
ncs-setup --dest $HOME/ncs-run

(nso) devnet@PC1 ~ $ source nso-5.1/ncsrc
(nso) devnet@PC1 ~ $ ncs-setup --dest $HOME/ncs-run

# Copy Cisco Images and configs
cp -R nso-5.1/packages/neds/cisco-ios-cli-3.0 ncs-run/packages/cisco-ios-cli-3.0

cd ncs-run
ncs-netsim create-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 3 c

### Configuration ###

(nso) devnet@PC1 ~ $ cp -R nso-5.1/packages/neds/cisco-ios-cli-3.0 ncs-run/packages/cisco-ios-cli-3.0
(nso) devnet@PC1 ~ $ cd ncs-run/
(nso) devnet@PC1 ~/ncs-run $ ls
logs  ncs-cdb  ncs.conf  packages  README.ncs  scripts  state
(nso) devnet@PC1 ~/ncs-run $ echo $NCS_DIR
/home/devnet/nso-5.1
(nso) devnet@PC1 ~/ncs-run $ ncs-netsim create-network $NCS_DIR/packages/neds/cisco-ios-cli-3.0 3 c
DEVICE c0 CREATED                                                     
DEVICE c1 CREATED
DEVICE c2 CREATED
(nso) devnet@PC1 ~/ncs-run $ 
####

# Start Simulation 3 routers c0 c1 c2
ncs-netsim start

devnet@PC1 ~/ncs-run $ ncs-netsim start
./start.sh: 12: ./env.sh: Syntax error: "(" unexpected
DEVICE c0 FAIL
./start.sh: 12: ./env.sh: Syntax error: "(" unexpected
DEVICE c1 FAIL
./start.sh: 12: ./env.sh: Syntax error: "(" unexpected
DEVICE c2 FAIL

# Start Simukation
ncs-netsim start

# Enter CLI C1
ncs-netsim cli-i c1

en show run

exi

dmin@ncs> exit
@ERICK-ZABALA ➜ ~/ncs-run $ ncs-netsim cli-i c1

admin connected from 127.0.0.1 using console on codespaces-870877
c1> en
c1# sh run
----^
syntax error: ambiguous command
Possible alternatives starting with sh:
  show          - Show information about the system
  show-defaults - Show default values when showing the configuration
c1# show run
no service pad
no ip domain-lookup
no ip http server
no ip http secure-server
ip routing
ip source-route
ip vrf my-forward
 bgp next-hop Loopback 1
!
ip community-list 1 permit
ip community-list 2 deny
ip community-list standard s permit
interface FastEthernet1/0
exit
interface Loopback0
exit
class-map match-all a
!
class-map match-all cmap1
 match mpls experimental topmost 1
 match packet length max 255
 match packet length min 2
 match qos-group 1
!
policy-map a
!
policy-map map1
 class c1
  drop
  estimate bandwidth delay-one-in 500 milliseconds 100
  priority percent 33
 !
!
no spanning-tree optimize bpdu transmission
mpls ip propagate-ttl
router bgp 64512
 aggregate-address 10.10.10.1 255.255.255.251
 neighbor 1.2.3.4 remote-as 1
 neighbor 1.2.3.4 ebgp-multihop 3
 neighbor 2.3.4.5 remote-as 1
 neighbor 2.3.4.5 activate
 neighbor 2.3.4.5 capability orf prefix-list both
 neighbor 2.3.4.5 weight 300
!
c1# exit

ncs-setup --netsim-dir ./netsim --dest .

# Start NCS

ncs
 
@ERICK-ZABALA ➜ ~/ncs-run $ 
@ERICK-ZABALA ➜ ~/ncs-run $ ncs --status | grep status
status: started
        db=running id=31 priority=1 path=/ncs:devices/device/live-status-protocol/device-type
@ERICK-ZABALA ➜ ~/ncs-run $ ncs_cli -u admin
 
ncs_cli -u admin

admin@ncs> show configuration devices device
device c0 {
    address   127.0.0.1;
    port      10022;
    ssh {
        host-key ssh-rsa {
            key-data "AAAAB3NzaC1yc2EAAAADAQABAAABgQDEcaG+0EVoFEGKfXBLwE2m/Xj0U/SimA3ir4Hprtq5\ntZ1EAdNRi5V8pV/E8yhf5g6uL6zrTAeoJZqH661uiKJmey8QKAE78iLQ6YmpamOOGTJx0uN0\nUCfPAxZwNyGTeaBtUzK3yUmHu2cDaTk3upxL1fqjUfsy4ntnDz+D+13qC6yleord6WzgHPrh\nR2gI7dV+9YPfJzK63tpBq8+pIcIf6vdJ4tbn4te2rKP3PLs1+sd8qhDn7LkjfthF1V6Hpr17\nllai6rEcxWY0LX9MbzZzMLkSeM5KeU9eV89DpF8rdgIGq/1V4Pp4gIBYA11eQ/ua7+dNooVA\ntafMsuMKt5wYrK+kuuMB4OR10h1p2KDCR+J80Mbp1pAQh7rLtqEi0atoTj45eXcjcuGziWKA\nMviw9W8YJJsUwtbbjgq1HJbAnoeqh/WKb6EB5SqbKqwZ0/u/MuKn6Jt/HxC+6LW/3FpHuwkx\nb5UITKFUD0ZkyW5ZDNcxIwoNHA+DiL9YmHFRpZU=";
        }
    }
    authgroup default;
    device-type {
        cli {
            ned-id cisco-ios-cli-3.0;
        }
    }
    state {
        admin-state unlocked;
    }
}
device c1 {
    address   127.0.0.1;
    port      10023;
    ssh {
        host-key ssh-rsa {
            key-data "AAAAB3NzaC1yc2EAAAADAQABAAABgQDEcaG+0EVoFEGKfXBLwE2m/Xj0U/SimA3ir4Hprtq5\ntZ1EAdNRi5V8pV/E8yhf5g6uL6zrTAeoJZqH661uiKJmey8QKAE78iLQ6YmpamOOGTJx0uN0\nUCfPAxZwNyGTeaBtUzK3yUmHu2cDaTk3upxL1fqjUfsy4ntnDz+D+13qC6yleord6WzgHPrh\nR2gI7dV+9YPfJzK63tpBq8+pIcIf6vdJ4tbn4te2rKP3PLs1+sd8qhDn7LkjfthF1V6Hpr17\nllai6rEcxWY0LX9MbzZzMLkSeM5KeU9eV89DpF8rdgIGq/1V4Pp4gIBYA11eQ/ua7+dNooVA\ntafMsuMKt5wYrK+kuuMB4OR10h1p2KDCR+J80Mbp1pAQh7rLtqEi0atoTj45eXcjcuGziWKA\nMviw9W8YJJsUwtbbjgq1HJbAnoeqh/WKb6EB5SqbKqwZ0/u/MuKn6Jt/HxC+6LW/3FpHuwkx\nb5UITKFUD0ZkyW5ZDNcxIwoNHA+DiL9YmHFRpZU=";
        }
    }
    authgroup default;
    device-type {
        cli {
            ned-id cisco-ios-cli-3.0;
        }
    }
    state {
        admin-state unlocked;
    }
}
device c2 {
    address   127.0.0.1;
    port      10024;
    ssh {
        host-key ssh-rsa {
            key-data "AAAAB3NzaC1yc2EAAAADAQABAAABgQDEcaG+0EVoFEGKfXBLwE2m/Xj0U/SimA3ir4Hprtq5\ntZ1EAdNRi5V8pV/E8yhf5g6uL6zrTAeoJZqH661uiKJmey8QKAE78iLQ6YmpamOOGTJx0uN0\nUCfPAxZwNyGTeaBtUzK3yUmHu2cDaTk3upxL1fqjUfsy4ntnDz+D+13qC6yleord6WzgHPrh\nR2gI7dV+9YPfJzK63tpBq8+pIcIf6vdJ4tbn4te2rKP3PLs1+sd8qhDn7LkjfthF1V6Hpr17\nllai6rEcxWY0LX9MbzZzMLkSeM5KeU9eV89DpF8rdgIGq/1V4Pp4gIBYA11eQ/ua7+dNooVA\ntafMsuMKt5wYrK+kuuMB4OR10h1p2KDCR+J80Mbp1pAQh7rLtqEi0atoTj45eXcjcuGziWKA\nMviw9W8YJJsUwtbbjgq1HJbAnoeqh/WKb6EB5SqbKqwZ0/u/MuKn6Jt/HxC+6LW/3FpHuwkx\nb5UITKFUD0ZkyW5ZDNcxIwoNHA+DiL9YmHFRpZU=";
        }
    }
    authgroup default;
    device-type {
        cli {
            ned-id cisco-ios-cli-3.0;
        }
    }
    state {
        admin-state unlocked;
    }
}
[ok][2023-08-26 22:52:31]
admin@ncs> exi

