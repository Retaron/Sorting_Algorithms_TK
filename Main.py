import tkinter as tk
from tkinter import *
from tkinter import filedialog
import random
import time
global arraysize
arraysize = 1500
lines = ""
global arr
arr = []
global filename
filename = ""
global fileCondition
fileCondidion = False
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    filelabel.configure(text="File Opened: "+filename)
    fileA = open(filename,'r')
    global filepreviewstore
    filepreviewstore = fileA.read()
    #lines = fileA.readlines()
    lines = fileA.read()
    print(filepreviewstore)
    filepreviewstore = filepreviewstore.replace("\n", ",")
    FilePreview.insert(tk.END, filepreviewstore)
    randomButton["state"] = "normal"
    InsertionSort["state"] = "normal"
    MergeSort["state"] = "normal"
    BubbleSort["state"] = "normal"
    QuickSort["state"] = "normal"
    fileA.close()
    global arr
    arr = filepreviewstore.split(",",arraysize)
    for i in range(0, len(arr)):
        try:
            arr[i] = int(arr[i])
        except:
            arr[i] = arr[i]
            print("uhh, boss you might wanna look at this\nwhat?\ntheres a strig in the number file")
    print(filepreviewstore)
    print(len(arr))
    fileCondidion = True
    
def Randomise():
    fileB = open(filename, 'w')
    writecontent = []
    for i in range(0,arraysize,1):
        writecontent.append(str(random.randint(0,100)) + "\n")
    writecontent.append(str(random.randint(100,100000)))
    fileB.writelines(writecontent)
    fileB.close()
    print(writecontent)
    fileA = open(filename,'r')
    filepreviewstore2 = fileA.read()
    print(filepreviewstore2)
    filepreviewstore2 = filepreviewstore2.replace("\n", ",")
    #FilePreview.insert(tk.END, filepreviewstore2)
    FilePreview.delete(1.0,tk.END)
    FilePreview.insert(tk.END, filepreviewstore2)
    fileA.close()
def insertionSort():
    start = time.perf_counter()
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    end = time.perf_counter()
    timeElapsed = str(end-start)
    TimeMeter.delete(1.0,tk.END)
    TimeMeter.insert(tk.END, timeElapsed)
    writecontent = []
    for i in range(0,len(arr)-2,1):
        writecontent.append(str(arr[i]) + "\n")
    writecontent.append(str(arr[len(arr)-1]))
    fileB = open(filename, 'w')
    fileB.writelines(writecontent)
    fileB.close()
    fileA = open(filename,'r')
    filepreviewstore2 = fileA.read()
    filepreviewstore2 = filepreviewstore2.replace("\n", ",")
    FilePreview.delete(1.0,tk.END)
    FilePreview.insert(tk.END, filepreviewstore2)
    fileA.close()
def mergeSortContainer():
    start = time.perf_counter()
    def mergeSort(Array):
        if len(Array)>1:
            mid = len(Array)//2
            lefthalf = Array[:mid]
            righthalf = Array[mid:]
            mergeSort(lefthalf)
            mergeSort(righthalf)
            i=j=k=0       
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    Array[k]=lefthalf[i]
                    i=i+1
                else:
                    Array[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                Array[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                Array[k]=righthalf[j]
                j=j+1
                k=k+1
    end = time.perf_counter()
    timeElapsed = str(end-start)
    TimeMeter.delete(1.0,tk.END)
    TimeMeter.insert(tk.END, timeElapsed)
    writecontent = []
    for i in range(0,len(arr)-2,1):
        writecontent.append(str(arr[i]) + "\n")
    writecontent.append(str(arr[len(arr)-1]))
    fileB = open(filename, 'w')
    fileB.writelines(writecontent)
    fileB.close()
    fileA = open(filename,'r')
    filepreviewstore2 = fileA.read()
    filepreviewstore2 = filepreviewstore2.replace("\n", ",")
    FilePreview.delete(1.0,tk.END)
    FilePreview.insert(tk.END, filepreviewstore2)
    fileA.close()
def bubble_sort():
    start = time.perf_counter()
    # We go through the list as many times as there are elements
    for i in range(len(arr)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end = time.perf_counter()
    timeElapsed = str(end-start)
    TimeMeter.delete(1.0,tk.END)
    TimeMeter.insert(tk.END, timeElapsed)
    writecontent = []
    for i in range(0,len(arr)-2,1):
        writecontent.append(str(arr[i]) + "\n")
    writecontent.append(str(arr[len(arr)-1]))
    fileB = open(filename, 'w')
    fileB.writelines(writecontent)
    fileB.close()
    fileA = open(filename,'r')
    filepreviewstore2 = fileA.read()
    filepreviewstore2 = filepreviewstore2.replace("\n", ",")
    FilePreview.delete(1.0,tk.END)
    FilePreview.insert(tk.END, filepreviewstore2)
    fileA.close()
def QuickSortContainer():
    def sort(array=[12,4,5,6,7,3,1,15]):
        """Sort the array by using quicksort."""

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            # Don't forget to return something!
            return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array
    start = time.perf_counter()
    sort(arr)
    end = time.perf_counter()
    timeElapsed = str(end-start)
    TimeMeter.delete(1.0,tk.END)
    TimeMeter.insert(tk.END, timeElapsed)
    writecontent = []
    for i in range(0,len(arr)-2,1):
        writecontent.append(str(arr[i]) + "\n")
    writecontent.append(str(arr[len(arr)-1]))
    fileB = open(filename, 'w')
    fileB.writelines(writecontent)
    fileB.close()
    fileA = open(filename,'r')
    filepreviewstore2 = fileA.read()
    filepreviewstore2 = filepreviewstore2.replace("\n", ",")
    FilePreview.delete(1.0,tk.END)
    FilePreview.insert(tk.END, filepreviewstore2)
    fileA.close()
    print("done file stuff")
##def TimeMeter(timeelapsed, tk):
def NewFileFunc():
    NewFileFuncFilename = NewFileText.get(1.0,tk.END)
    print(NewFileFuncFilename)
    NewFileFuncFilename = NewFileFuncFilename.replace("\n","") + ".txt"
    fileA = open(NewFileFuncFilename, "x")
    NewFileText.delete(1.0,tk.END)
    NewFileText.insert(tk.END, "file create")
    fileA.close()
##################TEST AREA##################
def argless():
    def argser(numb):
        numb = numb+1
        return numb
    print(argser(5))

    
##################TEST AREA##################   
man = tk.Tk()
man.title('Counting Seconds')
button = tk.Button(man, text='Stop', width=15, height=1, command=man.destroy)
enter = tk.Button(man, text = 'Enter', width=12, height=10,command = browseFiles)
#browse = tk.Button(man, text = 'browse', width=15, height=10,command=man.)
filelabel = tk.Label(man, text = "File explorer", width = 40, height=4, fg="blue")
filelabel.grid(row = 0, column = 1, sticky = W, columnspan = 5)
#file preview text box
FilePreview = tk.Text(man, height=3, width=40)
#FilePreview.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 2, columnspan = 5)
FilePreview.grid(row = 1, column = 1, columnspan = 5)
canv = Canvas(man)
#enter file button
enter.grid(row = 0, column = 7, padx = 2, rowspan = 3)
#stop button
button.grid(row = 4, column = 7, sticky = W)
#random button
randomButton = tk.Button(man, text='Randomise', width = 10, height = 2, command = Randomise)
randomButton["state"] = DISABLED
randomButton.grid(row = 2, column = 0)
### New File Button###
NewFile = tk.Button(man, text='New File', width = 10, height = 2, command=NewFileFunc)
NewFile.grid(row = 1,column = 0)
## file name create insert text ##
NewFileText = tk.Text(man, height = 1 , width = 10)
NewFileText.grid(row = 0, column = 0)
NewFileText.insert(tk.END,"File Name")
#insertion sort button
InsertionSort = tk.Button(man, text='Insertion Sort', width = 10, height = 2, command = insertionSort)
InsertionSort.grid(row = 4 , column = 1)
InsertionSort["state"] = DISABLED
#time elaspsed
TimeMeter = tk.Text(man, height=1, width=20, fg="blue")
TimeMeter.grid(row = 6, column = 1, columnspan = 2)
TimeMeter.insert(tk.END, "Time for algorithm")
#Merge sort
MergeSort = tk.Button(man, text='Merge Sort', width = 10, height = 2, command = mergeSortContainer)
MergeSort.grid(row = 4, column = 2)
MergeSort["state"] = DISABLED
#Bubble sort
BubbleSort = tk.Button(man, text='Bubble Sort', width = 10, height = 2, command = bubble_sort)
BubbleSort.grid(row = 4 , column = 3 , pady = 5, padx = 5)
BubbleSort["state"] = DISABLED
#Quick sort
QuickSort = tk.Button(man, text='Quick sort', width = 10, height = 2, command = QuickSortContainer)
QuickSort.grid(row = 5 , column = 1 , pady = 5,)
QuickSort["state"] = DISABLED
#canvas_height=300
#canvas_width=400
#y = int(canvas_height/2)
#canv.create_line(0, y, canvas_width, y )

argless()
man.mainloop()

