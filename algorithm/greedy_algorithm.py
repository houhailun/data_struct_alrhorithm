#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/19 18:17
# Author: Hou hailun

from copy import deepcopy

# 贪心算法
# 贪心算法解决问题的步骤：
# 1、针对一组数据，定义了限制值和期望值，希望从中选出几个数据，在满足限制值的情况下，期望值最大
# 2、尝试用贪心算法解决：每次选择当前情况下，在对限制值同等贡献量的情况下，对期望值贡献最大的数据
# 贪心算法可能不是全局最优解


# 贪心算法Demo
# Demo1: 0/1背包
# 问题描述：有 N 件物品和一个承重为 W 的背包（也可定义为体积），每件物品的重量是 wi，价值是 pi，
#       求解将哪几件物品装入背包可使这些物品在重量总和不超过 W 的情况下价值总和最大。
#       这个问题隐含了一个条件，每个物品只有一件，也就是限定每件物品只能选择 0 个或 1 个，因此又被称为 0-1 背包问题
# 具体实例：一个背包，最多能承载重量为 W=150 的物品，现在有 7 个物品（物品不能分割成任意大小），编号为 1~7，
#       重量分别是 wi=[35、30、60、50、40、10、25]，价值分别是 pi=[10、40、30、50、35、40、30]，
#       现在从这 7 个物品中选择一个或多个装入背包，要求在物品总重量不超过 W 的前提下，所装入的物品总价值最高。
# 问题分析：
#    1、目标函数: sum(Pi)最大，使得装入背包中的所有物品Pi的价值加起来最大
#    2、约束条件：装入背包的物品总重量不能超过背包容量 Sum(Wi)<=M(M=150)
#    3、贪心策略：
#       3.1 选择价值最大的物品
#       3.2 选择重量最小的物品
#       3.3 选择单位重量价值最大的物品
class Good:
    def __init__(self, weight, value, status):
        self.weight = weight  # 物品重量
        self.value = value    # 物品价值
        self.status = status  # 是否放入背包标记


class Greedy:
    def greedy(self, goods, W, strategory='strategy_max_unit_value'):  # goods是物品的集合，W是背包的空闲重量
        result = []
        sum_weight = sum_value = 0
        goodsMat = deepcopy(goods)
        while True:
            if strategory == 'strategy_min_weight':
                s = self.strategy_min_weight(goodsMat, W)
            elif strategory == 'strategy_max_value':
                s = self.strategy_max_value(goodsMat, W)
            else:
                s = self.strategy_max_unit_value(goodsMat, W)
            if -1 == s:
                break
            sum_weight += goodsMat[s].weight
            sum_value += goodsMat[s].value
            result.append(goodsMat[s].weight)
            W = W - goodsMat[s].weight
            goodsMat[s].status = 1
            goodsMat.pop(s)
        return result, sum_weight, sum_value

    def strategy_min_weight(self, goods, W):
        # 按最小重量贪心策略
        index = -1
        minWeight = goods[0].weight
        for i in range(0, len(goods)):
            currGood = goods[i]
            # 选择当前未选择的物品 && 物品的重量小于当前背包剩余重要 && 当前物品的重量小于最小重量的物品重量
            if currGood.status == 0 and currGood.weight <= W and currGood.weight <= minWeight:
                index = i
                minWeight = goods[index].weight
        return index

    def strategy_max_value(self, goods, W):
        # 按最大价值贪心策略
        index = -1
        max_value = goods[0].value
        for i in range(0, len(goods)):
            currGood = goods[i]
            if currGood.status == 0 and currGood.weight <= W and currGood.value > max_value:
                index = i
                max_value = goods[index].value
        return index

    def strategy_max_unit_value(self, goods, W):
        # 按最大单位重要的价值贪心策略
        index = -1
        max_unit_value = goods[0].value / goods[0].weight
        for i in range(0, len(goods)):
            currGood = goods[i]
            curr_unit_value = currGood.value / currGood.weight
            if currGood.status == 0 and currGood.weight <= W and curr_unit_value >= max_unit_value:
                index = i
                max_unit_value = currGood.value / currGood.weight
        return index


# Demo2: 最优装载问题
# 问题描述：有一天海盗们截获了一艘装满各种各样古董的货船，每一件都价值连城，一旦打碎就是去了价值，海盗船载重量为C，每件固定的重量为wi，海盗们该如何尽可能装载最多数量的古董呢？
# 问题分析：
#   1、目标函数：装载的古董数最多
#   2、约束条件：装载股东的总重量不能超过船的承载重量C
#   3、贪心策略：选择重量最小的物品
def max_ans():
    # 船载重量固定为C，只要每次选择重量最小的古董，直到不能再装为止，这样装载的古董数量最大，
    # 把古董按重量从小到大排序，根据策略选出尽可能多的古董。
    antique = [4, 10, 7, 11, 3, 5, 14, 2]  # 古董重量
    ship_antique = 30  # 船承载的重量

    antique.sort()
    ans, tmp = 0, 0
    ship = []
    for a in antique:
        tmp += a
        if tmp <= ship_antique:
            ans += 1
            ship.append(a)
    print('装载古董的数量:', ans)
    print('装载的古董:', ship)


# Demo3: 分糖果问题
# 问题描述：已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，当某个糖果的大小s>=某个孩子的需求因子g时，代表该糖果可以满足该孩子，求使用这些糖果，最多能满足多少孩子（注意，某个孩子最多只能用1个糖果满足）
# 问题分析：
#   1、目标函数：分到糖果的孩子最多
#   2、约束条件：当某个糖果的大小s>=某个孩子的需求因子g时，代表该糖果可以满足该孩子
#   3、贪心策略：
#       优先选择需求因子g最小的孩子,当某个孩子有多个糖果满足时，优先用最小的糖果
# 算法设计：
#   1、对需求因子数组g和糖果大小数组s进行排序，从小到大
#   2、按照从小到大的顺序使用各糖果尝试是否可满足某个孩子，每个糖果只尝试1次，只有尝试成功时，换下一个孩子尝试，直到发现没更多的孩子或者没有更多的糖果，循环结束
def findContentChild(g, s):
    if not g or not s:
        return 0

    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:  # 只有孩子的需求g小于糖果大小s才分给该孩子
            child += 1  # 已经有一个孩子分配到糖果
        cookie += 1     # 上一个糖果已经分配或者不能分配，用下一个糖果检查能否分配
    return child


# Demo4: 移除K个数字
# 问题描述：已知一个使用字符串表示非负整数num，将num中的k个数字移除，求移除k个数字后，可以获得的最小的可能的新数字(num不会以0开头，num长度小于10002)
# 具体实例：输入：num = “1432219”,k=3；在去掉3个数字后得到的很多可能里，如1432，4322，2219，1219。。。。；去掉数字4、3、2、得到的1219最小
# 问题分析：
#   1、目标函数：去掉k个数字后新的到的数字最小
#   2、约束条件：k 小于num的位数
#   3、贪心策略：
#       若去掉某一位数字，为了使得到的新数字最小，需要尽可能让得到的新数字优先最高位最小，其次次位最小，再其次第三位最小；
#       从高位向地位遍历，如果对应的数字大于下一位数字，则把该位数字去掉，得到的数字最小
# 算法设计：
#   使用栈存储最终结果或删除工作，从高位向低位遍历num，如果遍历的数字大于栈顶元素，则将该数字push入栈，如果小于栈顶元素则进行pop弹栈，直到栈为空或不能再删除数字(k==0)或栈顶小于当前元素为止。最终栈中从栈底到栈顶存储的数字，即为结果
def removeknums(nums, k):
    n = len(nums)
    if n < k:  # nums位数必须大于k
        return None
    stack = []
    for number in nums:
        if not stack:  # 空栈，则直接入栈
            stack.append(number)
            continue
        if k > 0:  # k 大于0
            while k > 0 and stack:
                if stack[-1] > number:  # 栈顶元素大于下一个数字, 栈顶元素出战
                    stack.pop()
                    k -= 1
                else:
                    break
        stack.append(number)
    if k != 0:  # 扫描完后k不为0，则只取0:k的数据
        return ''.join(stack[:-k])
    return ''.join(stack)


if __name__ == "__main__":

    # 0/1背包
    goods = [Good(35, 10, 0), Good(30, 40, 0), Good(60, 30, 0), Good(50, 50, 0),
             Good(40, 35, 0), Good(10, 40, 0), Good(25, 30, 0)]
    g = Greedy()
    result, sum_weight, sum_value = g.greedy(goods, 150, 'strategy_min_weight')
    print("--------------按照取最小重量的贪心策略--------------")
    print("最终总重量为：" + str(sum_weight))
    print("最终总价值为：" + str(sum_value))
    print("重量选取依次为：", end='')
    print(result)

    print("--------------按照取最大价值贪心策略--------------")
    result, sum_weight, sum_value = g.greedy(goods, 150, 'strategy_max_value')
    print("最终总重量为：" + str(sum_weight))
    print("最终总价值为：" + str(sum_value))
    print("重量选取依次为：", end='')
    print(result)

    print("--------------按照取单位重量的最大价值贪心策略--------------")
    result, sum_weight, sum_value = g.greedy(goods, 150)
    print("最终总重量为：" + str(sum_weight))
    print("最终总价值为：" + str(sum_value))
    print("重量选取依次为：", end='')
    print(result)

    # 最优装载问题
    print(' 最优装载问题 '.center(40, '-'))
    max_ans()

    # 分糖果问题
    print(' 分糖果问题 '.center(40, '-'))
    g = [5, 10, 2, 9, 15, 9]
    s = [6, 1, 20, 3, 8]
    print(findContentChild(g, s))

    print(' 移除数字 '.center(40, '-'))
    print(removeknums('1221312', 3))