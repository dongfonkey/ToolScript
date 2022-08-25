#统计文件的行数
import argparse


def main():
    parser = argparse.ArgumentParser(description="统计文件的行数")
    parser.add_argument("-f", "--file", help="欲统计文件名称或路径", dest="file", type=str)
    args = parser.parse_args()

    
    line_count = 0

    with open(args.file, encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                line_count += 1
    
    print("改文件的行数为：{}".format(line_count))





if __name__ == "__main__":
    main()
