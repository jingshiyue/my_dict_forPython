# -*- coding: UTF-8 -*-
#房贷计算器
import os


def calc_single_month(n):
    # 等额本息 计算单个月
    repayment1 = rate * (1 + rate) ** (n - 1)/((1 + rate) ** time - 1) * money
    repayment2 = repayment - repayment1
    print('第%d个月: 还款本金是：%0.2f，利息是：%0.2f' % (n, repayment1,repayment2))
    return repayment1,repayment2




# 等额本金-每月应还款额
def DEBJMonthlyPaymentCal(principal, yearRate, month):
    monthRate = yearRate
    MB = principal / month  # 每月本金
    # 初始化相关变量
    IR = [0] * month  # 每月利息
    YE = [0] * month  # 每月贷款余额
    MP = [0] * month  # 每月还款额
    YE[0] = principal
    for i in range(0, month):
        IR[i] = YE[i] * monthRate
        MP[i] = MB + IR[i]
        if i < month - 1:
            YE[i + 1] = YE[i] - MB
    return MP,IR,MP[0]-IR[0]





if __name__ == '__main__':
    while 1:
    
        while 1:
            try:
                money = int(input('请输入贷款总金额:(整数、单位万)'))
                print("-----------------------------")
                break
            except:
                print("贷款总金额输入错误 !")
                print("******************")

        while 1:
            try:
                time = int(input('请输入贷款年限:(整数)'))
                print("------------------------")
                break
            except:
                print("贷款年限输入错误 !")
                print("******************")

        while 1:
            try:
                rate = float(input('请输入贷款年利率:(4.9,表示4.9%)'))
                print("---------------------------")
                break
            except:
                print("贷款年利率输入错误 !")
                print("******************")

        while 1:
            try:
                _type = int(input('请输入方式 1: 等额本息 2: 等额本金: '))
                print("------------------------------")
                if _type == 1 or  _type == 2:
                    break
                else:
                    raise("贷款方式输入错误!")
            except:
                print("贷款方式输入错误 !")
                print("******************")


        # money = 100
        # time = 30
        # rate = 5.65

        # 将万转换为元
        money *= 10000
        # 月利率，将年利率4.9%转换为0.049，除以12转为月利率
        rate /= (12 * 100)
        # 年转换为月，总月数
        time *= 12

        if _type == 1:
            repayment = rate * (1 + rate) ** time / ((1 + rate) ** time - 1) * money
            print("="*50)
            print('每月还款金额是：%0.2f' % (repayment))
            total_interest = repayment * time - money
            print('利息总额：%.2f 万' % (total_interest/10000))
            print("="*50)
            while 1:
                try:
                    pay_sum = int(input("输入查看前N期累计还款: "))
                    print("---------------------------")
                    if pay_sum > time:
                        rasie("期数输入过大!")
                    break
                except:
                    print("ERROR: N 须为整数且不大于【贷款年限*12】 !")
                    print("*********************************")

            print("="*50)
            print("前%d期累计还款如下:" % pay_sum)

            month_sum = pay_sum
            benJin_sum = 0
            liXi_sum = 0
            for i in range(1,month_sum+1):
                benJin_per, liXi_per = calc_single_month(i)
                benJin_sum += benJin_per
                liXi_sum += liXi_per
            print("="*80)
            print('【等额本息】 前%d期累计还款: %0.2f，其中还本金: %0.2f，利息: %0.2f' %(pay_sum, benJin_sum+liXi_sum, benJin_sum, liXi_sum))
            print("="*80)
        elif _type == 2:
            MP,IR,huanBenJin = DEBJMonthlyPaymentCal(money,rate,time)
            liXi_sum = 0
            for liXi in IR:
                liXi_sum += liXi
            print('首月还款额: %.2f,利息总额：%.2f 万' % (MP[0],liXi_sum/10000))
            print("="*50)
            while 1:
                try:
                    pay_sum = int(input("输入查看前N期累计还款: "))
                    print("---------------------------")
                    if pay_sum > time:
                        rasie("期数输入过大!")
                    break
                except:
                    print("ERROR: N 须为整数且不大于【贷款年限*12】 !")
                    print("**********************************")

            print("前%d年累计还款如下:" % pay_sum)
            print("="*50)
            idx = pay_sum
            liXi_sum = 0
            month_counter = 1
            for liXi in IR[0:idx]:
                liXi_sum += liXi
                print("第%d个月: 还本金: %0.2f，还利息: %0.2f" %(month_counter,huanBenJin,liXi))
                month_counter += 1
            print("="*80)
            print('【等额本金】 前%d期累计还款: %0.2f，其中还本金: %0.2f，利息: %0.2f' %(pay_sum, huanBenJin*idx+liXi_sum, huanBenJin*idx, liXi_sum))
            print("="*80)



        ipt = input('【Q+回车】退出;输入其他键继续:')
        if ipt.lower() == "q":
            exit()
        else:
            continue
