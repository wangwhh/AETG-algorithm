# README
## 简介
该项目是浙江大学软件质量保证与测试课程作业，实现了AETG算法，基于京东和携程的网站建模信息，生成T-wise的组合测试用例。
## 查看帮助信息
```
python code/run.py -h
```

```
usage: run.py [-h] [-t T] [-w {jingdong,xiecheng}] [--max MAX] [--min MIN] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -t T                  Covered Array 的强度 (T-wise converage)
  -w {jingdong,xiecheng}, --website {jingdong,xiecheng}
                        被测网站的名称，目前支持 jingdong 和 xiecheng
  --max MAX             候选测试用例的最大数量
  --min MIN             候选测试用例的最小数量
  -o OUTPUT, --output OUTPUT
                        测试用例的输出文件名，默认为 output.csv
```

## 运行程序
```
python code/run.py # 添加你需要的参数
```



#### 后记

感觉这是软测课上为数不多的有点学到的东西（这是可以说的吗

其实感觉没有完全按照 AETG 的算法来实现，在生成候选集的时候应该排除已经使用过的值，但是懒得搞了（

第一次用 typst 写报告，感觉很爽！！好用！（虽然是用了 PeiPei 的模板 [PeiPei233/typst-template](https://github.com/PeiPei233/typst-template)）

