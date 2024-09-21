# 文件的读取操作

# 打开文件函数：open(name, mode, encoding)
# name:是要打开的文件的路径
# mode：设置打开文件的模式：只读、写入、追加等，
#      r:以只读方式打开文件，文件的指针会放在文件的开头。这是默认模式
#      w:打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，原有内容会被删除。
#        如果该文件不存在，创建新文件。
#      a:打开一个文件用于追加。如果该文件已存在，新的内容会被写入到已有内容之后。如果该文件不存在，
#        创建新文件进行写入
# encoding：编码格式，推荐使用UTF-8

# 打开文件
f = open("E:/test.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件方法  文件对象.read(num)
# num表示要从文件中读取的数据的长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有数据
print(f"读取10个字节的结果是：{f.read(10)}")
print(f"read方法读取全部内容的结果是：{f.read()}")
print(f"------------------------------")

# 读取文件方法  文件对象.readlines()
# readlines可以按照行的方式把整个文件的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
f = open("E:/test.txt", "r", encoding="UTF-8")
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容是：{lines}")

# 读取文件方法  文件对象.readline()  一次读取一行内容
f = open("E:/test.txt", "r", encoding="UTF-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

print(f"line1对象的类型：{type(line1)}")

print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件行
f = open("E:/test.txt", "r", encoding="UTF-8")
for line in f:
    print(f"每一行数据是：{line}")

# 文件的关闭，如果文件不关闭，那个文件将一直被python程序所占用
f.close()
print(f"------------------------------")

# with open 方法 打开文件后，自动关闭
with open("E:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"line对象的类型：{type(line)}")
        print(f"再次打开后每一行数据是：{line}")

# 大连海事大学（原大连海运学院）
# （Dalian Maritime University）
# 简称海大、大连海大，位于辽宁省大连市
# 是交通运输部直属的全国重点大学，是交通运输部、教育部、辽宁省人民政府、大连市人民政府共建的全日制公办本科高校
# 是国家“211工程”、“双一流”建设高校。