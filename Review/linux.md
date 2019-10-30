## 处理目录常用的命令

ls：列出目录

cd：切换目录

pwd：查看当前所在路径

mkdir：创建一个新的目录

rmdir：删除一个空的目录

cp：复制文件或目录

rm：移除文件或目录

mv：移动文件或目录，或修改文件与目录的名称



##  文件内容查看

cat：从第一行开始显示文件内容

tac：从最后一行开始显示，可以看出tac是cat的倒着写

nl：显示的时候，顺道输出行号

more：一页一页的显示文件内容

less：与more类似，但是比more更好的是，可以往前翻页

head：只看头几行

tail：只看尾巴几行、



## Linux磁盘管理

常用三个命令为 df、duhe fdisk

* df：列出文件系统的整体磁盘使用量
* du：检查磁盘空间使用量，与df命令不同的是Linux du命令是对文件和目录磁盘使用的空间的查看，
* fdisk：用于磁盘分区

**磁盘格式化：**

mkfs[-t  文件系统格式] 装置文件名



**磁盘检验：**

fsck（file system check）用来检查和维护不一致的文件系统。

若系统掉电或磁盘发生问题，可利用fsck命令对文件系统进行检查。

语法：

```
fsck [-t 文件系统] [-ACay] 装置名称
```



**磁盘挂载与卸除**

Linux 的磁盘挂载使用 `mount` 命令，卸载使用 `umount` 命令。

磁盘挂载语法：

```
mount [-t 文件系统] [-L Label名] [-o 额外选项] [-n]  装置文件名  挂载点
```



[Linux 常用命令全拼](https://www.cnblogs.com/yjd_hycf_space/p/7730690.html)

