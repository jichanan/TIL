import tkinter
import tkinter.font

window = tkinter.Tk()
window.title('단위변환')
def m2pyeong():
    m2 = entry1.get()
    entry2.delete("0","end")
    entry2.insert("0",round(float(m2)*0.3025,4))
def pyeongm2():
    pyeong = entry2.get()
    entry1.delete(0,"end")
    entry1.insert(0, round(float(pyeong)*3.305785,4))

label1 = tkinter.Label(window,text='제곱미터').grid(row=0, column=0)
label2 = tkinter.Label(window,text='평').grid(row=1,column=0)

entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

font = tkinter.font.Font(weight='bold',size = 10)

btn1 = tkinter.Button(window, font=font, text='제곱미터->평',bg='skyblue',fg='red',command=m2pyeong).grid(row=2,column=0)
btn2 = tkinter.Button(window, font=font, text='평->제곱미터',bg='skyblue',fg='red',command=pyeongm2).grid(row=2,column=1)

window.mainloop()