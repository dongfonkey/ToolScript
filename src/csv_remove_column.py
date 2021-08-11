import argparse

def main():
    parser = argparse.ArgumentParser(description="将CSV文件按某一字段排序")
    parser.add_argument("-f", "--file", help="原始文件名", dest="source_file", type=str)
    parser.add_argument("-t", "--title", help="删除依据的字段", dest="title", type=str)
    parser.add_argument("-o", "--output", help="输出文件名", dest="output", type=str)
    args = parser.parse_args()



    with open(args.source_file, encoding="utf-8") as fr:
        line = fr.readline()
        title_list = line.split(",")
        index = title_list.index(args.title)
        while line != "":
            item_list = line.split(",")
            del item_list[index]
            write_str = ",".join(item_list)
            with open(args.output, "a", encoding="utf-8") as fw:
                fw.write(write_str + "\n")
            fw.close()
            line = fr.readline()
    fr.close()



    print("********************\nAll Done !!!\n********************")



if __name__ == '__main__':
    main()