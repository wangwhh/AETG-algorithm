import numpy as np
import itertools
from collections import Counter
import math

def AETG(parameters, t, m_max, m_min):
    uncovered_pairs = np.array(generate_ucps(parameters, t))
    test_case = []
    rate = 0
    max_cover_count = int(math.factorial(len(parameters)) / math.factorial(t) / math.factorial(len(parameters) - t))
    while len(uncovered_pairs) > 0:
        # 生成m个候选测试用例
        candidate_test_cases = []
        m = int(m_min + rate * (m_max - m_min))
        for m_cnt in range(m):
            tmp_test_case = [-1] * len(parameters)
            # 选择 uncovered pair 中出现频率最高的参数和其取值
            parameter_index = []
            for i in range(len(parameters)):
                counter = Counter(uncovered_pairs[:, i])
                if -1 in counter:
                    del counter[-1]
                if len(counter) == 0:
                    parameter_index.append(([], 0))
                    continue
                max_count = max(counter.values())
                most_common_elements = [key for key, count in counter.items() if count == max_count]
                parameter_index.append((most_common_elements, max_count))
            # 选择出现频率最高的参数
            max_parameter_count = max(parameter_index, key=lambda x: x[1])
            max_parameter = [i for i in range(len(parameter_index)) if parameter_index[i][1] == max_parameter_count[1]]
            # 随机选一个最大的参数
            max_parameter = np.random.choice(max_parameter)
            
            # 从该参数随机选择一个取值
            max_parameter_value = parameter_index[max_parameter][0]
            max_parameter_value = np.random.choice(max_parameter_value)
            
            # 让测试用例的第一个参数等于该取值
            tmp_test_case[max_parameter] = max_parameter_value
            
            # 将后面的列随机排列 
            list1 = list(range(0, max_parameter))
            list2 = list(range(max_parameter + 1, len(parameters)))
            random_params = list1 + list2
            np.random.shuffle(random_params)
            random_params = [max_parameter] + random_params
            for i in range(1, t):
                index = random_params[i]
                # 选择包含该组合最多的 uncovered pairs 的参数
                best_values = []
                # 选择包含该组合最多的 uncovered pairs 的参数
                for i in range(parameters[index]):
                    new_case = tmp_test_case[:]
                    new_case[index] = i
                    count = 0
                    for pair in uncovered_pairs:
                        if is_contained(pair, new_case):
                            count += 1
                            break
                    if len(best_values) != 0 and count > best_values[0][1]:
                        best_values.clear()
                        best_values.append((i, count))
                    elif len(best_values) == 0 or count == best_values[0][1]:
                        best_values.append((i, count))
                # 从中随机选择一个
                best_value = np.array(best_values)[:, 0]
                best_value = np.random.choice(best_value)
                tmp_test_case[index] = best_value
            
            for i in range(t, len(parameters)):
                index = random_params[i]
                count = 0
                # 从已生成的测试用例中选择 t - 1 个参数
                combinations = itertools.combinations(range(0, i), t - 1)
                best_values = []
                for j in range(parameters[index]):
                    for comb in combinations:
                        new_case = [-1] * len(parameters)
                        for k in comb:
                            new_case[random_params[k]] = tmp_test_case[random_params[k]]
                        new_case[index] = j
                        for pair in uncovered_pairs:
                            if is_contained(pair, new_case):
                                count += 1
                                break
                    if len(best_values) != 0 and count > best_values[0][1]:
                        best_values.clear()
                        best_values.append((j, count))
                    elif len(best_values) == 0 or count == best_values[0][1]:
                        best_values.append((j, count))
                best_value = np.array(best_values)[:, 0]
                tmp_test_case[index] = np.random.choice(best_value)
                

            # 至此生成了一个测试用例
            covered_pairs = count_covered_pairs(tmp_test_case, uncovered_pairs, t)
            candidate_test_cases.append((tmp_test_case, covered_pairs))
        
        # 选择一个效果最好的加入测试用例集
        best_test_case = max(candidate_test_cases, key=lambda x: x[1])
        test_case.append(best_test_case)
        # 从 uncovered pairs 中删除该测试用例覆盖的所有 pair
        uncovered_pairs = delete_pairs(best_test_case[0], uncovered_pairs, t)
        # 随 count 减少增加 m
        rate = (max_cover_count - best_test_case[1])/(max_cover_count - 10)
        if rate > 1:
            rate = 1
            
    return test_case
    
        
def generate_ucps(parameters, t):
    # Generate all possible t-way combinations of parameters
    uncovered_pairs = []
    param_combinations = itertools.combinations(range(len(parameters)), t)

    for combo in param_combinations:
        # Create a list representing a t-way combination with -1 for unselected parameters
        lists = []
        for index in combo:
            lists.append(range(parameters[index]))
        pairs = itertools.product(*lists)
        for p in pairs:
            pair = [-1] * len(parameters)
            for i in range(len(combo)):
                pair[combo[i]] = p[i]
            uncovered_pairs.append(pair)

    return uncovered_pairs
    

def count_covered_pairs(test_case, uncovered_pairs, t):
    count = 0
    combinations = itertools.combinations(range(len(test_case)), t)
    for comb in combinations:
        new_case = [-1] * len(test_case)
        for i in comb:
            new_case[i] = test_case[i]
        for pair in uncovered_pairs:
            if is_contained(pair, new_case):
                count += 1
                break
    return count


def delete_pairs(test_case, uncovered_pairs, t):
    combinations = itertools.combinations(range(len(test_case)), t)
    count = 0
    for comb in combinations:
        new_case = [-1] * len(test_case)
        for i in comb:
            new_case[i] = test_case[i]
        size = len(uncovered_pairs)
        for i in range(size):
            pair = uncovered_pairs[i]
            if is_contained(pair, new_case):
                uncovered_pairs = np.delete(uncovered_pairs, i, 0)
                count+=1
                break
    return uncovered_pairs
                
def is_contained(pair, test_case):
    for i in range(len(pair)):
        if test_case[i] != -1 and pair[i] != test_case[i]:
            return False
    return True