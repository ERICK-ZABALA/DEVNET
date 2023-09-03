# ANSIBLE

# Install Ansible OS

$ sudo apt update
$ sudo apt-get install software-properties-common
$ sudo apt-add-repository ppa:ansible/ansible
$ sudo apt-get install ansible

$ ansible --version

+ ping your target
$ ansible -i hosts 172.16.5.4 -m ping
+ see detailed info about your target
$ ansible -i hosts 172.16.5.4 -m setup 

Nota:

Los módulos de Ansible son código Python que se ejecuta en el host remoto de forma predeterminada. Sin embargo, muchos equipos de red no tienen Python disponible o simplemente no lo tienen instalado. Por eso, en la mayoría de los casos, Ansible ejecuta el conjunto de instrucciones (o "playbook") en el servidor de control (la máquina desde la que se ejecuta Ansible) en lugar de hacerlo en el equipo remoto. Esto significa que el conjunto de instrucciones primero se interpreta localmente en el servidor de control y luego se envían comandos o configuraciones al equipo remoto según sea necesario.

Ejecutando $ ansible -i hosts 172.16.5.4 -m setup;
Como estamos ejecutando el conjunto de instrucciones localmente en el servidor de control, el módulo "setup" recopilará información en el servidor de control en lugar del equipo remoto. Esto no es necesario, por lo que cuando la conexión se establece como "local", para evitar este paso innecesario desactivando la obtención de información ("fact gathering") o estableciéndola en "no" o "false". Dado que los módulos de red se ejecutan localmente (en el servidor de control), para aquellos módulos que ofrecen una opción de copia de seguridad, los archivos se respaldan localmente en el nodo de control también.

En otras palabras, cuando se ejecutan módulos de Ansible relacionados con redes en el servidor de control, algunos de estos módulos tienen la capacidad de realizar copias de seguridad de ciertos archivos de configuración o datos en el servidor de control antes de aplicar cambios en los equipos de red. Estos archivos de copia de seguridad se almacenan localmente en el servidor de control para que estén disponibles en caso de que se necesiten en el futuro. Esto puede ser útil para recuperar la configuración anterior en caso de que ocurra algún problema durante la ejecución del módulo de Ansible.

Available 2.5 Ansible: network_cli, netconf, httpapi, ios-commnad-module and local.


