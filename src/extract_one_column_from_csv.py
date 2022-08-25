#从csv中单独抽取出一列
import argparse
import csv
import sys

maxInt = sys.maxsize


while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

def write_to_csv(dict_item, head, path):
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writerow(dict_item)
    f.close()

def main():
    parser = argparse.ArgumentParser(description="按照列名单独抽取csv中的一列")
    parser.add_argument("-f", "--file", help="输入文件名称或路径", dest="file", type=str)
    parser.add_argument("-o", "--output", help="结果输出文件路径（不指定时默认在控制台中打印）", dest="output", type=str, default=None)
    parser.add_argument("-t", help="欲抽取的csv文件的列名", dest="line_count", type=str)
    args = parser.parse_args()


    input = args.file
    output = args.output
    title = args.line_count


    #初始化
    with open(output, "w", encoding="utf-8") as f_clean:
        f_clean.write(title + "\n")
    f_clean.close

    header = [title]
    with open(input, 'r', encoding='utf-8') as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            info_dict = {
                title: row[title]
            }
            write_to_csv(info_dict, header, output)
    fr.close()
            
    
    print("All Done !!!")

if __name__ == "__main__":
    main()
