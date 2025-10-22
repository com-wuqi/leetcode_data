def compare_strings(a,b) -> int:
    """
    比较两个字符串的字典序
    返回: 1(a>b), -1(a<b), 0(相等)
    """
    min_lenth = min(len(a), len(b))
    
    for i in range(min_lenth):
        if a[i] != b[i]:
            return 1 if a[i] > b[i] else -1
    
    # 如果共同前缀都相同，比较长度
    if len(a) == len(b):
        return 0
    elif len(a) > len(b):
        return 1 # a>b
    else:
        return -1
