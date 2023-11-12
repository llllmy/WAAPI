import tkinter as tk
from tkinter import filedialog
import subprocess

def browse_path(entry):
    """ 打开文件夹选择对话框并更新对应的文本框 """
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)  # 清除当前文本框内容
    entry.insert(0, folder_path)  # 插入新选择的路径
def run_other_script():
    """ 运行另一个 Python 脚本 """
    param1 = entry1.get()
    param2 = entry2.get()
    subprocess.run(["python", "导入.py",param1,param2])


# 创建根窗口
global entry1
global entry2
if __name__ == "__main__":
    root = tk.Tk()
    root.title("导入音频")

    # 创建第一个带有浏览按钮的框架
    frame1 = tk.Frame(root)
    frame1.pack(padx=10, pady=5)

    entry1 = tk.Entry(frame1, width=40)
    entry1.pack(side=tk.LEFT, padx=5)

    button1 = tk.Button(frame1, text="音频文件路径", command=lambda: browse_path(entry1))
    button1.pack(side=tk.LEFT)

    # 创建第二个带有浏览按钮的框架
    frame2 = tk.Frame(root)
    frame2.pack(padx=10, pady=5)

    entry2 = tk.Entry(frame2, width=40)
    entry2.pack(side=tk.LEFT, padx=5)

    button2 = tk.Button(frame2, text="Wwise存放路径", command=lambda: browse_path(entry2))
    button2.pack(side=tk.LEFT)

    # 创建一个新的按钮，放在下面
    new_button = tk.Button(root, text="导入", command=run_other_script)
    new_button.pack(pady=10)

    # 运行主事件循环
    root.mainloop()
