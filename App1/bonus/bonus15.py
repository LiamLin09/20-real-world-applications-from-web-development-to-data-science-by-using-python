import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

button3 = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [button3]])

window.read()
window.close()
