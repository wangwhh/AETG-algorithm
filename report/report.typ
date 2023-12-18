#import "assets/report-template.typ": *

#show: project.with(
  title: "AETG算法实现",
  course: "软件质量保证与测试",
  author: "王俊怡",
  id: "3210106016",
  advisor: "赵晓琼",
  college: "计算机科学与技术学院",
  major: "软件工程",
  year: 2023,
  month: 12,
  day: 17,
)

#align(center, text(size: 17pt)[
    *AETG Algorithm Implementation Experiment Report*
])

= Introduction
== Combinational Testing
Combinatorial testing, is a software testing technique used to systematically test different combinations of input parameters or configuration settings in order to identify defects or vulnerabilities in a software system.

In software development, there are often many possible combinations of input values or configuration settings that can affect the behavior of a system. Testing all possible combinations individually can be time-consuming and impractical, especially for complex software with numerous parameters. Combinational testing offers a more efficient way to cover a wide range of scenarios instead of testing each one separately.

== AETG
The AETG (Automated Efficient Test Generation) algorithm is a method to generate test cases in combination testing that cover all possible combinations of input parameters. This algorithm is a form of combinatorial testing designed to efficiently test complex systems with many interacting components or settings.

The AETG algorithm reduces the number of test cases needed to achieve significant coverage, thereby saving time and resources in the testing process.
@605761

= Algorithm Description
Assume that we have a system with $k$ test parameters and that the $i$ th parameter has $l_i$ different values.  We select each test case by first generating M different candidate test cases and then choosing one that covers the most new pairs. Each candidate test case is selected by the following greedy algorithm:

+ Choose the first parameter $f$ and a value $l$ for $f$ such that it appears in the greatest number of uncovered pairs.

+ Let $f_1 = f$. Then randomly generate a order for the remaining parameters. Then, we have an order for all k parameters $f_1, ..., f_k$ .

+ For each parameter $f_i$ in the order, choose a value $l_i$ for $f_i$. The value $l_i$ is chosen by the following method.
    - Assume that we have already selected $i-1$ values for parameters $f_1, ..., f_(i-1)$ and we will now select the value for $f_i$.
    - if $i<=t$, for each value of $f_i$, we combine it with the $l_1, ..., l_(i-1)$. Now we have $l_1, ..., l_i$. Then calculate the number of new pairs that will be covered by the new case. Then we choose the value that covers the most new pairs.
    - if $i>t$, for each value of $f_i$, we select $t-1$ parameters from $f_1, ..., f_(i-1)$ and traverse all possible combinations. Then we will follow the same steps as before, choose the value that covers the most new pairs.

+ After we have selected all $k$ values, we have a candidate test case. Then we choose the candidate test case that covers the most new pairs.

+ Repeat step 1-4 until the uncovered-pairs-set is empty.

= Algorithm Implementation

== Data Structure 

=== Class `Data`
Class Data has 4 variables: `name, options, parameters, data`. `name` is the name of the data. `options` is the title of each parameters. `parameters` is an array stores the number of the values of each parameters, which will be used in AETG algorithm. `data` is a 2D array that stores the data. 

For example, if we have parameters like this: `[5, 7, 2, 3, 6]`, it represents that we have 5 parameters and the first parameter has 5 values, the second parameter has 7 values, and so on. Then we can use this array in AETG to generate the test case.

=== Test Case
The test case in AETG algorithm is an array. For example, if the test case is `[-1, 0, 2, -1, 1]`, it means that the first parameter is not selected, the second parameter is the first value, the third parameter is the third value, and so on.


=== Uncoveres Pairs
At the beginning of the algorithm, all uncovered pairs (ucps) will be generated. 
The uncovered pairs is an array that stores the pairs that are not covered. For each ucp, we find all combinations of *t* parameters and all combinations of the values for each parameters. We represent it as `[[0, 0, -1, -1, -1], [0, 1, 1, -1, -1], ...]` where t=2.

== Algorithm Implementation
=== Pseudo Code
#code( 
    stepnumber:1,
    numbers: true,
)[```python
uncovered_pairs = generate_uncovered_pairs(parameters, t)
test_case = []
while uncovered_pairs is not empty:
    # generate_candidate_test_cases
    candidate_test_cases = []
    for m: 1 to M
        test_case = []
        test_case[0] = choose_best_first_value()
        for i: 1 to t
            for each value in parameters[i]:
                tmp_test_case[i] = value
                pairs_count = count_pairs(tmp_test_case, uncovered_pairs)
            best_value = choose_best_value()
            test_case[i] = best_value
            candidate_test_cases.append(test_case)
        for i: t+1 to k
            for each combination of t-1 parameters:
                for each value in parameters[i]:
                    test_case[i] = value
                    candidate_test_cases.append(test_case)
    test_case = choose_best_candidate(candidate_test_cases, uncovered_pairs)
    uncovered_pairs = update_uncovered_pairs(test_case, uncovered_pairs)
```]

=== Details
+ Random selection

    When selecting the first parameter and the best value for each parameters, we may encounter situations with multiple optimal solutions. In this case, I *ramdomly* choose one of them. If we always choose the first optimal solution, the algorithm may get stuck in a local optimal solution.
+ Dynamic M

    In the AETG algorithm, we use the greedy algorithm to generate test cases multiple times and finally select the one with the most coverage from these test cases. At the beginning, the algorithm can easliy find a test case that covers a lot of pairs. However, as the number of uncovered pairs decreases, the algorithm will be more difficult to find a test case that covers a lot of pairs. To solve this problem, I designed a dynamic method to adjust the number of M. 

#code(
    stepnumber:1,
    numbers: true,
)[```python
# User input the min and max value of M from the command line.
rate = 0
max_cover_count = int(math.factorial(len(parameters)) / math.factorial(t) / math.factorial(len(parameters) - t))
while len(uncovered_pairs) > 0:
    # aetg code...
    m = int(m_min + rate * (m_max - m_min))
    for m_cnt in range(m):
        # generate candidate test cases...
    rate = (max_cover_count - best_test_case[1])/(max_cover_count - 10)
    if rate > 1:
        rate = 1
```]

= Results
The complete results can be seen in file 'result/output_website_t-wise.csv'.
== JingDong
=== CIT Model
#code(
    stepnumber:1,
    numbers: true,
)[```python
# 品牌
brand = ['ThinkPad', 'DELL', '华为', 'Lenovo', 'Apple', 'hp', 'ASUS', 'MI', 'HONOR']
# 能效等级
energy_efficiency = ['一级', '二级', '三级']
# SSD
ssd = ['3TB', '128GB', '256GB+1TB', '512GB+2TB', '3TB*2']
# 厚度
thickness = ['15.0mm及以下', '15.1-18.0mm', '18.1-20.0mm', '20.0mm以上']
# 机身材质
body_material = ['金属', '金属+复合材质', '复合材质', '含碳纤维']
# 屏幕尺寸
screen_size = ['13.0英寸以下', '13.0-13.9英寸', '14.0-14.9英寸', '15.0-15.9英寸', '16.0-16.9英寸']
# 刷新率
refresh_rate = ['144Hz', '60Hz', '120Hz', '90Hz', '165Hz']
```]

=== Partial Test Cases
+ 2-wise
    #figure(
        image("assets/2023-12-18-13-41-57.png", width: 100%),
        caption: "2-wise-jingdong",
    )
+ 3-wise
    #figure(
        image("assets/2023-12-18-13-44-08.png", width: 100%), 
        caption: "3-wise-jingdong" 
    )

== XieCheng
=== CIT Model
#code(
    stepnumber:1,
    numbers: true,
)[```python
# 票型
ticket_type = ['单程', '往返', '多程']
# 出发地
start = ['国内', '国际·中国港澳台热门', '亚洲', '欧洲', '美洲', '非洲', '大洋洲']
# 目的地
end = ['国内', '国际·中国港澳台热门', '亚洲', '欧洲', '美洲', '非洲', '大洋洲']
# 仅看直飞
direct = ['是', '否']
# 舱型
cabin_type = ['经济/超经舱', '公务/头等舱', '公务舱', '头等舱']
# 乘客类型
customer = ['仅成人', '成人与儿童', '成人与婴儿', '成人与儿童与婴儿']
```]

= Conclusion and Discussion
=== Partial Test Cases
+ 2-wise
    #figure(
        image("assets/2023-12-18-13-45-20.png", width: 100%),   
        caption: "2-wise-xiecheng"
    )
+ 3-wise
    #figure(
    image("assets/2023-12-18-13-53-04.png", width: 100%),
    caption: "3-wise-xiecheng",
    )

#show: bibliography(
    "assets/ref.bib",
    title: "References"
)

