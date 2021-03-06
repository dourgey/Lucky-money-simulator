from 中文编程 import *

def 随机分配(红包列表):
    for 索引, 当前红包金额 in 遍历索引和元素(红包列表):
        随机增减金额 = 小数(随机生成一个实数(0, 浮点数(当前红包金额 - 小数('0.01')))).量化(小数('.00'))
        当前红包金额 -= 随机增减金额
        红包列表[索引] = 当前红包金额  # 将结果写回去
        红包列表[整数(随机生成一个实数(0, 长度(红包列表)))] += 随机增减金额
    洗牌(红包列表)

总金额 = 小数(输入('请输入总金额：')).量化(小数('.00'))
红包个数 = 整数(输入('请输入红包数目：'))

# 平均分配后，较大的那批红包的个数
大红包数 = 整数(总金额 * 100) % 红包个数

较大的那批红包金额 = 小数(总金额 / 小数(红包个数)).量化(小数('.00'), 向上取整)
较小的那批红包金额 = 小数(总金额 / 小数(红包个数)).量化(小数('.00'), 向下取整)

# 生成初始红包状态
普通红包 = []
for 当前编号 in 范围(红包个数):
    if 当前编号 < 大红包数:
        普通红包.append(较大的那批红包金额)
    else:
        普通红包.append(较小的那批红包金额)

拼手气红包 = 普通红包[:]
随机分配(拼手气红包)

# 输出分配结果
for 索引, 当前红包 in 遍历索引和元素(拼手气红包):
    打印('第', 索引 + 1, '个红包：', 字符串(当前红包))

# 实现Decimal求和
打印('最终红包总金额：', 规约(lambda 甲, 乙 : 甲 + 乙, 拼手气红包))

# 暂停查看结果
暂停()
