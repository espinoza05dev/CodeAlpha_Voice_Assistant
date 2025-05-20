def supoorted_languages(code = 1):
    import json
    with open("words/Languages.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        #if code is equal to one returns the code language else returns exit comand
        code_comand = [lang["code"] for lang in data["languages"]] if code == 1 else [comand["comand"] for comand in data["languages"]]
        return code_comand