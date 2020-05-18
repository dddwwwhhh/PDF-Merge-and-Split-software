from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog, Text
import os
input_path="/"
file_list = []
out_path ="merge.pdf"
split_message=[]
save_path=''
def addfile():
    global input_path
    
    destroy_message()
    filename = filedialog.askopenfilename(initialdir=input_path,title="Select File",filetypes=(("PDF","*.pdf"),("all files","*.*")))
    if filename == '':
        pass
    else:
        #store current path for next time adding files.
        current_path = os.path.dirname(filename)
        input_path = current_path
        #adding file path to the list
        file_list.append(filename)

    for pdf_path in file_list:
        message(pdf_path,bg='gray')
#get saving path for split        
def get_save_path():
    global save_path
    save_path = tk.filedialog.askdirectory(initialdir=input_path,title="Save File Path For Split")
    destroy_message()
    message('Saving path for split files: {}'.format(save_path))
    
#clean all list and message
def clean_all():
    global file_list
    global split_message
    file_list=[]
    split_message=[]
    for widget in frame.winfo_children():
        widget.destroy()
        
#clean all list but keep message in display
def clean_list():
    global file_list
    global split_message
    file_list=[]
    split_message=[]

#quit the program
def quit_def():
    root.destroy()

#user input for output file path and file name.
def out_path_def():
    global out_path
    out_path = filedialog.asksaveasfilename(initialdir="/Users/Cheng",title="Save File",filetypes=(("PDF","*.pdf"),("all files","*.*")),defaultextension=".pdf")
    
#remove message the window 
def destroy_message():
    for widget in frame.winfo_children():
        widget.destroy()

#display message
def message(message,fg='white',bg='black'):
    label = tk.Label(master=frame,text=message,fg=fg,bg=bg)
    label.pack()

    
#merge PDF files    
def merge_pdfs(paths,output_path):
    
    if paths==[]:
        
        destroy_message()
        message('Please add files','black', 'red')
        clean_list()
    else:
        try:

            #if the output file path empty, using default file path
            if output_path=="merge.pdf":
                output_path=os.path.abspath(os.getcwd())+"\\"+"merge.pdf"


            pdf_writer = PdfFileWriter()

            for path in paths:
                pdf_reader = PdfFileReader(path, strict=False)
                for page in range(pdf_reader.getNumPages()):
                    # Add each page to the writer object
                    pdf_writer.addPage(pdf_reader.getPage(page))

            # Write out the merged PDF
            try:
                with open(output_path, 'wb') as out:
                    pdf_writer.write(out)
                #display output file paths  
                destroy_message()
                message('Merged.\nFile name or path: {}'.format(output_path),fg='white',bg="black")
                clean_list()

            except:
                destroy_message()
                message('Please check {} is occupied'.format(output_path),fg='black',bg="red")
                clean_list()

        except:
            destroy_message()
            message('Error, Please make sure input PDF files are correct and unencrypted.',fg='black',bg="red")
            clean_list()
                    
#split all PDFs to single page PDF file                    
def split(input_files, output_path):
    try:
        #if not input file, display message
        if len(input_files)==0:
            destroy_message()
            label = tk.Label(master=frame,text='Plaese add file for split',bg="red")
            label.pack()
        else:

            
            #if the output file path empty, using default file path
            if output_path=='':
                output_path=os.path.abspath(os.getcwd())+"\\"



            for each_pdf_file in input_files:
                pdf = PdfFileReader(each_pdf_file, strict=False)
                file_name = os.path.basename(each_pdf_file)
                    
                if file_name[-4:]==".pdf":
                    file_name=file_name[:-4]
                    
                for page in range(pdf.getNumPages()):
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf.getPage(page))
                    output = f'{output_path}{file_name}{page}.pdf'
                    with open(output, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                    split_message.append(output)
                    
            destroy_message()
            for each_split_message in split_message:
                message('{}'.format(each_split_message),fg='white',bg="black")
            
        clean_list()
            
    except:
        destroy_message()
        message('{}'.format(each_split_message),fg='white',bg="black")
        clean_list()
        
def help():
    destroy_message()
    message('Add--add PDF files for merge or split\nClean--clean all added files\nMerge--merge all PDF files to single one, if file path is not defined, it uses default path.\nSave as--set output file locaiton for merged file\nSplit--split all PDF file to single page PDF files\nSave path--the path for split files','black','white')

root = tk.Tk()
root.title("PDF Merge and Split")
root.minsize(800, 700)
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack(fill=tk.BOTH,  expand=True)



frame = tk.Frame(canvas, bg="white")
frame.pack(fill=tk.BOTH,expand=1, padx=60,pady=60)
canvas1 = tk.Canvas(root, height=100, width=700, bg="white")
canvas1.pack(fill=tk.X)


add =tk.Button(canvas1,text='Add',padx=10,pady=5,fg="white",bg="#263D42",command=lambda:addfile(),borderwidth=2)
add.pack(side=tk.LEFT)
clean =tk.Button(canvas1,text='Clean',padx=10,pady=5,fg="white",bg="#263D42",command=clean_all,borderwidth=2)
clean.pack(side=tk.LEFT)

merge =tk.Button(canvas1,text='Merge',padx=10,pady=5,fg="white",bg="#263D42",command=lambda:merge_pdfs(file_list,out_path),borderwidth=2)
merge.pack(side=tk.LEFT,padx=(80,0))

out_path_btn =tk.Button(canvas1,text='Save as',padx=10,pady=5,fg="white",bg="#263D42",command=out_path_def,borderwidth=2)
out_path_btn.pack(side=tk.LEFT)

split_btn =tk.Button(canvas1,text='Split',padx=10,pady=5,fg="white",bg="#263D42",command=lambda:split(file_list,save_path),borderwidth=2)
split_btn.pack(side=tk.LEFT,padx=(80,0))
save_path_btn =tk.Button(canvas1,text='Save path',padx=10,pady=5,fg="white",bg="#263D42",command=get_save_path,borderwidth=2)
save_path_btn.pack(side=tk.LEFT)

quit =tk.Button(canvas1,text='Quit',padx=10,pady=5,fg="white",bg="#263D42",command=quit_def,borderwidth=2)
quit.pack(side=tk.RIGHT)
help()

root.mainloop()