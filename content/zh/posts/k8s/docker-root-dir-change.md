The standard data directory used by docker is /var/lib/docker, and since this directory will store all your images, volumes, etc. it can become quite large in a relative small amount of time.

If you want to move the docker data directory on another location you can follow the following simple steps.

# 1. Stop the docker daemon

```
sudo service docker stop
```

# 2. Add a configuration file to tell the docker daemon what is the location of the data directory

Create docker daemon configuration */etc/docker/daemon.json* with following content:

**Version before v17.05.0**

```
{ 
   "graph": "/path/to/your/new/docker/root" 
}
```

“"/path/to/your/new/docker/root”” is the new location you want to use for your new docker data directory.

**v17.05.0 and newer**

From v17.05.0, the `-g` or `--graph` flag for the `dockerd` or `docker daemon` command was used to indicate the directory in which to store persistent data and resource configuration and has been replaced with the more descriptive `--data-root` flag. We create daemon configuration file:

```
{ 
   "data-root": "/path/to/your/new/docker/root"
}
```

These flags “graph” were added before Docker 1.0, so will not be *removed*, only *hidden.* You still use this flag but simply discourage from using it.

# 3. Copy the current data directory to the new one

We can use both rsync and cp command:

```
sudo rsync -aP /var/lib/docker/ "/path/to/your/new/docker/root"sudo cp -rp /var/lib/docker/* "/path/to/your/new/docker/root/"
```

# 4. Rename the old docker directory

Rename old directory to ensure that docker daemon can’t use old directory.

```
sudo mv /var/lib/docker /var/lib/docker.old
```

# 5. Restart the docker daemon

```
sudo service docker start
```

# 6. Test

If everything is ok you should see no differences in using your docker containers.

# 7. Clean old data.

Alter all, we should clean old data:

```
rm -rf /var/lib/docker.old
```
