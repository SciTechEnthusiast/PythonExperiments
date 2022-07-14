
**Sonar requirements**

*Fire below commands in wsl*

```console 
sysctl -w vm.max_map_count=524288
sysctl -w fs.file-max=131072
ulimit -n 131072
ulimit -u 8192
```



Download sonar scanner from belwo link and add it to path 