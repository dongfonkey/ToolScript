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
    parser.add_argument("-t", "--title", help="排序依据的字段", dest="title", type=str)
    args = parser.parse_args()


    #csv转dict的list
    item_list = []
    with open(args.source_file, encoding="utf-8") as fr:
        reader = csv.DictReader(fr)
        for row in reader:
            item_dict = dict(row)
            item_list.append(item_dict)
    fr.close()

    sum = 0
    for item in item_list:
        sum += int(item[args.title])

    print("********************\nSUM:\t" + str(sum) + "\n********************")



if __name__ == '__main__':
    main()