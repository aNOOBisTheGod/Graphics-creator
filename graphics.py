from tkinter import *    
a = Tk()
a.geometry('1920x1080')
a['bg'] = 'black'
c = Canvas(a, width = 9000, height = 900, bg = 'black')
c.pack()
savex = 0
savey = 0
m = 0
for i in range(100):
    m += 40
    c.create_line(m, 0, m, 20, width = 2, fill = 'white')
m = 0
for i in range(100):
    m += 40
    c.create_line(0, m, 20, m, width = 2, fill = 'white')


def create_line():
    global savex, savey
    pointx = x.get()
    pointy = y.get()
    pointx = int(pointx) * 40
    pointy = int(pointy) * 40
    global n
    n = c.create_line(savex, savey, pointx, pointy, width = 2, fill = 'white')
    savex = pointx
    savey = pointy

def del_last():
    c.delete(n)

    
def clear_all():
    m = 0
    c.delete('all')
    for i in range(100):
        m += 40
        c.create_line(m, 0, m, 20, width = 2, fill = 'white')
    m = 0
    for i in range(100):
        m += 40
        c.create_line(0, m, 20, m, width = 2, fill = 'white')
    m = 0

    
btn = Button(text='создать линию', background='#000', foreground='#0c0',
             padx='20', pady='8', font='16', highlightcolor = '#0cc', command=create_line)
btn_clearall = Button(text='удалить все', background='#000', foreground='#0c0',
             padx='20', pady='8', font='16', highlightcolor = '#0cc', command=clear_all)
btn_clear = Button(text='удалить последнюю линию', background='#000', foreground='#c00',
             padx='20', pady='8', font='16', highlightcolor = '#c0c', command=del_last)
btn_clearall.place(x = 100 ,y =  930, height = 70, width = 200)
btn_clear.pack()
btn.pack()
x = Entry(a)
x.place(x = 750 ,y =  920, height = 20, width = 50)
y = Entry(a)
y.place(x = 750 ,y =  950, height = 20, width = 50)
a.mainloop()
 
