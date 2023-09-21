# GIT

+ GitHub = Centrilized Hosting Service - CHS
+ Git = Revision Control System - RCS

Git is usefull: 

**Summary of Git's Key Features:**

- **Distributed Development:** Git facilitates parallel and independent development in private repositories, allowing for offline work. It offers flexibility not found in centralized version control systems.

- **Scalability:** Git seamlessly accommodates thousands of developers, ensuring the smooth integration of their contributions, making it suitable for large-scale projects.

- **Performance:** Prioritizing speed and efficiency, Git employs compression and delta checks to optimize data storage and transfer. This speed is crucial for projects like the Linux kernel.

- **Accountability and Immutability:** Git enforces a change log for every file modification, maintaining a clear history and reasons for changes. Data objects in Git remain immutable, enhancing accountability.

- **Atomic Transactions:** Git guarantees the integrity of repositories by ensuring related changes occur entirely or not at all, preventing incomplete or corrupted states.

- **Complete Repositories:** Each Git repository contains a comprehensive archive of all historical file revisions, preserving the project's entire version history.

- **Free and Open-Source:** Git's origins are rooted in the principles of free and open-source software, maintaining a liberal usage license that aligns with these values.

These features make Git a powerful and flexible version control system for developers and teams of all sizes.

# Install GIT
```bash
$ sudo apt update
$ sudo apt install -y git
& git --version
```

+ Verify Config Set:

```bash
$ git config --list
```

```bash
Output:

filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
credential.helper=/.codespaces/bin/gitcredential_github.sh
user.name=name = ER!CK;
user.email=38144008+ERICK-ZABALA@users.noreply.github.com
gpg.program=/.codespaces/bin/gh-gpgsign
init.defaultbranch=main

```

+ Set Username and Email:

```bash
$ git config --global user.name "ER!CK;"
```

```bash
$ git config --global user.email "erickzabala@hotmail.com"

```

# GITIGNORE
 
 That feature is useful to avoid upload files with sensitive information, ex API Keys, passwords, etc.

File: .gitignore

 ```bash
 # Byte-compiled / optimized / DLL files
pycache /
*.py[cod]
*$py.class
# OSX
# =========================
.DS_Store
.AppleDouble
.LSOverride
 ```
