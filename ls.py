import sys
 
import os
 
 
def ls(*args):
    # 如果有传路径参数，则取路径参数，没传则取当前目录（"." 表示当前目录）
    path = args[1] if args.__len__() > 1 else "."
    # 文件不存在，直接退出
    if not os.path.exists(path):
        return
    # 文件不是一个目录，直接退出
    if not os.path.isdir(path):
        return
 
    files = os.listdir(path)
    # 对文件名进行排序，方便阅读一些
    files.sort()
    print("  ".join(files))
 
 
if __name__ == "__main__":
    ls(*sys.argv)
