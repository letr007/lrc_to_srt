import os
import re

print("本程序用于将.lrc格式转.srt格式")
print("Coryright ©letr")

l_list = os.listdir(os.getcwd())
lrc_file_list = []
for i in l_list:
	j = i.split(".")
	if j[-1] == "lrc":
		lrc_file_list.append(i)
print("-" * 30)
print("找到文件(.lrc)")
print("-" * 30)
n = 1
for k in lrc_file_list:
	print("%s)" % str(n),k)
	n+=1
print("-" * 30)
index = int(input("请选择要转换的文件序号:"))
print("-" * 30)
lrc_f = open("./%s" % lrc_file_list[index - 1], "r")
lrc_file = lrc_f.readlines()
lrc_f.close()
srt_file = lrc_file_list[index - 1].split(".")[0]
srt_f = open("./%s.srt" % srt_file, "w")

for i in range(len(lrc_file)):
	# 提取信息
	info_1 = lrc_file[i]
	if i == len(lrc_file) - 1:
		break
	info_2 = lrc_file[i + 1]
	# 分离出时间进行处理
	tmp_1_0 = info_1.split("]")
	tmp_2_0 = info_2.split("]")
	# 切片字符串，除去多余内容
	time_1 = tmp_1_0[0][1:]
	time_2 = tmp_2_0[0][1:]
	# 将毫秒时间分离
	tmp_1_1 = time_1.split(".")
	tmp_1_2 = tmp_1_1[1]
	tmp_2_1 = time_2.split(".")
	tmp_2_2 = tmp_2_1[0].split(":")
	tmp_2_3 = tmp_2_2[1]
	# 将毫秒留出时间间隔
	if int(tmp_2_1[1]) < 50:
		if int(tmp_2_3) > 0:
			tmp_2_3 = str(int(tmp_2_3) - 1)
			tmp_2_4 = int(tmp_2_1[1]) - 50
			tmp_2_4 = str(1000 + tmp_2_4)
		else:
			tmp_2_4 = tmp_2_1[1]
	else:
		tmp_2_4 = str(int(tmp_2_1[1]) - 50)
	# 格式化毫秒为字幕要求格式
	if len(tmp_2_4) == 2:
		tmp_2_4 = tmp_2_4 + "0"
	if len(tmp_2_4) == 1:
		tmp_2_4 = tmp_2_4 + "00"
	if len(tmp_1_2) == 2:
		tmp_1_2 = tmp_1_2 + "0"
	if len(tmp_1_2) == 1:
		tmp_1_2 = tmp_1_2 + "00"
	if len(tmp_2_3) == 1:
		tmp_2_3 = "0" + tmp_2_3
	# 拼接时间
	time_1 = tmp_1_1[0] + "," + tmp_1_2
	time_2 = tmp_2_2[0] + ":" + tmp_2_3 + "," + tmp_2_4
	# 重整为字幕时间格式
	time_srt = "00:" + time_1 + " --> " + "00:" + time_2
	# 构建字幕格式
	data_l1 = "%s\n" % str(i + 1)
	data_l2 = "%s\n" % time_srt
	data_l3 = "%s\n" % tmp_1_0[1]
	srt_data = data_l1 + data_l2 + data_l3 
	# 写入文件
	srt_f.write(srt_data)
print("转换完成")
print("-" * 30)
srt_f.close()

