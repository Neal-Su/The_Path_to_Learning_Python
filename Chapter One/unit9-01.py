# JSON数据格式的转换

# json数据格式可以实现跨编程语言的数据交互

# 导入json模块
import json

# 准备一个列表，列表内每一个元素都是字典，将其转换为json
data = [{"name": "张大山", "age": "11"}, {"name": "王大锤", "age": "13"}, {"name": "赵小虎", "age": "15"}]
json_str = json.dumps(data, ensure_ascii=False)
# ensure_ascii=False不写中文的话不用写这个参数，如果里面包含中文为了把内容正确展示出来
# 这个意思是表明，不使用ASC2来转换他，

print(type(json_str))  # json格式就是拥有特定格式的字符串
print(json_str)

# 准备字典，将字典转换为json
d = {"name": "周杰伦", "adds": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "张大山", "age": "11"}, {"name": "王大锤", "age": "13"}, {"name": "赵小虎", "age": "15"}]'
# 上面这个字符串一定要放在''单引号中，否则会报错
python_list = json.loads(s)
print(type(python_list))
print(python_list)

# 将json字符串转换为Python数据类型{k: v, k: v}
s = '{"name": "周杰伦", "adds": "台北"}'
# 上面这个字符串一定要放在''单引号中，否则会报错
python_dict = json.loads(s)
print(type(python_dict))
print(python_dict)