import json
#解析json

"""
json.load() 从文件中读取json数据
json.dump() 将数据写入文件
json.loads() 从字符串中读取json数据
json.dumps() 将数据写入字符串
"""

def parse_json_file(json_file):
    with open(json_file) as f:
        obj = json.load(f)
        print(obj)


def dump_data_json(data):
    with open("b.json", "w", encoding="utf-8") as f:
        # ensure_ascii=False: 不转换为ascii码
        # indent=4: 缩进4个空格
        json.dump(data, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    # parse_json_file("a.json")

    d1 = {
        "uid":3001,
        "name": "张三",
        "age": 18,
        "scores":[100, 99, 98]
    }

    # dump_data_json(d1)


