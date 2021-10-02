print("********班级期末成绩管理系统********")

students = []  # 创建students列表，用来储存所有学生
stu = []  # 创建stu列表，用来临时存储单个学生信息
filename = 'output.txt'  # 初始化输出文件
with open(filename, 'a') as f:
    f.write("学号\t" + "姓名\t" + "成绩\n")


def get_max(*students):  # 定义函数，求最高分
    maxs = 0
    for arr in students:
        for stu in arr:
            maxs = (maxs if maxs > float(stu[2]) else float(stu[2]))
    return maxs


def get_min(*students):  # 定义函数，求最低分
    mins = 10000
    for arr in students:
        for stu in arr:
            mins = (mins if mins < float(stu[2]) else float(stu[2]))
    return mins


def get_avg(*students):  # 定义函数，求平均分
    sums = 0
    cnt = 0
    for arr in students:
        for stu in arr:
            sums += float(stu[2])
            cnt += 1
    return sums / cnt


def search(n, *students):  # 定义函数，查找对应学号的学生信息
    for arr in students:
        for stu in arr:
            if n == stu[0]:
                s = "学号为" + n +"的学生姓名为 " + stu[1] + ",成绩为 " + stu[2]
                print(s)
                with open(filename, 'a') as f:  # 将当前信息写入文件
                    f.write(s)


while True:
    op = int(input("请输入数字选择功能(1-输入 2-统计 3-查询 0-退出)："))

    if op == 1:
        sn, name, score = input("请分别输入学生的学号，姓名与成绩（用空格隔开）\n").split()  # 用户输入学生数据
        stu.clear()         # 清空临时数据
        stu.append(sn)      # 添加学号
        stu.append(name)    # 添加姓名
        stu.append(score)   # 添加成绩
        students.append(stu[:])  # 将当前学生信息添加到students列表中
        s = sn + "\t" + name + "\t" + score + "\n"  # 格式化当前信息
        print(s)            # 将当前信息显示到控制台
        with open(filename, 'a') as f:  # 将当前信息写入文件
            f.write(s)
    elif op == 2:
        s1 = "最高分为：" + str(get_max(students)) + "\n"  # 求最高分
        s2 = "最低分为：" + str(get_min(students)) + "\n"  # 求最低分
        s3 = "平均分为：" + str(get_avg(students)) + "\n"  # 求平均分
        s = s1 + s2 + s3    # 格式化当前信息
        print(s)            # 将当前信息显示到控制台
        with open(filename, 'a') as f:  # 将当前信息写入文件
            f.write(s)
    elif op == 3:
        n = input("请输入要查找的学生学号:")
        search(n, students)
    elif op == 0:
        print("程序退出，感谢使用。")
        break
    else:
        print("输入数字不合法，请重新输入")
        continue
