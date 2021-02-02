try:
    import tkinter as tk
    import cmath as cm
except ImportError:
    import Tkinter as tk

def resistance(r1=0, x1=0, r2=0, x2=0):
    try:
        return (complex(r1, x1)*complex(r2, x2))/(complex(r1, x1)+complex(r2,x2))
    except TypeError:
        (r1, x1, r2, x2) = (int(r1), int(x1), int(r2), int(x2))
        return (complex(r1, x1)*complex(r2, x2))/(complex(r1, x1)+complex(r2,x2))


def getNR():
    try:
        res = resistance(int(r1.get()), int(x1.get()), int(r2.get()), int(x2.get()))
        print(res)
        polar = cm.polar(res)
        tk.Label(root, text=f'Z = {round(res.real, 2)}+{round(res.imag, 2)}').grid(row=4, column=1)
        tk.Label(root, text=f'Z = {round(polar[0], 2)}*e^({round(polar[1], 2)}j)').grid(row=5, column=1)

    except TypeError:
        print('ERRUR ERRUERUERE')
        pass

def enter(*kargs):
    getNR()

root = tk.Tk()
root.title('Impedence Combinations')
frame = tk.Frame(root)
frame.grid(row=0, column=0)

rInfoLab = tk.Label(root, text='R') #Creation des labels utiles au programme
xInfoLab = tk.Label(root, text='X')
z1Lab = tk.Label(root, text='Z1')
z2Lab = tk.Label(root, text='Z2')

r1 = tk.Entry(root) # Creation des boites entry
r1.insert(0, '0')

x1 = tk.Entry(root)
x1.insert(0, '0')

r2 = tk.Entry(root)
r2.insert(0, '0')

x2 = tk.Entry(root)
x2.insert(0, '0')

r1.bind('<Return>', enter)
x1.bind('<Return>', enter)
r2.bind('<Return>', enter)
x2.bind('<Return>', enter)

rInfoLab.grid(row=0, column=1) #placement des labels 'info'
xInfoLab.grid(row=0, column=2)
z1Lab.grid(row=1, column=0) #placement des labels z1 et z2
z2Lab.grid(row=2, column=0)

r1.grid(row=1, column=1) #placement des entry box de r1, z1, r2, z2
x1.grid(row=1, column=2)
r2.grid(row=2, column=1)
x2.grid(row=2, column=2)

okButton = tk.Button(root, text='Ok', command=getNR)
okButton.bind('<Return>', enter)
okButton.grid(row=4, column=0)

root.mainloop()