#统计每个key中有数据的条目占总条目的比例
import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description="抽取文件的前n行")
    parser.add_argument("-f", "--file", help="输出文件名称或路径", dest="file", type=str)
    parser.add_argument("-o", "--output", help="结果输出文件路径（不指定时默认在控制台中打印）", dest="output", type=str, default=None)
    parser.add_argument("-n", help="欲抽取的行数", dest="line_count", type=int)
    args = parser.parse_args()


    input = args.file
    output = args.output
    line_count = args.line_count
    lines_list = []

    with open(input, 'r', encoding='utf-8') as fr:
        for index in range(0,line_count):
            line_content = fr.readline()
            lines_list.append(line_content)
    fr.close()

    #输出
    if output == None:
        for line_content in lines_list:
            print(line_content)
    else:
        with open(output, "w", encoding="utf-8") as fw:
            for line_content in lines_list:
                fw.write(line_content)
        fw.close()
    
    print("All Done !!!")

if __name__ == "__main__":
    main()
