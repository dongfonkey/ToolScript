import argparse

def main():
    parser = argparse.ArgumentParser(description="将txt文件中每行的内容去重")
    parser.add_argument("-f", "--file", help="文件名或文件路径", dest="file", type=str)
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as fr:
        lines = fr.readlines()
    fr.close()

    lines = list(set(lines))

    with open(args.file.replace(".txt", "") + " de_emphasised.txt", "w", encoding="utf-8") as fw:
        fw.writelines(lines)
    fw.close()

    print("File de-emphasis done !!!")

if __name__ == "__main__":
    main()