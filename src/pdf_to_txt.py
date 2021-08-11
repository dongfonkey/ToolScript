import pdfminer
import argparse
from pdfminer.high_level import extract_text

def main():
    parser = argparse.ArgumentParser(description="将PDF中的文本抽取为txt")
    parser.add_argument("-f", "--file", help="PDF文件名", dest="source_file", type=str)
    parser.add_argument("-o", "--output", help="输出文件的文件名", dest="output_file", default="none", type=str)
    args = parser.parse_args()

    text = extract_text(args.source_file)
    text = text.replace("\n\n", " ")
    text = text.replace("\n", " ")
    while(text.find("  ") != -1):
        text = text.replace("  ", " ")


    if args.output_file == "none":
        output = args.source_file.replace(".pdf", "") + ".txt"
    else:
        output = args.output_file

    with open(output, "w", encoding="utf-8") as fw:
        fw.write(text)
    fw.close()
    print("Done !!!")

if __name__ == "__main__":
    main()