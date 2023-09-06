# Jenkins
Para los ingenieros que han trabajado en un entorno de red grande, comprenden que las consecuencias de una modificación de red mal ejecutada pueden ser significativas. Podemos implementar cientos de cambios sin problemas, pero basta con una modificación errónea para que la red tenga un impacto negativo en todo el negocio.

Dada la posible complejidad y el impacto, en muchos entornos de redes se utiliza un Comité Asesor de Cambios (CAB). El proceso típico del CAB es:

1. El ingeniero de redes diseña y documenta los pasos del cambio, incluyendo la razón, dispositivos involucrados, comandos, verificación y resultados esperados.

2. Se solicita una revisión técnica por parte de un compañero, que varía según la complejidad del cambio: simple (un compañero) o complejo (ingeniero senior).

3. El ingeniero presenta el cambio al comité, que realiza preguntas, evalúa el impacto y aprueba o rechaza la solicitud de cambio.

5. El cambio se lleva a cabo durante la ventana de cambio programada, ya sea por el ingeniero original o por otro ingeniero.

Sin embargo, este proceso presenta desafíos en la práctica:

- La documentación lleva mucho tiempo, ya que es necesario detallar cada paso debido al potencial impacto.
- La disponibilidad de ingenieros con experiencia es limitada, y su tiempo debe reservarse para problemas más complejos.
- Las reuniones son costosas en tiempo y pueden ser difíciles de organizar, especialmente si alguien clave está ausente.

Estos son algunos de los desafíos del proceso basado en humanos del CAB. Ahora se explorará una alternativa potencial para el CAB y la gestión de cambios en general, que se ha adoptado en el mundo de la ingeniería de software.

CI: El desarrollo de software implica hacer cambios pequeños y rápidos en el código, con pruebas automáticas para asegurarse de que no rompan el sistema.

En resumen, el proceso de Integración Continua (CI) busca acortar el camino desde la idea hasta el cambio en el código. El flujo de trabajo generalmente involucra los siguientes pasos:

1. Un ingeniero toma una copia actual del código base y realiza su modificación.
2. El ingeniero envía la modificación al repositorio.
3. El repositorio notifica a un grupo de ingenieros para revisar y aprobar o rechazar la modificación.
4. El sistema CI verifica continuamente el repositorio en busca de cambios o recibe notificaciones del repositorio.
5. El sistema CI ejecuta pruebas automatizadas para identificar posibles problemas.
6. Si no se encuentran errores, el sistema CI puede fusionar la modificación en el código principal y, opcionalmente, implementarla en el sistema de producción.

Estos son pasos generales, y el proceso puede variar según la organización, como la ejecución de pruebas automáticas antes de la revisión del código o la inclusión de un ingeniero humano para comprobaciones adicionales. 

# Install Jenkins

$ sudo apt install openjdk-11-jre-headless

$ java --version

openjdk 11.0.4 2019-07-16
OpenJDK Runtime Environment (build 11.0.4+11-post-Ubuntu-1ubuntu218.04.3)
OpenJDK 64-Bit Server VM (build 11.0.4+11-post-Ubuntu-1ubuntu218.04.3,
mixed mode, sharing)

$ curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins


$ sudo service jenkins enable
$ sudo service jenkins start
$ sudo service jenkins status

Explorer:
http://172.30.157.251:8080/

$ sudo nano  /var/lib/jenkins/secrets/initialAdminPassword
c3726e11c7784f77...

IOS XR	
10.10.20.173
cisco / cisco
telnet
core-rtr01

IOS XR
10.10.20.174
cisco / cisco
telnet
core-rtr02

![Alt text](image.png)

![Alt text](image-1.png)

# Execute Python Script Jenkins


```bash

#!/bin/sh

pwd
ls -ll
# Definir la contraseña de "devnet"
password="devnet"
# Cambiar al usuario "devnet" e iniciar una sesión de shell, proporcionando la contraseña
echo "$password" | su -c "python3 /home/devnet/devnet/DEVNET/jenkins/conx_telnet_rtr01_v2.py" - devnet

```

![Alt text](image-2.png)

### Dar permisos sudo a usuario jenkins como root (no recomendado)

devnet@PC1 ~/devnet/DEVNET/jenkins $ sudo usermod -aG sudo jenkins
[sudo] password for devnet: 
devnet@PC1 ~/devnet/DEVNET/jenkins $ sudo -l -U jenkins
Matching Defaults entries for jenkins on PC1:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User jenkins may run the following commands on PC1:
    (ALL : ALL) ALL
devnet@PC1 ~/devnet/DEVNET/jenkins $ id jenkins
uid=102(jenkins) gid=113(jenkins) groups=113(jenkins),27(sudo)

$ sudo vi /etc/sudoers

Add:
jenkins ALL=NOPASSWD:/path of script/