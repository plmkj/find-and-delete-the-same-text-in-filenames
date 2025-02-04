import os
from itertools import combinations

def find_common_substrings(file_names):
    # 获取所有可能的子串
    def get_substrings(s):
        return {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}

    # 找出所有文件名的公共子串
    common_substrings = get_substrings(file_names[0])
    for file_name in file_names[1:]:
        common_substrings = common_substrings.intersection(get_substrings(file_name))

    return common_substrings

def remove_common_substrings(file_names, common_substrings):
    new_file_names = []
    for file_name in file_names:
        new_name = file_name
        for substring in common_substrings:
            new_name = new_name.replace(substring, '')
        new_file_names.append(new_name)
    return new_file_names

def process_files_in_folder(folder_path):
    # 获取文件夹中的所有文件名
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    file_names = [os.path.splitext(f)[0] for f in files]  # 提取文件名（不包含后缀）
    extensions = [os.path.splitext(f)[1] for f in files]  # 提取文件后缀

    # 找出所有公共子串
    common_substrings = find_common_substrings(file_names)

    # 移除公共子串
    new_file_names = remove_common_substrings(file_names, common_substrings)

    # 重新组合文件名和后缀
    new_file_paths = [os.path.join(folder_path, new_name + ext) for new_name, ext in zip(new_file_names, extensions)]
    old_file_paths = [os.path.join(folder_path, f) for f in files]

    # 打印结果
    print("原始文件名：", files)
    print("公共子串：", common_substrings)
    print("新文件名：", [os.path.basename(new_path) for new_path in new_file_paths])

    # 确认是否重命名
    confirm = input("是否确认重命名文件？(y/n): ")
    if confirm.lower() == 'y':
        for old_path, new_path in zip(old_file_paths, new_file_paths):
            os.rename(old_path, new_path)
        print("文件重命名完成！")
    else:
        print("操作已取消。")

if __name__ == "__main__":
    folder_path = input("请输入文件夹路径：")
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        process_files_in_folder(folder_path)
    else:
        print("输入的路径无效，请检查路径是否正确！")