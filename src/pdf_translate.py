import pdfminer
import argparse
from pdfminer.high_level import extract_text
import json
import requests
from hashlib import md5
import random
import time


def read_config(config_path):
    config_fr = open(config_path, encoding="utf-8")
    config = json.load(config_fr)
    config_fr.close()
    return config["appid"], config["key"]


def MD5(message):
    MD5_message = md5(message.encode('utf-8')).hexdigest()
    return MD5_message


def translate(q, appid, key):
    salt = random.randint(1000000000, 9999999999)
    sign = MD5(appid + q + str(salt) + key)
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=" + q + "&from=en&to=zh&appid=" + appid + "&salt=" + str(salt) + "&sign=" + sign
    try:
        r = requests.get(url)
        res_dict = json.loads(r.text)
        translated_message = res_dict["trans_result"][0]["dst"]
        return translated_message
    except:
        return "error"


def main():
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    appid, key = read_config(dirname + "\pdf_translate_config.json")

    parser = argparse.ArgumentParser(description="将PDF中的文本抽取为txt")
    parser.add_argument("-f", "--file", help="PDF文件名", dest="source_file", type=str)
    parser.add_argument("-o", "--output", help="输出文件的文件名", dest="output_file", default="none", type=str)
    args = parser.parse_args()

    text = extract_text(args.source_file)
    text = text.replace("\n\n", " ")
    text = text.replace("\n", " ")
    while(text.find("  ") != -1):
        text = text.replace("  ", " ")

    sentences = text.split(". ")
    total_count = str(len(sentences))

    if args.output_file == "none":
        output = args.source_file.replace(".pdf", "") + " chinese.txt"
    else:
        output = args.output_file

    with open(output, "w", encoding="utf-8") as fw:
        fw.write("")
    fw.close()

    
    index = 1
    for sentence in sentences:
        sentence = sentence + "."
        translated_sentence = translate(sentence, appid, key)
        if translated_sentence != "error":
            with open(output, "a", encoding="utf-8") as fw_t:
                fw_t.write(translated_sentence + "\n")
            fw_t.close()
            print("Translate:\t" + str(index) + "/" + total_count)
        else:
            print("ERROR:\t" + str(index) + "/" + total_count)
        index += 1
        time.sleep(1)
    
    print("**************\nALL DONE\n**************")


if __name__ == "__main__":
    main()