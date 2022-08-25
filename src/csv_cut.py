#将csv按照行数切片
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
    parser = argparse.ArgumentParser(description="将文件按照允许的最大行数切片")
    parser.add_argument("-f", "--file", help="输入文件名称或路径", dest="file", type=str)
    parser.add_argument("-n", help="每个文件最大的行数", dest="line_count", type=int)
    args = parser.parse_args()


    input = args.file
    maxlineCount = args.line_count


    #抽取第一行作为header
    with open(input, "r", encoding="utf-8") as fr_header:
        header_line = fr_header.readline()
        header = header_line.replace("\n", "").split(",")
    fr_header.close()

    part_index = 1
    with open(input, "r", encoding="utf-8") as fr:
        reader = csv.DictReader(fr)
        line_index = 1
        #初始化part1
        with open(input.replace(".csv", "")+".part"+str(part_index)+".csv", "w", encoding="utf-8") as f_clean:
            f_clean.write(header_line)
        f_clean.close()
        for row in reader:
            info_dict = dict(row)
            write_to_csv(info_dict, header, input.replace(".csv", "")+".part"+str(part_index)+".csv")
            line_index += 1
            if line_index >= maxlineCount-1:
                line_index = 1
                part_index += 1
                with open(input.replace(".csv", "")+".part"+str(part_index)+".csv", "w", encoding="utf-8") as f_clean:
                    f_clean.write(header_line)
                f_clean.close()
    fr.close() 
    
    print("All Done !!!")

if __name__ == "__main__":
    main()