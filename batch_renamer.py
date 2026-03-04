import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class BatchRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文件批量重命名工具 (Batch Renamer)")
        self.root.geometry("700x600")
        self.root.resizable(True, True)

        self.directory_path = tk.StringVar()
        self.target_extension = tk.StringVar(value=".pdf")
        self.separator_char = tk.StringVar(value="_")
        self.files_to_rename = [] # Store tuples of (old_name, new_name)

        self.create_widgets()

    def create_widgets(self):
        # 1. 文件夹选择区
        frame_dir = tk.LabelFrame(self.root, text="第一步: 选择文件夹", padx=10, pady=10)
        frame_dir.pack(fill="x", padx=10, pady=5)

        tk.Entry(frame_dir, textvariable=self.directory_path, state='readonly', width=50).pack(side="left", padx=(0, 10))
        tk.Button(frame_dir, text="浏览...", command=self.browse_directory).pack(side="left")

        # 2. 规则设置区
        frame_rules = tk.LabelFrame(self.root, text="第二步: 设置重命名规则", padx=10, pady=10)
        frame_rules.pack(fill="x", padx=10, pady=5)

        # 过滤后缀
        tk.Label(frame_rules, text="只处理以下后缀的文件:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame_rules, textvariable=self.target_extension, width=15).grid(row=0, column=1, sticky="w", padx=5)
        tk.Label(frame_rules, text="(例如: .pdf 或 .csv，如果留空则处理所有文件)").grid(row=0, column=2, sticky="w")

        # 分隔符设置
        tk.Label(frame_rules, text="删除目标字符之前的所有内容:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame_rules, textvariable=self.separator_char, width=15).grid(row=1, column=1, sticky="w", padx=5)
        tk.Label(frame_rules, text="(例如输入 '_' 则保留 '_' 后面的内容)").grid(row=1, column=2, sticky="w")
        
        tk.Button(frame_rules, text="生成预览", command=self.generate_preview, bg="#e0e0e0").grid(row=2, column=0, columnspan=3, pady=10)

        # 4. 执行按钮 - 先 Pack 到底部，确保不会被多余的 Treeview 挤压掉
        frame_action = tk.Frame(self.root)
        frame_action.pack(side="bottom", fill="x", padx=10, pady=10)
        tk.Button(frame_action, text="⚡ 开始批量重命名", command=self.execute_rename, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(side="right")

        # 3. 预览区 - 最后 Pack，并设置 expand=True 占据剩下的所有空间
        frame_preview = tk.LabelFrame(self.root, text="第三步: 预览结果", padx=10, pady=10)
        frame_preview.pack(fill="both", expand=True, padx=10, pady=5)

        # Treeview (Table) for preview
        columns = ('old', 'new')
        self.tree = ttk.Treeview(frame_preview, columns=columns, show='headings')
        self.tree.heading('old', text='原文件名')
        self.tree.heading('new', text='新文件名')
        self.tree.column('old', width=280)
        self.tree.column('new', width=280)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame_preview, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def browse_directory(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.directory_path.set(folder_selected)
            self.tree.delete(*self.tree.get_children()) # Clear previous previews
            self.files_to_rename = []

    def generate_preview(self):
        self.tree.delete(*self.tree.get_children())
        self.files_to_rename = []
        
        directory = self.directory_path.get()
        if not directory:
            messagebox.showwarning("提示", "请先选择一个文件夹！")
            return
            
        target_ext = self.target_extension.get().strip().lower()
        if target_ext and not target_ext.startswith("."):
            target_ext = f".{target_ext}"
            
        sep_char = self.separator_char.get()
        
        if not sep_char:
             messagebox.showwarning("提示", "请输入作为分隔符的字符！")
             return

        try:
            for filename in os.listdir(directory):
                # Check extension filter
                if target_ext and not filename.lower().endswith(target_ext):
                    continue
                    
                # Skip directories
                if os.path.isdir(os.path.join(directory, filename)):
                    continue

                # Apply renaming logic: Find separator and keep everything after it
                name_parts = filename.split(sep_char, 1)
                
                if len(name_parts) > 1:
                    new_filename = name_parts[1]
                    self.files_to_rename.append((filename, new_filename))
                    self.tree.insert('', tk.END, values=(filename, new_filename))
                    
            if not self.files_to_rename:
                messagebox.showinfo("预览", "在该文件夹下没有找到符合规则可以重命名的文件。")
                
        except Exception as e:
            messagebox.showerror("错误", f"读取文件夹时发生错误:\n{str(e)}")

    def execute_rename(self):
        if not self.files_to_rename:
            messagebox.showwarning("提示", "没有需要重命名的文件。请先点击生成预览。")
            return
            
        directory = self.directory_path.get()
        
        # Confirmation dialog
        confirm = messagebox.askyesno("确认", f"即将重命名 {len(self.files_to_rename)} 个文件。\n此操作不可逆转，确定要继续吗?")
        if not confirm:
            return

        success_count = 0
        error_count = 0
        
        for old_name, new_name in self.files_to_rename:
            old_path = os.path.join(directory, old_name)
            new_path = os.path.join(directory, new_name)
            
            # Check if target file already exists to prevent accidental overwrite
            if os.path.exists(new_path) and old_path.lower() != new_path.lower():
                messagebox.showerror("冲突", f"重命名失败: 目标文件已存在!\n{new_name}\n为防止覆盖，操作已停止。")
                self.generate_preview() # Refresh
                return
                
            try:
                os.rename(old_path, new_path)
                success_count += 1
            except Exception as e:
                print(f"Failed to rename {old_name}: {e}")
                error_count += 1
                
        messagebox.showinfo("完成", f"重命名完成！\n成功: {success_count} 个文件\n失败: {error_count} 个")
        self.generate_preview() # Refresh the list

if __name__ == "__main__":
    root = tk.Tk()
    app = BatchRenamerApp(root)
    root.mainloop()
