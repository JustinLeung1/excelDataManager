import tkinter as tk
import tkinter.filedialog as fd
import os
import csv

foldernames = {"folder_1": ""}


root = tk.Tk()
root.title("CSV Data Manager")
root.geometry("700x100")


def folder_window():
    foldernames["folder_1"] = fd.askdirectory()
    folder_label.config(text=foldernames["folder_1"])


def create_csv():
    if foldernames["folder_1"] == "":
        return
    file_list = ["n/a"] * 100
    file_directory = os.listdir(foldernames["folder_1"])
    for file in file_directory:
        lot = file.split("_Part_")
        if len(lot) > 1:
            number = int(lot[1].split('.')[0])
            file_list[number - 1] = file
    new_csv = []
    for file in file_list:
        if file == "n/a":
            content = [''] * 52
            new_csv.append(content)
            continue
        with open(foldernames["folder_1"] + '/' + file, 'r') as csv_read:
            reader = csv.reader(csv_read, delimiter=',')
            i = 0
            content = []
            for row in reader:
                i += 1
                if i >= 13:
                    content.append(row[0])
        new_csv.append(content)

    transpose_csv = [[new_csv[j][i] for j in range(len(new_csv))] for i in range(len(new_csv[0]))]
    with open(foldernames["folder_1"] + '/' + "log.csv", 'w', newline='') as csv_write:
        writer = csv.writer(csv_write)
        for row in transpose_csv:
            writer.writerow(row)


folder_button = tk.Button(root, text="Choose a folder", command=folder_window, font="arial 14", width="15")
folder_button.grid(row=1, column=1, pady=5)

create_csv_button = tk.Button(root, text="Create a CSV", command=create_csv, font="arial 14", width="15")
create_csv_button.grid(row=2, column=1)

folder_label = tk.Label(root, bg="white", width="60", height='2', relief="sunken")
folder_label.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
