# 0x01. Shell, permissions
## Foundations > System engineering & DevOps > Bash

chmod u+x file
### Tasks


------------


#### 0. My name is Betty
Create a script that switches the current user to the user betty.


- You should use exactly 8 characters for your command (+1 character for the new line)
- You can assume that the user betty will exist when we will run your script


```shell
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$

```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 0-iam_betty

##### answer

```shell
#!/bin/bash
su betty

```

su -- substitute user identity

The su utility requests appropriate user credentials via PAM and switches to that user ID (the default user is the superuser).  A shell is then executed.

------------


#### 1. Who am I
Write a script that prints the effective username of the current user.

```shell
julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$

```

**Repo**:

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 1-who_am_i


##### answer

```shell
#!/bin/bash
id -un

```
 id -- return user identity

The historic whoami(1) command is equivalent to ``id -un''.

------------


#### 2. Groups
Write a script that prints all the groups the current user is part of.

```shell
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$

```
Note: depending on the user, you will get a different output.

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 2-groups

##### answer

```shell
#!/bin/bash
id -Gn

```
The historic groups(1) command is equivalent to ``id -Gn [user]''

------------


#### 3. New owner
Write a script that changes the owner of the file hello to the user betty.

```shell
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$

```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 3-new_owner

##### answer

```shell
#!/bin/bash
chown betty hello

```
chown -- change file owner and group
The chown utility changes the user ID and/or the group ID of the specified files.  Symbolic links named by arguments are silently left unchanged unless -h is used.

------------


#### 4. Empty!
Write a script that creates an empty file called hello.

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 4-empty

##### answer

```shell
#!/bin/bash
touch hello

```
touch -- change file access and modification times
The touch utility sets the modification and access times of files.  If any file does not exist, it is created with default permissions.

------------


#### 5. Execute
Write a script that adds execute permission to the owner of the file hello.

- The file hello will be in the working directory

```shell
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 5-execute

##### answer

```shell
#!/bin/bash
chmod u+x hello

```
chmod -- change file modes or Access Control Lists
u = The user permission bits in the original mode of the file.
x = The execute/search bits.
+ = If no value is supplied for perm, the "+'' operation has no effect.  If no value is supplied for who, each permission bit specified in perm, for which the corresponding bit in the file mode creation mask (see umask(2)) is clear, is set.  Otherwise, the mode bits represented by the specified who and perm values are set
------------


#### 6. Multiple permissions
Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

- The file hello will be in the working directory

```shell
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$

```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 6-multiple_permissions

##### answer

```shell
#!/bin/bash
chmod u+x,g+x,o+r hello

```
r = The read bits.
g = The group permission bits in the original mode of the file.
o = The other permission bits in the original mode of the file.

------------


#### 7. Everybody!
Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello

- The file hello will be in the working directory
- You are not allowed to use commas for this script

```shell
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

GitHub repository: holberton-system_engineering-devops
Directory: 0x01-shell_permissions
File: 7-everybody

##### answer

```shell
#!/bin/bash
chmod ugo+x hello

```

------------


#### 8. James Bond
Write a script that sets the permission to the file hello as follows:

- Owner: no permission at all
- Group: no permission at all
- Other users: all the permissions
The file hello will be in the working directory You are not allowed to use commas for this script

```shell
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```
**Repo:**

GitHub repository: holberton-system_engineering-devops
Directory: 0x01-shell_permissions
File: 8-James_Bond

##### answer

```shell
#!/bin/bash
chmod 007 hello

```

------------


#### 9. John Doe
Write a script that sets the mode of the file hello to this:
```shell
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
```
- The file hello will be in the working directory
- You are not allowed to use commas for this script

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 9-John_Doe

##### answer

```shell
#!/bin/bash
chmod 753 hello

```

------------


#### 10. Look in the mirror
Write a script that sets the mode of the file hello the same as olleh’s mode.

- The file hello will be in the working directory
- The file olleh will be in the working directory

```shell
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$
```
Note: the mode of olleh will not always be 664. Make sure your script works for any mode.

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 10-mirror_permissions

##### answer

```shell
#!/bin/bash
chmod --reference=olleh hello

```

------------


#### 11. Directories
Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

```shell
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 11-directories_permissions

##### answer

```shell
#!/bin/bash
chmod -R ugo+x

```

------------


#### 12. More directories
Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.

```shell
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 12-directory_permissions

##### answer

```shell
#!/bin/bash
mkdir -m 751 dir_holberton

```

------------


#### 13. Change group
Write a script that changes the group owner to holberton for the file hello

- The file hello will be in the working directory

```shell
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien holberton   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 13-change_group

##### answer

```shell
#!/bin/bash
chgrp holberton hello

```

------------


#### 14. Owner and group
Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

```shell
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change_owner_and_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 betty holberton   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir0
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir1
drwx--x--x 2 betty holberton 4096 Sep 20 14:49 dir2
drwxr-x--x 2 betty holberton 4096 Sep 20 14:59 dir_holberton
-rw-rw-r-- 1 betty holberton   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 100-change_owner_and_group

##### answer

```shell
#!/bin/bash
chown -Rh betty:holberton

```

------------


#### 15. Symbolic links
Write a script that changes the owner and the group owner of _hello to betty and holberton respectively.

- The file _hello is in the working directory
- The file _hello is a symbolic link

```shell
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic_link_permissions
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 betty  holberton    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$
```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 101-symbolic_link_permissions

##### answer

```shell
#!/bin/bash
chown -h betty:holberton _hello

```

------------


#### 16. If only
Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.

- The file hello will be in the working directory

```shell
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if_only
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 betty  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```
**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 102-if_only

##### answer

```shell
#!/bin/bash
chown --from=guillaume betty hello

```

------------


#### 17. Star Wars
Write a script that will play the StarWars IV episode in the terminal.

**Repo:**

- GitHub repository: holberton-system_engineering-devops
- Directory: 0x01-shell_permissions
- File: 103-Star_Wars

##### answer

```shell
#!/bin/bash
telnet towel.blinkenlights.nl

```

------------





