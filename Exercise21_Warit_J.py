from tkinter import *
def leftClickButt(event):
    BMI = float(0)
    BMI = float(textBoxWeight.get())/((float(textBoxHeight.get())/100) ** 2)
    print("Height",textBoxHeight.get(), "Weight", textBoxWeight.get(),"BMI",BMI)
    if BMI >= 30.0:
        labelResult = Label(MainWindow, text="ผลลัพธ์: อ้วนมาก",fg='red').grid(row=2, column=1)
    elif BMI >= 25.0:
        labelResult = Label(MainWindow, text="ผลลัพธ์: อ้วน",fg='red').grid(row=2, column=1)
    elif BMI >= 23.0:
        labelResult = Label(MainWindow, text="ผลลัพธ์: น้ำหนักเกิน",fg='red').grid(row=2, column=1)
    elif BMI >= 18.6:
        labelResult = Label(MainWindow, text="ผลลัพธ์: น้ำหนักปกติ",fg='green').grid(row=2, column=1)
    else:
        labelResult = Label(MainWindow, text="ผลลัพธ์: ผอมเกินไป",fg='orange').grid(row=2, column=1)


MainWindow = Tk()
labelHeight = Label(MainWindow, text = "Height(cm)").grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow, text = "Weight(kg)").grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calcButton = Button(MainWindow,text="Calculate BMI")
calcButton.bind('<Button-1>',leftClickButt)
calcButton.grid(row=2, column=0)
MainWindow.mainloop()
