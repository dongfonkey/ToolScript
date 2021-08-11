import argparse
import csv

def write_to_csv(dict_item, head, path):
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writerow(dict_item)
    f.close()


def main():
    parser = argparse.ArgumentParser(description="将txt文件按分隔符转换为csv")
    parser.add_argument("-f", "--file", help="文件名称或文件路径", dest="file", type=str)
    parser.add_argument("-o", "--output", help="输出文件名称或文件路径，默认与输入文件同名",dest="output", type=str, default=None)
    parser.add_argument("-s", "--splitLabel", help="分隔符", dest="split_label", type=str, default="\t")
    args = parser.parse_args()

    

    index = 1
    input = args.file
    output = args.output
    print(repr(args.split_label).replace("'", ""))
    if output is None:
        output = ".".join(input.split(".")[:-1]) + ".csv"
        error_output = ".".join(input.split(".")[:-1]) + " error.csv"

    #print(split_label)
    with open(input, encoding="utf-8") as fr:
        head = repr(fr.readline().replace("\n", ""))[1:-1].split(repr(args.split_label)[1:-1].replace("\\\\", "\\"))
        print(head)
        #head = head
        #print(head)
        #清理输出文件，并写入头部
        with open(output, "w", encoding="utf-8") as fw_clean:
            fw_clean.write(",".join(head) + "\n")
        fw_clean.close()
        item_count = len(head)
        while True:
            line = fr.readline()
            if line == "":
                break
            else:
                info_list = repr(line.replace("\n", ""))[1:-1].split(repr(args.split_label)[1:-1].replace("\\\\", "\\"))
                if len(info_list) == item_count:
                    csv_dict = {}
                    for i in range(0, item_count):
                        csv_dict[head[i]] = info_list[i]
                    write_to_csv(csv_dict, head, output)
                else:
                    with open(error_output, "a", encoding="utf-8") as err_fw:
                        err_fw.write(line)
                    err_fw.close()
                print(str(index) + "\t has done!!!")
                index += 1
    fr.close()

    print("All Done !!!")

if __name__ == "__main__":
    main()