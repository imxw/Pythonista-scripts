#!python3
"""
卡片模板
"""

import keyboard
import dialogs

from datetime import datetime


def main():
    is_kb = keyboard.is_keyboard()
    options = [
        {"title": "通用型: 基础卡-内容", "key": "basic1"},
        {"title": "通用型: 基础卡-原文-评论", "key": "basic2"},
        {"title": "通用型: 行动卡", "key": "action"},
        {"title": "信息型: 新知卡", "key": "new"},
        {"title": "信息型: 术语卡", "key": "term"},
        {"title": "信息型: 人物卡", "key": "person"},
        {"title": "信息型: 图示卡", "key": "pic"},
        {"title": "叙事型: 事件卡-单一事件", "key": "event1"},
        {"title": "叙事型: 事件卡-时间线", "key": "event2"},
        {"title": "叙事型: 事件卡-故事卡", "key": "story"},
        {"title": "美感型: 新词卡", "key": "word"},
        {"title": "美感型: 金句卡-评论", "key": "sentence1"},
        {"title": "美感型: 金句卡-仿写", "key": "sentence2"},
    ]
    selected = dialogs.list_dialog("卡片模板", options)
    if not selected:
        return
    n = selected["key"]
    text = ""
    date_format = "%Y%m%d%H%M"
    now = datetime.now()
    date_str = now.strftime(date_format)
    if n == "basic1":
        text = f"title:: \n内容:: \nref:: \nuid:: {date_str}\ntype:: [[基础卡]]"
    elif n == "basic2":
        text = f"title:: \n原文:: \n评论:: \nref:: \nuid:: {date_str}\ntype:: [[基础卡]]"
    elif n == "action":
        text = f"title:: \n原理:: \n行动:: \nref:: \nuid:: {date_str}\ntype:: [[行动卡]]"
    elif n == "new":
        text = (
            f"title:: \n已知:: \n新知:: \neg:: \nref:: \nuid:: {date_str}\ntype:: [[新知卡]]"
        )
    elif n == "term":
        text = (
            f"title:: \n定义:: \n解释:: \neg:: \nref:: \nuid:: {date_str}\ntype:: [[术语卡]]"
        )
    elif n == "person":
        text = f"title:: \n小传:: \nref:: \nuid:: {date_str}\ntype:: [[人物卡]]"
    elif n == "pic":
        text = f"title:: \n说明:: \nref:: \nuid:: {date_str}\ntype:: [[图示卡]]"
    elif n == "event1":
        text = f"title:: \n时间:: \n地点:: \n行动者:: \n反应:: \nref:: \nuid:: {date_str}\ntype:: [[事件卡]]"
    elif n == "event2":
        text = f"title:: \n时间线:: \nref:: \nuid:: {date_str}\ntype:: [[事件卡]]"
    elif n == "story":
        text = f"title:: \n故事:: \nref:: \nuid:: {date_str}\ntype:: [[事件卡]]"
    elif n == "word":
        text = f"新词:: \n原句:: \n造句:: \nref:: \nuid:: {date_str}\ntype:: [[新词卡]]"
    elif n == "sentence1":
        text = f"title:: \n金句:: \n评论:: \nref:: \nuid:: {date_str}\ntype:: [[金句卡]]"
    elif n == "sentence2":
        text = f"title:: \n金句:: \n仿写:: \nref:: \nuid:: {date_str}\ntype:: [[金句卡]]"
    if is_kb:
        keyboard.insert_text(text)
    else:
        # For debugging in the main app:
        print("Keyboard input:\n", text)


if __name__ == "__main__":
    main()
