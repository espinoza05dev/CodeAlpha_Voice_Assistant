def supoorted_languages():
    import json
    with open("words/Languages.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        codes = [lang["code"] for lang in data["languages"]]
        return codes
