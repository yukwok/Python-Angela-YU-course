import tkinter

window = tkinter.Tk()
window.title('Billy first GUI app')
window.minsize(width=500, height=300)
print('hello world')


label = tkinter.Label(text='i am a label1,s sfsdf')

label.pack()


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64, )


window.mainloop()
