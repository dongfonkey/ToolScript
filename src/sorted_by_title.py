import argparse
import csv

def write_to_csv(dict_item, head, path):
    with open(path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writerow(dict_item)
    f.close()


def main():
    parser = argparse.ArgumentParser(description="将CSV文件按某一字段排序")
    parser.add_argument("-f", "--file", help="原始文件名", dest="source_file", type=str)
    parser.add_argument("-o", "--output", help="输出文件的文件名", dest="output", default="output.csv", type=str)
    parser.add_argument("-t", "--title", help="排序依据的字段", dest="title", type=str)
    parser.add_argument("-r", "--reverse", help="是否降序", dest="reverse", default="True", type=str)
    args = parser.parse_args()


    #csv转dict的list
    item_list = []
    with open(args.source_file, encoding="utf-8") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            item_dict = dict(row)
            item_list.append(item_dict)
    fr.close()

    if args.reverse == "True":
        re_list = sorted(item_list, key=lambda x:float(x[args.title]), reverse=True)
    elif args.reverse == "False":
        re_list = sorted(item_list, key=lambda x:float(x[args.title]), reverse=False)

    head = re_list[0].keys()
    with open(args.output, "w", encoding="utf-8") as fw:
        fw.write(",".join(head) + "\n")
    fw.close()
    for sorted_item in re_list:
        write_to_csv(sorted_item, head, args.output)

    print("********************\nAll Done !!!\n********************")



if __name__ == '__main__':
    main()