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
# GIT ADD & Commit:

```bash
$ git add .
$ git add myFile.txt
$ git commit -m "updated: Add myFile.txt"

```

# GIT LOG

Permit verify all commit and added file to your repository in order from new commits to old commits.

```bash
$ git log
```

Output:

```bash
commit 4473bea6bb05cec9c50f756a4b5332ceef53c1c1 (HEAD -> main)
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Thu Sep 21 05:11:59 2023 +0000

    updated: file gitignore

commit 74b0c115a600bfffcf9edc20ad26617260641fb3 (origin/main, origin/HEAD)
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Thu Sep 21 04:44:42 2023 +0000
:...skipping...
commit 4473bea6bb05cec9c50f756a4b5332ceef53c1c1 (HEAD -> main)
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Thu Sep 21 05:11:59 2023 +0000

    updated: file gitignore

commit 74b0c115a600bfffcf9edc20ad26617260641fb3 (origin/main, origin/HEAD)
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Thu Sep 21 04:44:42 2023 +0000

    updated: github

commit a1e59790ca14a6045c606aeffa08a7ea9c438436
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Wed Sep 20 03:40:43 2023 +0000

    updated docker

```

+ More information using Git ID: 

```bash
$ git show 4473bea6bb05cec9c50f756a4b5332ceef53c1c1
```

Output:

```bash
commit 4473bea6bb05cec9c50f756a4b5332ceef53c1c1 (HEAD -> main)
Author: name = ER!CK <38144008+ERICK-ZABALA@users.noreply.github.com>
Date:   Thu Sep 21 05:11:59 2023 +0000

    updated: file gitignore

diff --git a/.gitignore b/.gitignore
new file mode 100644
index 00000000..7c1a581f
```

# GIT REVERT

To revert changes, verify that you do not have any commit on queue using git status.

```bash
git revert 3bb043fbb1f5d279d6d6f7748e41920dba9e2f93
```

Output:

```bash
Auto-merging network/github/Readme.md
[main 075a97df] Revert "updated: file gitignore"
 1 file changed, 7 insertions(+), 2 deletions(-)

```



