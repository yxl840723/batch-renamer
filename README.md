# Batch Renamer (批量重命名工具)

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## 🇬🇧 English

### Overview
Batch Renamer is a lightweight, graphical user interface (GUI) desktop application built with Python and Tkinter. It helps you quickly and efficiently batch rename multiple files within a directory based on a specific separator character.

### Key Features
* **Separator-Based Renaming:** Automatically removes all text *before* a specified separator character. (e.g., if the file is `2023-10-invoice.pdf` and the separator is `-`, the new name becomes `10-invoice.pdf`. If you use `-` again, `invoice.pdf`).
* **Extension Filtering:** Only process specific file types (e.g., `.pdf`, `.csv`), leaving other files in the same folder untouched.
* **Safe Preview:** Before any actual renaming occurs, the app generates a table previewing exactly how the old filenames map to the new filenames.
* **Conflict Prevention:** Checks if a file with the target name already exists to prevent accidental data overwriting.

### How to Use
1. **Choose a Folder:** Click "浏览..." (Browse) to select the folder containing the files you want to rename.
2. **Set Rules:**
   * **Target Extension (Optional):** Enter a file extension (like `.pdf`) to only target those files. Leave empty to target all file types.
   * **Separator Character:** Enter the character used to split your filename.
3. **Generate Preview:** Click "生成预览" (Generate Preview) to see the proposed changes in the table below.
4. **Execute:** If the preview looks correct, click the "⚡ 开始批量重命名" (Start Batch Rename) button at the bottom to apply the changes.

### Getting Started (Development)
1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the application:
   ```bash
   python batch_renamer.py
   ```

---

<a name="中文"></a>
## 🇨🇳 中文

### 简介
“批量重命名工具 (Batch Renamer)” 是一个基于 Python 和 Tkinter 开发的轻量级桌面图形化软件。它可以帮助你根据特定的“分隔符规则”，快速且高效地对一个文件夹下的多个文件进行批量重命名。

### 核心功能
* **按分隔符重命名：** 自动删除指定分隔符**之前**的所有内容。例如：文件名为 `项目A_财务报表.pdf`，如果分隔符设为 `_`，新文件名将变成 `财务报表.pdf`。
* **按扩展名过滤：** 可以指定只处理某种格式的文件（例如 `.pdf` 或 `.csv`），保护同文件夹下的其他文件不被误改。
* **安全预览：** 在实际执行修改之前，软件会生成一个表格，直观地左侧显示“原文件名”，右侧显示“新文件名”。你可以确认无误后再动手。
* **防覆盖保护：** 执行重命名前会检查目标文件名是否已经存在，如果存在则自动终止操作以防意外覆盖原文件。

### 使用说明
1. **选择文件夹：** 第一步点击“浏览...”按钮，选定你需要进行重命名操作的文件夹。
2. **设置规则：**
   * **文件后缀过滤 (可选)：** 输入你要处理的文件后缀（例如 `.pdf`）。如果不填，系统会尝试处理文件夹中的所有文件。
   * **分隔符：** 输入你要作为截断标准的字符（例如 `_` 或 `-`）。
3. **生成预览：** 点击“生成预览”按钮，下方表格会列出即将发生的重命名变化。
4. **执行重命名：** 检查表格中的新名字确认无误后，点击最下方绿色的 “⚡ 开始批量重命名” 按钮，完成真正的文件修改。

### 如何运行 (针对开发者)
1. 确保你的电脑上安装了 Python 3。
2. 克隆本代码库到本地。
3. 运行主程序：
   ```bash
   python batch_renamer.py
   ```
