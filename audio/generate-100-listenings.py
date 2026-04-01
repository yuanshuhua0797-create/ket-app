#!/usr/bin/env python3
"""
生成 100 套简单的 KET 听力对话和题目
"""

import json
from gtts import gTTS
import random

# 简单对话模板（所有占位符都是显式的）
simple_dialogues = [
    {
        "text": "What time does the library open? It opens at nine. And when does it close? It closes at five.",
        "question": "图书馆什么时候关闭？",
        "options": ["九点", "五点", "六点", "七点"],
        "answer": 1
    },
    {
        "text": "How much is this book? It's ten pounds. Do you have a discount? Yes, students get twenty percent off.",
        "question": "这本书学生买多少钱？",
        "options": ["2 pounds", "8 pounds", "10 pounds", "12 pounds"],
        "answer": 1
    },
    {
        "text": "Where should we meet? Let's meet at the station. What time? At three o'clock.",
        "question": "他们将在哪里见面？",
        "options": ["公园", "车站", "学校", "餐厅"],
        "answer": 1
    },
    {
        "text": "How many books do you need? I need two. What about pens? I need three.",
        "question": "需要几本书？",
        "options": ["两本", "三本", "四本", "五本"],
        "answer": 0
    },
    {
        "text": "Which shirt do you like? I like the red one. What about the blue one? That's too big.",
        "question": "说话人喜欢哪种颜色的衬衫？",
        "options": ["红色", "蓝色", "绿色", "黄色"],
        "answer": 0
    },
    {
        "text": "When is your party? It's on Saturday. What time does it start? At seven.",
        "question": "派对是什么时候？",
        "options": ["周一", "周六", "周三", "周日"],
        "answer": 1
    },
    {
        "text": "Who is coming to the party? Tom and Mary are coming. What about John? No, he can't come.",
        "question": "谁会来参加派对？",
        "options": ["Tom", "Mary", "John", "Tom和Mary"],
        "answer": 3
    },
    {
        "text": "How do you go to school? I take the bus. How long does it take? About twenty minutes.",
        "question": "说话人怎么去学校？",
        "options": ["步行", "坐车", "骑车", "坐公交"],
        "answer": 3
    },
    {
        "text": "What's the weather like today? It's sunny. What about tomorrow? It will be cloudy.",
        "question": "今天天气怎么样？",
        "options": ["晴朗", "多云", "下雨", "刮风"],
        "answer": 0
    },
    {
        "text": "What would you like to eat? I'd like pizza. Would you like hamburger? No, thank you.",
        "question": "说话人想吃什么？",
        "options": ["披萨", "汉堡", "三明治", "沙拉"],
        "answer": 0
    },
    {
        "text": "What time does the museum close? It closes at six. Is it open on Sunday? Yes, it is.",
        "question": "博物馆几点关闭？",
        "options": ["四点", "五点", "六点", "七点"],
        "answer": 2
    },
    {
        "text": "How much is that ticket? It's fifteen pounds. Can I get a discount? Yes, with a student card.",
        "question": "票多少钱？",
        "options": ["10 pounds", "15 pounds", "20 pounds", "25 pounds"],
        "answer": 1
    },
    {
        "text": "What color is your bag? It's black. Do you like blue bags? Yes, I do.",
        "question": "包是什么颜色的？",
        "options": ["黑色", "蓝色", "红色", "白色"],
        "answer": 0
    },
    {
        "text": "When is the meeting? It's on Friday morning. Where? In the office.",
        "question": "会议是什么时候？",
        "options": ["周五上午", "周五下午", "周六上午", "周日"],
        "answer": 0
    },
    {
        "text": "How many people are there? There are thirty. Are they all students? Most of them are.",
        "question": "有多少人？",
        "options": ["20人", "30人", "40人", "50人"],
        "answer": 1
    }
]

# 生成100套（循环使用模板）
print("正在生成 100 套听力对话...")

all_dialogues = []
for i in range(100):
    template = simple_dialogues[i % len(simple_dialogues)]
    
    # 为了增加多样性，修改数字、颜色等
    modified_text = template["text"]
    modified_options = template["options"].copy()
    
    # 简单替换（每10套更换一次模式）
    if i // 10 % 2 == 1:
        # 模式2：修改数字
        num_map = {
            "two": "four",
            "three": "five",
            "ten": "twenty",
            "nine": "eight",
            "five": "six",
            "six": "seven",
            "twenty": "thirty",
            "thirty": "forty"
        }
        for word, replacement in num_map.items():
            modified_text = modified_text.replace(f" {word} ", f" {replacement} ")
    elif i // 10 % 2 == 2:
        # 模式3：修改颜色
        color_map = {
            "red": "blue",
            "blue": "green",
            "green": "yellow",
            "black": "white",
            "white": "orange"
        }
        for word, replacement in color_map.items():
            modified_text = modified_text.replace(f" {word} ", f" {replacement} ")
    
    # 生成音频
    print(f"生成第 {i+1} 套音频...")
    tts = gTTS(text=modified_text, lang='en', slow=False)
    filename = f"listening{i+1}.mp3"
    tts.save(filename)
    print(f"✓ {filename} 已生成")
    
    # 保存数据
    all_dialogues.append({
        "dialogue": modified_text,
        "audioFile": f"audio/listening{i+1}.mp3",
        "question": template["question"],
        "options": modified_options,
        "answer": template["answer"]
    })

# 保存为 JSON 文件
with open('listening_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_dialogues, f, ensure_ascii=False, indent=2)

print(f"\n✅ 已生成 100 套听力对话和音频！")
print(f"   音频文件: listening1.mp3 ~ listening100.mp3")
print(f"   数据文件: listening_data.json")
