import shutil
import os

def config_read(filename, i):
    filename = filename
    line_read = i  # 读取第二行

    # 读取指定行内容
    with open(filename, 'r') as file:
        current_line = 1
        while current_line < line_read:
            file.readline()  # 跳过前面的行
            current_line += 1
        line = file.readline()  # 读取目标行内容
    result = line.split('=')[1].strip()
    result = fr"{result}"
    # print(result)
    return result

def config_write(filename, i, new_config):
    filename = filename
    line_number_to_modify = i  # 指定要修改的行号
    new_content = new_config+"\n"  # 替换为你想要修改的内容

    # 读取文件内容并修改指定行内容
    with open(filename, 'r', encoding="gbk") as file:
        lines = file.readlines()
        if line_number_to_modify <= len(lines):
            lines[line_number_to_modify - 1] = new_content  # 修改指定行内容
    # print(lines)
    # 将修改后的内容写回文件
    with open(filename, 'w', encoding="gbk") as file:
        file.writelines(lines)

def write(filename,new_text):
    with open(filename, "a") as file:
        # 写入字符串到文件
        file.write(new_text + "\n")


def copy_file(source_file, destination_dir):
    # 复制文件到目标目录
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    shutil.copy(source_file, destination_dir)
    # print(f"复制文件: {source_file} 到 {destination_dir}")

def read_last_line(file_path):
    with open(file_path, 'r') as file:
        # 使用 file.readlines() 读取所有行，并将其存储在列表中
        lines = file.readlines()
        # 如果文件为空，则返回空字符串
        if not lines:
            return ''
        # 返回列表中的最后一行
        return lines[-1]

def check_file(directory, filename):
    # 检查目录是否存在
    if os.path.isdir(directory):
        # 构建文件路径
        file_path = os.path.join(directory, filename)
        # 检查文件是否存在
        if os.path.isfile(file_path):
            download_successful = 1
        else:
            download_successful = 2 #下载失败
    else:
        download_successful = 3 # 下载目录出错
    return download_successful


def clear_folder(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 循环遍历文件夹中的文件
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, file)
        # 删除文件
        os.remove(file_path)


