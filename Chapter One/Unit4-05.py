def hesuan(tem):
    if tem <= 37.5:
        print(f"请出示您的健康码以及72小时核酸证明，并配合测量体温\n体温测量中，您的体温是：{tem}度，体温正常请进")
    else:
        print(f"请出示您的健康码以及72小时核酸证明，并配合测量体温\n体温测量中，您的体温是：{tem}度，需要隔离")
hesuan(36.5)
# 函数传入参数