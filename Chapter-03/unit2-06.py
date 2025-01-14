# 多进程案例，多并发视频拷贝器

# 需求分析
# 1.目标文件夹是否存在，如果不存在就不创建，如果存在则不创建
# 2.遍历源文件夹中所有任务，并拷贝到目标文件夹
# 3.采用进程实现多任务，完成高并发拷贝

import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 1.拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 2.打开源文件和目标文件
    with open(source_path, "r") as source_file:
        with open(dest_path, "w") as dest_file:
            # 循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1.定义源文件夹和目标文件夹
    source_dir = "当前目录下的视频文件"       # 源文件夹
    dest_dir = "/home/python/桌面/test"    # 目标文件夹

    # 2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")

    # 3.读取源文件夹的文件列表
    file_list = os.listdir(source_dir)

    # 4.遍历文件列表实现拷贝
    for file_name in file_list:
        # 5.使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()
