
def extract_name(s):
    # 分割字符串，限定分割次数为最后一个下划线之前
    parts = s.rsplit('_', 1)
    # 返回分割后的第一个部分
    return parts[0] if len(parts) > 1 else s

# 测试字符串
test_str = "Ambient_Biology_01"
result = extract_name(test_str)
print(result)  # 输出: Ambient_Biology
