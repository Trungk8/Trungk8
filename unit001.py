"""Ứng dụng Tkinter đơn giản để thu thập dữ liệu người dùng.

Hướng dẫn sử dụng:
    python unit001.py
"""

import logging
import tkinter as tk
from tkinter import ttk


logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


def on_submit(name: str, email: str) -> None:
    """Xử lý dữ liệu từ form và log kết quả."""
    logging.info("Nhận dữ liệu: name=%s, email=%s", name, email)


def handle_submit(name_entry: ttk.Entry, email_entry: ttk.Entry) -> None:
    """Callback cho nút gửi, lấy dữ liệu và truyền cho on_submit."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    on_submit(name, email)


def create_form(root: tk.Tk) -> None:
    """Tạo giao diện form với các trường nhập liệu và nút gửi."""
    root.title("Thông tin người dùng")

    mainframe = ttk.Frame(root, padding="20 20 20 20")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    ttk.Label(mainframe, text="Họ và tên").grid(column=0, row=0, sticky=tk.W)
    name_entry = ttk.Entry(mainframe, width=30)
    name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Email").grid(column=0, row=1, sticky=tk.W)
    email_entry = ttk.Entry(mainframe, width=30)
    email_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

    submit_button = ttk.Button(
        mainframe,
        text="Gửi",
        command=lambda: handle_submit(name_entry, email_entry),
    )
    submit_button.grid(column=0, row=2, columnspan=2, pady=10)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    name_entry.focus()


def main() -> None:
    """Khởi tạo và chạy vòng lặp Tkinter."""
    root = tk.Tk()
    create_form(root)
    root.mainloop()


if __name__ == "__main__":
    main()
