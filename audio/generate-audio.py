#!/usr/bin/env python3
"""
使用 gtts (Google Text-to-Speech) 生成听力音频
需要安装: pip install gtts
"""

from gtts import gTTS
import os

# 对话内容
dialogues = [
    {
        "filename": "listening1.mp3",
        "text": "What time does the train leave? It leaves at 9:30. And when does it arrive? It arrives at 11:15."
    },
    {
        "filename": "listening2.mp3",
        "text": "How much is this book? It's 10 pounds. Do you have a discount? Yes, students get 20% off."
    }
]

# 生成音频
print("正在生成音频...")

for dialogue in dialogues:
    print(f"生成 {dialogue['filename']}...")
    tts = gTTS(text=dialogue['text'], lang='en', slow=False)
    tts.save(dialogue['filename'])
    print(f"✓ {dialogue['filename']} 已生成")

print("\n✅ 所有音频生成完成！")
