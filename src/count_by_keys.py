#统计每个key中有数据的条目占总条目的比例
import argparse
import csv
import sys
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

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
    parser = argparse.ArgumentParser(description="统计csv中每个key中有数据的条目")
    parser.add_argument("-f", "--file", help="欲统计文件名称或路径", dest="file", type=str)
    parser.add_argument("-o", "--output", help="结果输出文件路径（不指定时默认在控制台中打印）", dest="output", type=str, default=None)
    args = parser.parse_args()

    start_state = 1
    input = args.file
    output = args.output
    keys_list = []
    keys_count = {}

    with open(input, 'r', encoding='utf-8') as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            #第一次运行获取keys构建数量的词典
            if start_state == 1:
                keys_list = list(dict(row).keys())
                for key in keys_list:
                    keys_count[key] = 0
                start_state = 0
                continue
            #遍历统计key的数量
            for key in keys_list:
                if row[key] != "":
                    keys_count[key] += 1
    fr.close()

    #输出
    if output == None:
        for key,value in keys_count.items():
            print(key,value)
    else:
        with open(output, "w", encoding="utf-8") as fw_clean:
            fw_clean.write(",".join(keys_list) + "\n")
        fw_clean.close()
        write_to_csv(keys_count, keys_list, output)
    
    print("All Done !!!")

if __name__ == "__main__":
    main()
