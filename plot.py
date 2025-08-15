import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re
# 设置中文字体
plt.rcParams["font.family"] = ["SimHei","WenQuanYi Micro Hei","Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

#功能描述：用户输入某天某变量，返回该变量的可视化图像
#先不考虑防御性或者鲁棒性，先完成主要功能
def get_date(input_date:str):
    # pattern = r'^25|2025.?(\d{1,2}).?(\d{1,2})$'
    pattern = r'^25|2025.?(0?\d|1[1-2]).?(0?\d|[1-3]\d)$'
    match_result = re.match(pattern,input_date)
    return match_result

def process_time(time:str):
    if '0' == time[0]:
        return time.replace("0","")
    else:
        return time

def path_gen(base_path,date):
    #check，转换成”统一格式“
    
    for item in os.listdir():
        if date in item:
            return  os.path.abspath(item)

def get_excel_data(data_path):
    #该函数用于读取文件数据，返回一个df
    df = pd.read_excel(data_path)
    return df


def line_plot(DataFrame,y):
    df['时间'] = pd.to_datetime(df['时间'],errors="coerce")
    df["小时分钟"] = df["时间"].dt.strftime("%H:%M")
    plt.plot(df["小时分钟"],df[y])
    plt.show()

def test():
    print(os.getcwd())
    data_path = "离线测试\\旋流器数据\\2025-6-25.xlsx"
    df = pd.read_excel(data_path)
    print(df.columns)
    # print(df['时间'].dtype)
    #转换时间类型
    df['时间'] = pd.to_datetime(df['时间'],errors="coerce")
    # print(df["时间"].dtype)
    #提取时间信息
    df["小时分钟"] = df["时间"].dt.strftime("%H:%M")
    

    #准备数据
    #因变量：泵池液位检测值
    plt.plot(df["小时分钟"],df["泵池液位检测值"],linestyle='-')
    plt.plot(df["小时分钟"],df["泵池补加水检测值"],marker="*",color='green')
    plt.xlabel("时间/t",size=15)
    plt.ylabel("泵池液位，补加水量",size=15,rotation=90,)
    plt.show()

if __name__ == "__main__":
    base_path = ".\\离线测试\\旋流器数据"
    os.chdir(base_path)
    test_user_input = "25/6/25","溢流200目粒度"
    user_input = "2025-6-30","溢流200目粒度"
    date_input ,y = test_user_input #收集用户输入
    m = get_date(date_input)
    month , day = m.groups()
    year = "2025"
    month = process_time(month)
    day = process_time(day)
    date = year+'-'+month+'-'+day
    data_path = path_gen(base_path,date)
    df = get_excel_data(data_path)
    line_plot(df,y)

    