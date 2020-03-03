# Devops Lab 2019 Python Task3 "Snapshots Application"
# by Andrei Leanovich

**Description:**
1. This application takes following system metrics:
  - CPU load percent,
  - Disk space used,
  - RAM used,
  - Disk IO write time,
  - Network Information.
2. Default interval between snapshots - 300 in seconds
3. Output file have default format txt (possible options txt and json)


**Requirements:**

Python version 3.6 or above

Installed psutil with pip

**Installation:**
Clone the repo and navigate to this folder.

  $ pip install .

  $ snapshot

**Uninstallation:**

  $ pip uninstall snapshot

**Examples of use:**

  $ snapshot

  $ snapshot 350 json

  $ snapshot 80 txt
