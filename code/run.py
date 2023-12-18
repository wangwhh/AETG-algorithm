import argparse
import csv
from aetg import AETG
from data import jingdong
from data import xiecheng

parser = argparse.ArgumentParser()
parser.add_argument('-t', default=2, type=int, help='Covered Array 的强度 (T-wise converage)')
parser.add_argument('-w', '--website', choices=['jingdong', 'xiecheng'] ,default='jingdong', help='被测网站的名称，目前支持 jingdong 和 xiecheng')
parser.add_argument('--max', default=100, type=int, help='候选测试用例的最大数量')
parser.add_argument('--min', default=50, type=int, help='候选测试用例的最小数量')
parser.add_argument('-o', '--output', default='output.csv', help='测试用例的输出文件名，默认为 output.csv')

args = parser.parse_args()

if args.t:
    t_value = args.t
if args.website:
    website = args.website  
if args.max:
    m_max = args.max
if args.min:
    m_min = args.min
if args.output:
    output = args.output


if __name__ == '__main__':
    print('t_value: ', t_value)
    print('website: ', website)
    if website == 'jingdong':
        data = jingdong()
        
    elif website == 'xiecheng':
        data = xiecheng()
        
    file = open(output, 'w', encoding='utf-8-sig', newline='')
    writer = csv.writer(file)
    
    writer.writerow(data.options + ['覆盖对数'])
    test_case = AETG(data.parameters, t_value, m_max, m_min)
    for case in test_case:
        write_case = [data.data[i][case[0][i]] for i in range(len(case[0]))] + [case[1]]
        writer.writerow(write_case)
         
    file.close()
    print('测试用例已经输出到 ' + output)
    