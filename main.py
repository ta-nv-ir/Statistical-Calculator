import PySimpleGUI as sg
import pandas as pd
import tkinter
import csv

sg.theme('DarkAmber')
layout = [  [sg.Text('The name or directory of your csv file:'), sg.InputText()],
            [sg.Text('Name of the column we are working on: '), sg.InputText()],
            [sg.Button('Enter Data')],[sg.Button('Display Data')],
            [sg.Button('Mean'), sg.Button('Median'), sg.Button('Varience'), sg.Button('Co-varience')],
            [sg.Button('Exit')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    a=values[0]
    z=pd.read_csv(a)
    b=values[1]
    if event == 'Display Data':
       root = tkinter.Tk()
       # open file
       with open((str(a)), newline="") as file:
          reader = csv.reader(file)
          # set window size
          root.geometry("500x500")
          # r and c tell us where to grid the labels
          r = 0
          for col in reader:
             c = 0
             for row in col:
                # i've added some styling
                label = tkinter.Label(root, width=20, height=2, \
                                      text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
             r += 1
       root.mainloop()
    if event == 'Mean':
       print (z[b].mean()) #getting mean from a column
    elif event == 'Median':
       print (z[b].median()) #getting median from a column
    elif event == 'Varience':
       print (z[b].var()) #getting Variance from a column
    elif event == 'Co-varience':
       y = input('Please enter the name of the column to get co-variance with: ')
       print(z[b].cov(z[y]))  # getting covariance from a column
    elif event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break


window.close()



















































