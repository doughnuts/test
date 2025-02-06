import yaml

with open("a.yaml", mode="rt", encoding="utf-8") as f:
    print(yaml.load(f, Loader=yaml.SafeLoader))


with open("a.yaml", mode="at", encoding="utf-8") as f:
    yaml.dump({"admin":[{'name': '张三', 'age': 18},{'name':'李四','age':55}]}, f, allow_unicode=True)
