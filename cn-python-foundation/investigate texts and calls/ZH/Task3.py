"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
#1. Take out all the phone numbers called by Bangalore's phone numbers.
def Bangalore_call(calls):
	Bangalore_call_list = []
	
	for element in calls:
		if element[0][:5] == '(080)':
			Bangalore_call_list.append(element[1])
			
	return Bangalore_call_list
#2. define functions to give different kinds of codes.

#define a function to return mobile phone number's code.	
def mobile_codes(mobile_string):
	
	return mobile_string[:4] 

#define a function to return fixed-line number's code.	
def area_codes(fixed_line_string):
	n = 0
	while fixed_line_string[n] != ")":
		n += 1
	return fixed_line_string[0:n+1]

#define a function to return sale man's number's code.	
def sale_codes(sale_string):
	
	return sale_string[:3]

#3. define a function to judge the type of phone numbers, and call the upper functions to return codes into a list.
def call_codes(call_list):
	code_list = []
#Take all the code from the called list.	
	for element in call_list:
		if element[0] == "(":
			code_list.append(area_codes(element))
		elif element[0] == "7" or element[0] == "8" or element[0] == "9":
			code_list.append(mobile_codes(element))
		elif element[:3] == "140":
			code_list.append(sale_codes(element))
		else:
			continue
	return code_list
	
#4. Remove all the same codes in the list
def remove_same_codes(code_list):
	target_code_list = []
	
	for element in code_list:
		if element not in target_code_list:
			target_code_list.append(element)
		else:
			continue
	return target_code_list
	
#PART 1	

	Bangalore_call_list = Bangalore_call(calls)
	code_list = call_codes(Bangalore_call_list)
	target_code_list = remove_same_code(code_list)
	print("The numbers called by people in Bangalore have codes:")
	print(target_code_list.join("\n")

	

#get the counts of Bangalore called  Bangalore.
def B2B_call_count(code_list):
	n = 0
	for element in input_list:
		if element == "(080)":
			n += 1
		else:
			continue
	return n
	
#PART 2
	Bangalore_call_list = Bangalore_call(calls)#get all Bangalore called phone numbers.
	code_list = call_codes(Bangalore_call_list)#get the number codes
	B2B_call_counts = B2B_call_count(code_list)
	call_rate = B2B_call_counts / len(code_list)
	print("{.2f} percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore.".format(call_rate))
