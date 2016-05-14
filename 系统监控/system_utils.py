
# -*- coding: utf-8 -*-
## 利用psutil 模块  获取系统信息
## 文档https://pythonhosted.org/psutil/
import psutil


print("系统信息")
print("cpu信息-------------------------------------------------------------------")
##此处是超线程
print("cpu核数",psutil.cpu_count())
print("cpu物理核数",psutil.cpu_count(logical=False))
# 1 表1秒 cpu利用率
print("cpu使用率%f%%"%psutil.cpu_percent(interval=1))
print("\n\n")
print("内存信息------------------------------------------------------------------")
mem=psutil.virtual_memory();
print(mem)
print("总内存",round(mem.total/(1024*1024*1024)),"G")
print("已用内存",round(mem.used/(1024*1024)),"M")
print("剩余内存",round(mem.free/(1024*1024)),"M")
print("可用内存",round(mem.available/(1024*1024)),"M")
print("内存使用率%f%%"%mem.percent)




print("磁盘信息-------------------------------------------------------------------")
print("磁盘所有分区信息",psutil.disk_partitions())

print("网络信息")
#网络地址
print(psutil.net_if_addrs())
print(psutil.net_io_counters())

print("分区状况",psutil.disk_usage("/"))
print("系统所有进程id",psutil.pids())