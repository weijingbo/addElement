import math
import datetime

import pandas as pd
def simpleCoe2Tle(startYear,startTime,six,ssc):
    tle = list()
    sBuffer0 = "1 "
    #行号 + 卫星编号
    sBuffer1 = "2 "
    sTemp = ssc #临时变量，存储six数组中转换后的String

    length = len(sTemp)# 临时变量，存储sTemp的长度
    if (length == 5):
        sBuffer0 += sTemp
        sBuffer1 += sTemp
    elif (length<5):
        for i in range(5-length):
            sBuffer0 += "0"
            sBuffer1 += "0"
        sBuffer0 += sTemp
        sBuffer1 += sTemp
    else:
        print("satellite ssc error")

    sBuffer0+="U          "+ str(startYear) + str(startTime)[:12] + "  .00000000  00000-0  00000-0 0 0000"
    sBuffer1+=" "
    #轨道的交角six[2]
    sTemp = str(six[2])
    length = len(sTemp)
    if (six[2] < 10):
        sBuffer1 += "00"
        if(length>=7):
            sBuffer1 += sTemp[:6]
        else:
            sBuffer1 += sTemp
            for i in range(6-length):
                sBuffer1 += "0"
    elif ((six[2]<100) and (six[2]>10)):
        sBuffer1 += "0"
        if (length >= 8):
            sBuffer1 += sTemp[:7]
        else:
            sBuffer1 += sTemp
            for i in range(7-length):
                sBuffer1 += "0"
    else:
        if (length >= 9):
            sBuffer1 += sTemp[:8]
        else:
            sBuffer1 += sTemp
            for  i in range(8-length):
                sBuffer1+="0"

    sBuffer1+=" "
    # 升交点赤经six[4]
    sTemp = str(six[4])
    length=len(sTemp)
    if (six[4] < 10):
        sBuffer1 += "00"
        if (length >= 7):
            sBuffer1 += sTemp[:6]
        else:
            sBuffer1 += sTemp
            for i in range(6-length):
                sBuffer1 += "0"
    elif ((six[4]<100) and (six[4]>10)):
        sBuffer1 += "0"
        if (length >= 8):
            sBuffer1 += sTemp[:7]
        else:
            sBuffer1 += sTemp
            for i in range(7-length):
                sBuffer1 += "0"
    else:
        if (length >= 9):
            sBuffer1 += sTemp[:8]
        else:
            sBuffer1 += sTemp
            for i in range(8-length):
                sBuffer1 += "0"
    sBuffer1 += " "
    #离心率six[1]
    sTemp = str(six[1])
    sTemp = sTemp[2:]
    length = len(sTemp)
    if (length >= 9):
        sBuffer1 += sTemp[0:7]
    else:
        sBuffer1 += sTemp
        for i in range(7-length):
            sBuffer1 += "0"
    sBuffer1 += " "
    #近地点角矩 six[3]
    sTemp=str(six[3])
    length = len(sTemp)

    if (six[3] < 10):
        sBuffer1 += "00"
        if (length >= 7):
            sBuffer1 += sTemp[:6]
        else:
            sBuffer1 += sTemp
            for i in range(6-length):
                sBuffer1 += "0"
    elif ((six[3]<100) and (six[3]>10)):
        sBuffer1 += "0"
        if (length >= 8):
            sBuffer1 += sTemp[:7]
        else:
            sBuffer1 += sTemp
            for i in range(7-length):
                sBuffer1 +="0"
    else:
        if (length >= 9):
            sBuffer1 += sTemp[:8]
        else:
            sBuffer1 += sTemp
            for i in range(8-length):
                sBuffer1 +="0"

    sBuffer1 +=" "
    # 在轨圈数 six[5]
    sTemp = str(six[5])
    length = len(sTemp)
    if (six[5] < 10):
        sBuffer1 += "00"
        if (length >= 7):
            sBuffer1 += sTemp[:6]
        else:
            sBuffer1 += sTemp
            for i in range(6-length):
                sBuffer1 +="0"
    elif ((six[5]<100) and (six[5]>10)):
        sBuffer1 +="0"
        if (length >= 8):
            sBuffer1 += sTemp[:7]
        else:
            sBuffer1 += sTemp
            for i in range(7-length):
                sBuffer1 += "0"
    else:
        if (length >= 9):
            sBuffer1 += sTemp[:8]
        else:
            sBuffer1 += sTemp
            for i in range(8-length):
                sBuffer1 +="0"

    sBuffer1 += " "

    # 平均运动（每日绕行圈数）six[0]
    sTemp = str(six[0])
    length = len(sTemp)
    if (six[0] < 10):
        sBuffer1 += "0"
        if (length >= 16):
            sBuffer1 += sTemp[:15]
        else:
            sBuffer1 += sTemp
            for i in range(15-length):
                sBuffer1 +="0"
    else:
        if (length >= 17):
            sBuffer1 += sTemp[:16]
        else:
            sBuffer1 += sTemp
            for i in range(16-length):
                sBuffer1 += "0"

    tle.append(sBuffer0)
    tle.append(sBuffer1)

    # 第一行校验
    sum = 0
    for i in range(len(tle[0])):
        subTLE = tle[0][i:i+1]
        if ((subTLE in ["U"," ",".","+"])):
            sum += 0
        elif ((subTLE == "-")):
            sum += 1
        else:
            sum=sum+int(subTLE)
    tle[0] = tle[0] + str(sum % 10)
    # 第二行校验
    sum = 0
    for i in range(len(tle[1])):
        subTLE = tle[1][i:i+1]
        if ((subTLE in ["U"," ",".","+"])):
            sum += 0
        elif ((subTLE == "-")):
            sum += 1
        else:
            sum=sum+int(subTLE)
    tle[1] = tle[1] + str(sum % 10)

    return tle


#真近点角转平近点角,传入单位为度,返回值单位为度.
def true2mean(true_anomaly_degree,e):
    true_anomaly_rad = math.radians(true_anomaly_degree)
    pian_rad = 2*math.atan(math.sqrt((1-e)/(1+e))*math.tan(true_anomaly_rad/2))

    mean_anomaly_rad = pian_rad-e*math.sin(pian_rad)
    mean_anomaly_degree = math.degrees(mean_anomaly_rad)%360

    return mean_anomaly_degree

#半长袖转运行圈次 sema单位km
def sema2numOfrotate(sema):
    GM = 398.60047e12  # 米3/秒2
    # 公式算出来的是米，所以，这里手动给sema(km)乘1000
    Period = math.sqrt((4 * (3.1415926 ** 2) * ((sema * 1000) ** 3)) / GM)
    Num_of_rotate = 86400 / Period  # 14.917565371231026
    return Num_of_rotate


#这种格式的时间字符串"2022-11-5 04:00:00",计算是一年的第几天(用十进制小数表示一年中的第几日和日中的小数部分)
def timestr2yday(timestr):
    t_str_datetime = datetime.datetime.strptime(timestr,"%Y-%m-%d %H:%M:%S")
    day = t_str_datetime.timetuple().tm_yday
    h = t_str_datetime.hour
    m = t_str_datetime.minute
    s = t_str_datetime.second
    fr = (h*3600+m*60+s)/86400
    return day+fr


#根据传入的所有卫星轨道六元素数据文件(file_location),在运行目录下生成对应tle文件(raw_tle.txt)
def generate_tle_from_coe6(file_location,ssc,name):

    coe6_data_df = pd.read_csv(file_location)

    each_sat_time_str_list = coe6_data_df["time"].to_list()
    each_sat_sema_list = coe6_data_df["sema"].to_list()
    each_sat_e_list = coe6_data_df["e"].to_list()
    each_sat_i_list = coe6_data_df["inclination"].to_list()
    each_sat_rann_list = coe6_data_df["RAAN"].to_list()
    each_sat_arg_of_perigee_list = coe6_data_df["Arg of Perigee"].to_list()
    each_sat_true_anomaly_list = coe6_data_df["True Anomaly"].to_list()


    index = 0
    with open("raw_tle.txt",mode="w") as f:
        for t_str,sema,e,i,rann,arg_of_perigee,true_anomaly in zip(each_sat_time_str_list,
                                                                   each_sat_sema_list,
                                                                   each_sat_e_list,
                                                                   each_sat_i_list,
                                                                   each_sat_rann_list,
                                                                   each_sat_arg_of_perigee_list,
                                                                   each_sat_true_anomaly_list):

            startYear = int(t_str[2:4]) #17
            startTime = float(str(timestr2yday(t_str))[:12])         #123.16666667  # 长度固定 长度为12
            numOfrotate = sema2numOfrotate(sema)
            mean_anomaly = true2mean(true_anomaly,e)
            six = []
            six.append(numOfrotate)  # 一天的圈数 对应半长轴
            six.append(e)  # 偏心率
            six.append(i)  # 轨道倾角
            six.append(arg_of_perigee)  # 近地点角 Argument of perigee
            six.append(rann)  # 升交点赤经 RANN
            six.append(mean_anomaly)  # 平近点角

            sat_name = "{}_{}".format(name,index)
            tle = simpleCoe2Tle(startYear, startTime, six, ssc)
            print(sat_name)
            print(tle[0])
            print(tle[1])
            f.write(sat_name+"\n")
            f.write(tle[0]+"\n")
            f.write(tle[1]+"\n")
            index+=1
            ssc_int =int(ssc)+1
            ssc = str(ssc_int)



if __name__ == '__main__':
    '''
    true_anomaly_degree,mean_anomaly_degree 
    246.57173714055182,246.61511610464922
    '''

    sema = 7161.962220298484
    e = 0.0004125145949619736
    inclination = 86.40324903837323
    rann = 0.004099708357840124
    true_anomaly_degree = 246.57173714055182
    print('true_anomaly_degree', true_anomaly_degree)
    mean_anomaly_degree = true2mean(true_anomaly_degree, e)
    print('mean_anomaly_degree', mean_anomaly_degree)

    Num_of_rotate = sema2numOfrotate(sema)

    print('Num_of_rotate', Num_of_rotate)

    startYear = 17
    startTime =123.16666667 #长度固定 长度为12

    six = []
    six.append(3) #一天的圈数 对应半长轴
    six.append(0.001) #偏心率
    six.append(28.5) #轨道倾角
    six.append(222) #近地点角 Argument of perigee
    six.append(111) #升交点赤经 RANN
    six.append(123) #平近点角
    # six[0] = 3 # 必须小于100
    # six[1] = 0.001 # 小于1
    # six[2] = 28.5 # 不能是负数
    # six[3] = 222 # 不超过360
    # six[4] = 111 # 不超过360
    # six[5] = 123 # 不超过360

    ssc = "10000" # 最多五位数

    tle_list = simpleCoe2Tle(startYear, startTime, six, ssc)
    print(tle_list[0])
    print(tle_list[1])






















