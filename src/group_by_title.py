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
    parser.add_argument("-t", "--title", help="分组依据的字段", dest="title", type=str)
    parser.add_argument("-g", "--group", help="分组类别", dest="group", type=str, default=None)
    args = parser.parse_args()


    #csv转dict的list
    item_list = []
    with open(args.source_file, encoding="utf-8") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            item_dict = dict(row)
            item_list.append(item_dict)
    fr.close()

    if args.group != None:
        group_list = args.group.split(",")
    else:
        group_set = set()
        for item in item_list:
            group_set.add(item[args.title])
        group_list = list(group_set)

    head = item_list[0].keys()
    for group in group_list:
        with open(group + ".csv", "w", encoding="utf-8") as fw:
            fw.write(",".join(head) + "\n")
        fw.close()
    with open("其它.csv", "w", encoding="utf-8") as fw:
        fw.write(",".join(head) + "\n")
    fw.close()
    for item in item_list:
        if item[args.title] in group_list:
            write_to_csv(item, head, item[args.title]+".csv")
        else:
            write_to_csv(item, head, "其它.csv")

    print("********************\nAll Done !!!\n********************")



if __name__ == '__main__':
    main()