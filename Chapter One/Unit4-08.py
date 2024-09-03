def check(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
result = check(16)
if not result:
    print("未成年")
# 在if判断中None等于False
# None函数返回值类型