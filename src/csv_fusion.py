import argparse
import os

def file_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root, dirs, files


def main():
    parser = argparse.ArgumentParser(description="将CSV文件按某一字段排序")
    parser.add_argument("-f", "--folder", help="存放聚合文件的文件夹", dest="source_folder", type=str)
    parser.add_argument("-o", "--output", help="输出的文件路径（文件名）", dest="output", type=str)
    args = parser.parse_args()


    #Define
    source_folder = args.source_folder
    output_path = args.output
    first_file_status = True

    #获取文件夹下的文件列表
    source_root, source_dirs, source_files = file_walk(source_folder)
    #随意读取一个文件表头，并写入最终文件中
    with open(os.path.join(source_root, source_files[0]), 'r', encoding='utf-8') as f_firstline:
        head = f_firstline.readline()
    f_firstline.close()
    with open(output_path, "w", encoding='utf-8') as f_clean:
        f_clean.write(head)
    f_clean.close()

    with open(output_path, 'a', encoding='utf-8') as fw:
        for file in source_files:
            file_path = os.path.join(source_root, file)
            with open(file_path, "r", encoding='utf-8') as fr:
                head = fr.readline()
                while True:
                    line = fr.readline()
                    if line != "":
                        fw.write(line)
                    else:
                        break
            fr.close()
            print(file_path + "\thas done!!!")
    fw.close()



if __name__ == '__main__':
    main()