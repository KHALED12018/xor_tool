import itertools
import sys
import tkinter as tk
from tkinter import filedialog

class XORDecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("xor_decrypt_by_Dragon_Noire2023")

        self.file_label = tk.Label(root, text="File Path:")
        self.file_label.pack()

        self.file_path = tk.Entry(root)
        self.file_path.pack()

        self.open_button = tk.Button(root, text="Open File", command=self.open_file)
        self.open_button.pack()

        self.key_label = tk.Label(root, text="XOR Decryption Key (hex values):")
        self.key_label.pack()

        self.key_entry = tk.Entry(root)
        self.key_entry.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file_path)

    def decrypt_file(self):
        key_input = self.key_entry.get()
        key_values = bytes.fromhex(key_input)

        key = itertools.cycle(key_values)
        file_path = self.file_path.get()

        with open(file_path, 'rb') as f:
            fw = f.read()

        decrypted_data = bytearray()
        for i in range(0, len(fw)):
            decrypted_data.append(fw[i] ^ next(key))

        save_path = filedialog.asksaveasfilename(defaultextension=".decrypted", filetypes=[("Decrypted Files", "*.decrypted")])
        with open(save_path, 'wb') as f:
            f.write(decrypted_data)

        print("Decryption completed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = XORDecryptorApp(root)
    root.mainloop()
