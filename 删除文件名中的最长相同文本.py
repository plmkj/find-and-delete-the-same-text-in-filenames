import os
from collections import defaultdict

def find_longest_common_part(filenames):
    # 提取文件名（不包括后缀）
    base_names = [os.path.splitext(f)[0] for f in filenames]
    
    # 用于存储所有可能的公共部分及其出现次数
    common_parts = defaultdict(int)
    
    # 遍历所有文件名，找到所有可能的公共部分
    for base_name in base_names:
        for i in range(len(base_name)):
            for j in range(i + 1, len(base_name) + 1):
                substring = base_name[i:j]
                if all(substring in base for base in base_names):
                    common_parts[substring] += 1
    
    # 找到最长的公共部分
    longest_common_part = ""
    for part, count in common_parts.items():
        if count == len(base_names) and len(part) > len(longest_common_part):
            longest_common_part = part
    
    return longest_common_part

def remove_common_part_and_rename(folder_path):
    try:
        # 检查文件夹路径是否存在
        if not os.path.exists(folder_path):
            print("指定的文件夹路径不存在，请检查路径是否正确。")
            return
        
        # 获取文件夹中的所有文件名
        filenames = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        if len(filenames) < 2:
            print("文件夹中文件数量不足，无法进行操作。")
            return
        
        # 找到所有文件名的最长公共部分（不包括后缀）
        longest_common_part = find_longest_common_part(filenames)
        print(f"找到的最长公共部分为: {longest_common_part}")
        
        if not longest_common_part:
            print("没有找到公共部分，无需重命名。")
            return
        
        # 确认是否继续操作
        confirm = input("是否删除最长公共部分并重命名文件？(y/n): ")
        if confirm.lower() != 'y':
            print("操作已取消。")
            return
        
        # 删除最长公共部分并重命名文件
        for filename in filenames:
            base_name, extension = os.path.splitext(filename)
            new_base_name = base_name.replace(longest_common_part, "")
            if new_base_name == base_name:
                print(f"文件 {filename} 没有最长公共部分，跳过。")
                continue
            new_name = new_base_name + extension
            new_path = os.path.join(folder_path, new_name)
            old_path = os.path.join(folder_path, filename)
            os.rename(old_path, new_path)
            print(f"文件 {filename} 已重命名为 {new_name}")
    
    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
try:
    folder_path = input("请输入文件夹路径: ")
    remove_common_part_and_rename(folder_path)
except Exception as e:
    print(f"程序运行出错: {e}")