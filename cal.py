import csv
import pandas as pd
import tkinter as tk
import tkinter.messagebox
from tkinter import *
from csv import reader
from sys import exit
from math import sqrt
from operator import itemgetter
#global month
#global data
global s
global r
r=0
s=20

def fun1():

    def sam1():

        #global month
        #global data



        def JAN():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            #print("PACKING METERIAL  PRIDICTION")
            with open('JAN.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            #print("l1:", listx)
            #print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            #print("l1:", listx)
            #print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            #print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            #print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            #print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            #print(q)
            w1 = p / q
            #print("w1:", w1)
            w0 = ya - (w1 * xa)
            #print("w0:", w0)

            def eq(g):
                s= w0 + (w1 * g)

                return s


            r = eq(data.get())
            res=0
            #print(data.get())
            if r>data.get():
                res=r-data.get()
                label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
            else:
                res=data.get()-r
                label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10,  y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)




        def FEB():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('FEB.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)


                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def MAR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('MAR.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)


        def APR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('APR.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def MAY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('MAY.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def JUNE():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('JUNE.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def JULY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('JULY.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def AUG():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('AUG.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def SEP():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('SEP.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",
                                   font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),
                                   fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def OCT():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            #print("PACKING METERIAL  PRIDICTION")
            with open('OCT.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            #print("l1:", listx)
            #print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            #print("l1:", listx)
            #print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            #print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            #print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            #print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            #print(q)
            w1 = p / q
            #print("w1:", w1)
            w0 = ya - (w1 * xa)
            #print("w0:", w0)

            def eq(g):
                s = w0 + (w1 * g)

                return s

            r = eq(data.get())
            res = 0
            # print(data.get())
            if r > data.get():
                res = r - data.get()
                label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
            else:

                res = data.get() - r
                label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def NOV():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                #print("PACKING METERIAL  PRIDICTION")
                with open('NOV.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:", listx)
                #print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:", listx)
                #print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                #print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                #print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                #print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                #print(q)
                w1 = p / q
                #print("w1:", w1)
                w0 = ya - (w1 * xa)
                #print("w0:", w0)

                def eq(g):
                    s = w0 + (w1 * g)

                    return s

                r = eq(data.get())
                res = 0
                # print(data.get())
                if r > data.get():
                    res = r - data.get()
                    label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"),fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
                else:

                    res = data.get() - r
                    label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                    label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                    label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                    label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
        def DEC():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            #print("PACKING METERIAL  PRIDICTION")
            with open('DEC.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            #print("l1:", listx)
            #print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            #print("l1:", listx)
            #print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            #print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            #print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            #print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            #print(q)
            w1 = p / q
            #print("w1:", w1)
            w0 = ya - (w1 * xa)
            #print("w0:", w0)

            def eq(g):
                s = w0 + (w1 * g)

                return s

            r = eq(data.get())
            res = 0
            # print(data.get())
            if r > data.get():
                res = r - data.get()
                label3 = Label(root, text="THE PREDICTED VALUE IS GREATER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO INCREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)
            else:

                res = data.get() - r
                label3 = Label(root, text="THE PREDICTED VALUE IS LESSER THAN YOUR REQUIRED VALUE:",font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=470)
                label3 = Label(root, text=r, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=520)
                label3 = Label(root, text="YOU HAVE TO DECREASE PACKING MATERIAL", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=550)
                label3 = Label(root, text=res, font=("arial", 18, "bold"), fg="GREEN").place(x=10, y=600)


        def default():

            label3 = Label(root, text="wrong data ", font=("arial", 28, "bold"), fg="RED").place(x=10, y=550)
            return "Wrong data"
        switcher = {
            1:JAN,
            2:FEB,
            3:MAR,
            4:APR,
            5:MAY,
            6:JUNE,
            7:JULY,
            8:AUG,
            9:SEP,
            10:OCT,
            11:NOV,
            12:DEC,

        }
        def switch(operation):
            return switcher.get(operation, default)()


        #print(month.get())
        print (switch(month.get()))
        #print(month.get())


    root = Tk()
    #root["bg"] = "red"
    root.geometry("1366x768")
    #root["bg"] = "black"
    #root.configure(bg="red")
    #background_image = tk.PhotoImage(file='Coats.png')
    #background_label = tk.Label(root, image=background_image)
    #background_label.place(relwidth=1, relheight=1)
    root.title("PACKING MATERIAL")
    heading = Label(root, text="MADURA COATS PRIVATE LIMITED ", font=("arial", 40, "bold"), fg="RED").pack()
    heading = Label(root, text="PACKING MATERIAL PREDICTION", font=("arial", 30, "bold"), fg="BLUE").pack()
    label1 = Label(root, text="ENTER THE MONTH: ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=200)
    label2 = Label(root, text="ENTER PACKING MATERIAL: ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=250)

    month = IntVar(root)
    data = IntVar(root)


    entry_box = Entry(root, textvariable=month, width=30, bg="white").place(x=280, y=210)
    entry_box = Entry(root, textvariable=data, width=30, bg="white").place(x=350, y=260)

    check = Button(root, text="PREDICT", width=10, height=2, bg="lightblue", command=sam1).place(x=250, y=300)

    #photo = PhotoImage(file = "Coats.png")
    #w = Label(root, image=photo)
    #w.pack()
    #ent = Entry(root)
    #ent.pack()
    #ent.focus_set()
    root.mainloop()

    
    
def fun2():
    def sam():
        def load_data_set(filename):
            try:
                with open(filename, newline='') as iris:
                    return list(reader(iris, delimiter=','))
            except FileNotFoundError as e:
                raise e


        def convert_to_float(data_set, mode):
            new_set = []
            try:
                if mode == 'training':
                    for data in data_set:
                        new_set.append([float(x) for x in data[:len(data)-1]] + [data[len(data)-1]])

                elif mode == 'test':
                    for data in data_set:
                        new_set.append([float(x) for x in data])

                else:
                    print('Invalid mode, program will exit.')
                    exit()

                return new_set

            except ValueError as v:
                print(v)
                print('Invalid data set format, program will exit.')
                exit()


        def get_classes(training_set):
            return list(set([c[-1] for c in training_set]))


        def find_neighbors(distances, k):
            return distances[0:k]


        def find_response(neighbors, classes):
            votes = [0] * len(classes)

            for instance in neighbors:
                for ctr, c in enumerate(classes):
                    if instance[-2] == c:
                        votes[ctr] += 1

            return max(enumerate(votes), key=itemgetter(1))


        def knn(training_set, test_set, k):
            distances = []
            dist = 0
            limit = len(training_set[0]) - 1

            # generate response classes from training data
            classes = get_classes(training_set)

            try:
                for test_instance in test_set:
                    for row in training_set:
                        for x, y in zip(row[:limit], test_instance):
                            dist += (x-y) * (x-y)
                        distances.append(row + [sqrt(dist)])
                        dist = 0

                    distances.sort(key=itemgetter(len(distances[0])-1))

                    # find k nearest neighbors
                    neighbors = find_neighbors(distances, k)

                    # get the class with maximum votes
                    index, value = find_response(neighbors, classes)

                    # Display prediction
                    #label1 = Label(root, text="DELAY PREDICTION ", font=("arial", 18, "bold"), fg="YELLOW").place(x=10, y=200)
                    label1 = Label(root, text='The predicted class for sample ' + str(test_instance) + ' is : ' + classes[index], font=("arial", 18, "bold"), fg="YELLOW").place(x=50, y=500)
                    print('The predicted class for sample ' + str(test_instance) + ' is : ' + classes[index])
                    print('Number of votes : ' + str(value) + ' out of ' + str(k))

                    # empty the distance list
                    distances.clear()

            except Exception as e:
                print(e)


        def main():
            try:
                # get value of k
                k = 3
                #int(input('Enter the value of k : '))

                # load the training and test data set
                training_file = 'delay-dataset.csv'
                test_file = 'delay-test.csv'
                training_set = convert_to_float(load_data_set(training_file), 'training')
                test_set = convert_to_float(load_data_set(test_file), 'test')

                if not training_set:
                    print('Empty training set')

                elif not test_set:
                    print('Empty test set')

                elif k > len(training_set):
                    print('Expected number of neighbors is higher than number of training data instances')

                else:
                    knn(training_set, test_set, k)

            except ValueError as v:
                print(v)

            except FileNotFoundError:
                print('File not found')


        if __name__ == '__main__':
            main()

    root = Tk()
    #root["bg"] = "red"
    root.geometry("1366x768")
    #root["bg"] = "black"
    #root.configure(bg="red")
    #background_image = tk.PhotoImage(file='Coats.png')
    #background_label = tk.Label(root, image=background_image)
    #background_label.place(relwidth=1, relheight=1)

    root.title("DELAY PREDICTION")
    heading = Label(root, text="MADURA COATS PRIVATE LIMITED ", font=("arial", 40, "bold"), fg="RED").pack()
    heading = Label(root, text="DELAY PREDICTION", font=("arial", 30, "bold"), fg="BLUE").pack()

    check = Button(root, text="PREDICT", width=10, height=2, bg="lightblue", command=sam).place(x=250, y=300)
    root.mainloop()


def fun3():
    def sam():



        def JAN():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("PRIORITY ORDER  PREDICTION")
            with open('1.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h

            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)

        def FEB():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PREORITY ORDER  PREDICTION")
                with open('2.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h
                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def MAR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('3.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def APR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('4.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def MAY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('5.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def JUNE():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('6.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def JULY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER PREDICTION")
                with open('7.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def AUG():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('8.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def SEP():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('9.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def OCT():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("PRIORITY ORDER  PREDICTION")
            with open('10.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def NOV():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("PRIORITY ORDER  PREDICTION")
                with open('11.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)
        def DEC():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("PRIORITY ORDER PREDICTION")
            with open('12.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF PREORITY ORDER PREDICTED TO ARRIVE THIS MONTH:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def default():
          return "Incorrect day"
        switcher = {
            1:JAN,
            2:FEB,
            3:MAR,
            4:APR,
            5:MAY,
            6:JUNE,
            7:JULY,
            8:AUG,
            9:SEP,
            10:OCT,
            11:NOV,
            12:DEC,

        }
        def switch(operation):
          return switcher.get(operation, default)()

        print (switch(month.get()))
    


    root = Tk()
    root.geometry("1366x768")
    root.title("PRIORITY ORDER")
    heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="BLUE").pack()
    heading = Label(root, text="PRIORITY ORDERS", font=("arial", 30, "bold"), fg="RED").pack()

    label1 = Label(root, text="ENTER THE MONTH: ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=200)
    label2 = Label(root, text="TOTAL ORDER : ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=250)
    global month

    month = IntVar(root)
    data=IntVar(root)
    entry_box = Entry(root, textvariable=month, width=30, bg="white").place(x=280, y=210)
    entry_box = Entry(root, textvariable=data, width=30, bg="white").place(x=280, y=250)
    check = Button(root, text="PREDICT", width=10, height=2, bg="lightblue", command=sam).place(x=250, y=300)
    root.mainloop()

def fun4():
    def sam():

        def JAN():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("NOT COMPLETED ORDER PRIDICTION")
            with open('13.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h

            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)

        def FEB():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PREDICTION")
                with open('14.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h
                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def MAR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PREDICTION")
                with open('15.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def APR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PRIDICTION")
                with open('16.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def MAY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER  PRIDICTION")
                with open('17.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h
                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def JUNE():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER  PREDICTION")
                with open('18.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def JULY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER  PREDICTION")
                with open('19.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def AUG():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PREDICTION")
                with open('20.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def SEP():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PREDICTION")
                with open('21.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def OCT():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("NOT COMPLETED ORDER PREDICTION")
            with open('22.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def NOV():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("NOT COMPLETED ORDER PREDICTION")
                with open('23.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)


        def DEC():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("NOT COMPLETED ORDER PREDICTION")
            with open('24.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            r=eq(data.get())
            label=Label(root,text="THE NUMBER OF NOT COMPLETED ORDERS:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=r,font=("arial",20,"bold"),fg="indigo").place(x=50,y=500)



        def default():
          return "Incorrect day"
        switcher = {
            1:JAN,
            2:FEB,
            3:MAR,
            4:APR,
            5:MAY,
            6:JUNE,
            7:JULY,
            8:AUG,
            9:SEP,
            10:OCT,
            11:NOV,
            12:DEC,

        }
        def switch(operation):
          return switcher.get(operation, default)()

        print (switch(month.get()))
    root = Tk()


    root.title("INDUSTRIAL FINISHING")
    root.geometry("1366x768")
    heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="RED").pack()
    heading = Label(root, text="NOT COMPLETED ORDER PREDICTION", font=("arial", 30, "bold"), fg="BLUE").pack()

    label1 = Label(root, text="ENTER THE MONTH: ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=200)
    label2 = Label(root, text="TOTAL ORDERS : ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=250)
    global month

    month = IntVar(root)
    data=IntVar(root)
    entry_box = Entry(root, textvariable=month, width=30, bg="white").place(x=280, y=210)
    entry_box = Entry(root, textvariable=data, width=30, bg="white").place(x=280, y=250)
    check = Button(root, text="PREDICT", width=10, height=2, bg="lightblue", command=sam).place(x=250, y=300)
    root.mainloop()

def fun5():
    def sam():

        def JAN():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("TYPES OF THREAD PRIDICTION")
            with open('25.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                return h
            

            r=eq(data.get())
            if r>1 and r<2:
                k = "STABLE SPUN POLYESTER   "
            if r>2 and r<3:
                k = "POLY COTTON CORESPUN    "
            if r>3 and r<4:
                k = "TEXTURED NYLON          "
            if r>4:
                k = "ULTRA POLY POLY         "

            label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=k,font=("arial",20,"bold"),fg="lime").place(x=50,y=450)


        def FEB():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PRIDICTION")
                with open('26.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h
                
                r=eq(data.get())
              
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER   "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN    "
                if r>3 and r<4:
                    k = "TEXTURED NYLON          "
                if r>4:
                    k = "ULTRA POLY POLY         "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def MAR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PRIDICTION")
                with open('27.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h
                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER     "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN      "
                if r>3 and r<4:
                    k = "TEXTURED NYLON            "
                if r>4:
                    k = "ULTRA POLY POLY           "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def APR():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PRIDICTION")
                with open('28.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER    "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN     "  
                if r>3 and r<4:
                    k = "TEXTURED NYLON           "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def MAY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PRIDICTION")
                with open('29.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                print(r)
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER    "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN     "
                if r>3 and r<4:
                    k = "TEXTURED NYLON           "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def JUNE():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PREDICTION")
                with open('30.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER    "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN     "
                if r>3 and r<4:
                    k = "TEXTURED NYLON           "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def JULY():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PREDICTION")
                with open('31.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER   "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN    "
                if r>3 and r<4:
                    k = "NYLAN  TEXTURED NYLON   "
                if r>4:
                    k = "ULTRA POLY POLY         "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def AUG():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD  PREDICTION")
                with open('32.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER    "
                if r>2 and r<3: 
                    k = "POLY COTTON CORESPUN     "
                if r>3 and r<4:
                    k = "TEXTURED NYLON           "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def SEP():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PREDICTION")
                with open('33.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = " STABLE SPUN POLYESTER   "
                if r>2 and r<3:
                    k = " POLY COTTON CORESPUN    "
                if r>3 and r<4:
                    k = " TEXTURED NYLON          "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def OCT():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("TYPES OF THREAD PREDICTION")
            with open('34.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            
            r=eq(data.get())
            if r>1 and r<2:
                k = "STABLE SPUN POLYESTER   "
            if r>2 and r<3:
                k = "POLY COTTON CORESPUN    "
            if r>3 and r<4:
                k = "TEXTURED NYLON           "
            if r>4:
                k = "ULTRA POLY POLY          "
            
            label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def NOV():
                p = 0
                q = 0
                w1 = 0
                w0 = 0
                xa = 0
                ya = 0
                print("TYPES OF THREAD PREDICTION")
                with open('35.csv', 'r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx = []
                    listy = []
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                print("l1:", listx)
                print("l2:", listy)
                listx.pop(0)
                listy.pop(0)
                print("l1:", listx)
                print("l2:", listy)
                for i in listx:
                    i = int(i)
                    xa = xa + i
                xa = xa / len(listx)
                print("x:", xa)
                for j in listy:
                    j = int(j)
                    ya = ya + j
                ya = ya / len(listy)
                print("y:", ya)
                for (a, b) in zip(listx, listy):
                    m = float(a) - xa;
                    n = float(b) - ya;
                    p = p + (m * n)
                print(p)
                for i in listx:
                    i = int(i)
                    q = q + (i - xa) ** 2
                print(q)
                w1 = p / q
                print("w1:", w1)
                w0 = ya - (w1 * xa)
                print("w0:", w0)

                def eq(g):
                    h = w0 + (w1 * g)
                    print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                    return h

                r=eq(data.get())
                if r>1 and r<2:
                    k = "STABLE SPUN POLYESTER    "
                if r>2 and r<3:
                    k = "POLY COTTON CORESPUN     "
                if r>3 and r<4:
                    k = "TEXTURED NYLON           "
                if r>4:
                    k = "ULTRA POLY POLY          "
                    
                label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
                label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)


        def DEC():
            p = 0
            q = 0
            w1 = 0
            w0 = 0
            xa = 0
            ya = 0
            print("TYPES OF THREAD PREDICTION")
            with open('36.csv', 'r+') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                listx = []
                listy = []
                for row in readCSV:
                    listx.append(row[0])
                    listy.append(row[1])
            print("l1:", listx)
            print("l2:", listy)
            listx.pop(0)
            listy.pop(0)
            print("l1:", listx)
            print("l2:", listy)
            for i in listx:
                i = int(i)
                xa = xa + i
            xa = xa / len(listx)
            print("x:", xa)
            for j in listy:
                j = int(j)
                ya = ya + j
            ya = ya / len(listy)
            print("y:", ya)
            for (a, b) in zip(listx, listy):
                m = float(a) - xa;
                n = float(b) - ya;
                p = p + (m * n)
            print(p)
            for i in listx:
                i = int(i)
                q = q + (i - xa) ** 2
            print(q)
            w1 = p / q
            print("w1:", w1)
            w0 = ya - (w1 * xa)
            print("w0:", w0)

            def eq(g):
                h = w0 + (w1 * g)
                print("THE REGRESSION EQUATION IS : Y = ", w0, " + ", w1, " * X")
                return h
            
            r=eq(data.get())
            if r>1 and r<2:
                k = "STABLE SPUN POLYESTER   "
            if r>2 and r<3:
                k = "POLY COTTON CORESPUN    "
            if r>3 and r<4:
                k = "TEXTURED NYLON          "
            if r>4:
                k = "ULTRA POLY POLY         "
                    
            label=Label(root,text="TYPES OF THREAD MOSTLY ARRIVE:",font=("arial",20,"bold"),fg="indigo").place(x=50,y=400)
            label=Label(root,text=k,font=("arial",20,"bold"),fg="indigo").place(x=50,y=450)




        def default():
          return "Incorrect day"
        switcher = {
            1:JAN,
            2:FEB,
            3:MAR,
            4:APR,
            5:MAY,
            6:JUNE,
            7:JULY,
            8:AUG,
            9:SEP,
            10:OCT,
            11:NOV,
            12:DEC,

        }
        def switch(operation):
          return switcher.get(operation, default)()

        print (switch(month.get()))
    root = Tk()


    root.geometry("1366x768")
    root.title("DIFFRENT TYPES OF THREAD")
    heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="RED").pack()
    heading = Label(root, text="TYPES OF THREAD PREDICTION", font=("arial", 30, "bold"), fg="BLUE").pack()

    label1 = Label(root, text="ENTER THE MONTH: ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=200)
    label2 = Label(root, text="TOTAL ORDER : ", font=("arial", 18, "bold"), fg="BLACK").place(x=10, y=250)

    global month

    month = IntVar(root)
    data=IntVar(root)
    entry_box = Entry(root, textvariable=month, width=30, bg="white").place(x=280, y=210)
    entry_box = Entry(root, textvariable=data, width=30, bg="white").place(x=280, y=250)
    check = Button(root, text="PREDICT", width=10, height=2, bg="lightblue", command=sam).place(x=250, y=300)
    root.mainloop()

def fun6():

   
    def fun1():

        def reason():
                p=0
                q=0
                w1=0
                w0=0
                xa=0
                ya=0
                s=0
                t=0
                r=0
                print("IMPLEMENTATION OF LINEAR REGRESSION")
                data=pd.read_csv('49.csv',usecols = ['time'])
                data1=pd.read_csv('49.csv',usecols = ['machine'])
                with open('49.csv','r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx=[]
                    listy=[]
                    test=[]
                    for row in readCSV:
                        test.append(row[0])
                        listx.append(row[1])
                        listy.append(row[2])

                listx.pop(0)
                listy.pop(0)

                for i in data:
                    li=data[i]
                    l=(list(li))
                test_list = list(map(int, l)) 


                for i in data1:
                    lj=data1[i]
                    v=(list(lj))
                test_list1 = list(map(int, v)) 
                

                for i in listx:
                    i=int(i)
                    xa=xa+i
                xa=xa/len(listx)
               

                for j in listy:
                    j=int(j)
                    ya=ya+j
                ya=ya/len(listy)
               

                for (a,b) in zip(listx,listy):
                    m=float(a)-xa;
                    n=float(b)-ya;
                    p=p+(m*n)

                for i in listx:
                    i=int(i)
                    q=q+(i-xa)**2

                w1=p/q
                

                w0=ya-(w1*xa)
                

                def eq(g):
                    o1=[]
                    h=w0+(w1*g)
                    d=int(h)
                    y=len(data)
                    for i in range(y):
                        if l[i]<=d:
                            k=i
                            o=v[k]
                            m=str(o)
                            o1.append(m)
                    return o1
                r = eq(lot.get())
                label3 = Label(root, text="THE AVALIABLE MACHINE ARE:", font=("arial", 15, "bold"), fg="indigo").place(x=20,y=450)
                label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=20, y=500)
        root = Tk()
        root.geometry("1366x768")
        root.title("REASON FOR PRIORITY ORDERS DELAY")

        heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="red").pack()
        heading = Label(root, text="PREDICTION OF AVALIABLE MACHINE", font=("arial", 30, "bold"), fg="black").place(x=400,y=100)
        label1 = Label(root, text="ENTER THE NO.OF LOTS:   ", font=("arial", 18), fg="BLACK").place(x=400, y=200)

        lot = IntVar(root)

        entry_box = Entry(root, textvariable=lot,width=30, bg="white").place(x=720, y=210)
        check = Button(root, text="PREDICT", width=10, height=2, bg="lightgreen", fg="black",command=reason).place(x=600, y=350)
        
        root.mainloop()
    
    def fun2():
        def reason1():

            def JAN():
                p=0
                q=0
                w1=0
                w0=0
                xa=0
                ya=0
                s=0
                t=0
                r=0
                print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                with open('37.csv','r+') as csvfile:
                    readCSV = csv.reader(csvfile, delimiter=',')
                    listx=[]
                    listy=[]
                    for row in readCSV:
                        listx.append(row[0])
                        listy.append(row[1])
                #print("l1:",listx)
                #print("l2:",listy)
                listx.pop(0)
                listy.pop(0)
                #print("l1:",listx)
                #print("l2:",listy)
                for i in listy:
                    if i=='1':
                        s+=1
                    if i=='2':
                        t+=1
                    if i=='3':
                        r+=1
                print("packing material shortage:",s)
                print("machine repair:",t)
                print("workers leave:",r)
                for i in listx:
                    i=int(i)
                    xa=xa+i
                xa=xa/len(listx)
                #print("x:",xa)
                for j in listy:
                    j=int(j)
                    ya=ya+j
                ya=ya/len(listy)
                #print("y:",ya)
                for (a,b) in zip(listx,listy):
                    m=float(a)-xa;
                    n=float(b)-ya;
                    p=p+(m*n)
                #print(p)
                for i in listx:
                    i=int(i)
                    q=q+(i-xa)**2
                #print(q)
                w1=p/q
                #print("w1:",w1)
                w0=ya-(w1*xa)
                #print("w0:",w0)
                def eq(g):
                    h=w0+(w1*g)
                    return h

                r = eq(data.get())
                if r>1 and r<2:
                    k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                if r>2 and r<3:
                    k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                if r>3:
                    k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                    
                label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)
                    
            def FEB():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('38.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)
           
            def MAR():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('39.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def APR():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('40.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def MAY():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('41.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)
            def JUNE():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('42.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def JULY():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('43.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def AUG():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('44.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h
                    
                    r = eq(data.get()) 
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def SEP():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('45.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h

                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)


            def OCT():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('46.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h

                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def NOV():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('47.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h

                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)


            def DEC():
                    p=0
                    q=0
                    w1=0
                    w0=0
                    xa=0
                    ya=0
                    s=0
                    t=0
                    r=0
                    print("\tReason for priority orders and predict the upcoming priority orders face the problems and solution")
                    with open('48.csv','r+') as csvfile:
                        readCSV = csv.reader(csvfile, delimiter=',')
                        listx=[]
                        listy=[]
                        for row in readCSV:
                            listx.append(row[0])
                            listy.append(row[1])
                    #print("l1:",listx)
                    #print("l2:",listy)
                    listx.pop(0)
                    listy.pop(0)
                    #print("l1:",listx)
                    #print("l2:",listy)
                    for i in listy:
                        if i=='1':
                            s+=1
                        if i=='2':
                            t+=1
                        if i=='3':
                            r+=1
                    print("packing material shortage:",s)
                    print("machine repair:",t)
                    print("workers leave:",r)
                    for i in listx:
                        i=int(i)
                        xa=xa+i
                    xa=xa/len(listx)
                    #print("x:",xa)
                    for j in listy:
                        j=int(j)
                        ya=ya+j
                    ya=ya/len(listy)
                    #print("y:",ya)
                    for (a,b) in zip(listx,listy):
                        m=float(a)-xa;
                        n=float(b)-ya;
                        p=p+(m*n)
                    #print(p)
                    for i in listx:
                        i=int(i)
                        q=q+(i-xa)**2
                    #print(q)
                    w1=p/q
                    #print("w1:",w1)
                    w0=ya-(w1*xa)
                    #print("w0:",w0)
                    def eq(g):
                        h=w0+(w1*g)
                        return h

                    r = eq(data.get())
                    if r>1 and r<2:
                        k = "MORE CONCENTRATION ON PACKING MATERIAL TO AVOID THIS FAILURE   "
                    if r>2 and r<3:
                        k = "MORE CONCENTRATION ON MACHINE EFFICIENCY TO AVOID THIS FAILURE "          
                    if r>3:
                        k = "MORE CONCENTRATION ON WORKERS ABSENTISM TO AVOID THIS FAILURE  "
                        
                    label3 = Label(root, text="THE PREDICTED VALUE OF ORDER TO BE FAILURE IN THIS MONTH:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=450)
                    label3 = Label(root, text=r, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=500)
                    label3 = Label(root, text="SOLUTION:", font=("arial", 15, "bold"), fg="indigo").place(x=50,y=570)
                    label3 = Label(root, text=k, font=("arial", 15, "bold"), fg="maroon").place(x=50, y=620)

            def default():
              return "Wrong data"
            switcher = {
                1:JAN,
                2:FEB,
                3:MAR,
                4:APR,
                5:MAY,
                6:JUNE,
                7:JULY,
                8:AUG,
                9:SEP,
                10:OCT,
                11:NOV,
                12:DEC,

            }
            def switch(operation):
              return switcher.get(operation, default)()

            print (switch(month.get()))
        root = Tk()
        root.title("REASON FOR PRIORITY ORDERS DELAY")
        
        heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="red").pack()
        heading = Label(root, text="PRIORITY DELAY PREDICTION", font=("arial", 30, "bold"), fg="black").place(x=400,y=100)
        
        label1 = Label(root, text="ENTER THE MONTH:   ", font=("arial", 18), fg="BLACK").place(x=400, y=200)
        label2 = Label(root, text="ENTER NO.OF ORDERS:", font=("arial", 18), fg="BLACK").place(x=400, y=250)
        
        month = IntVar(root)
        data=IntVar(root)


        entry_box = Entry(root, textvariable=month,width=30, bg="white").place(x=700, y=210)
        entry_box = Entry(root, textvariable=data,width=30, bg="white").place(x=700, y=260)
        check = Button(root, text="PREDICT", width=10, height=2, bg="lightgreen", fg="black",command=reason1).place(x=600, y=350)

    root = Tk()
    root.geometry("1366x768")
    #background_image = tk.PhotoImage(file='Coats.png')
    #background_label = tk.Label(root, image=background_image)
    #background_label.place(relwidth=1, relheight=1)
    root.title("REASON FOR PRIORITY ORDERS DELAY")
    heading = Label(root, text="MADURA COATS", font=("arial", 40, "bold"), fg="red").pack()
    heading = Label(root, text="PREDICTION OF AVALIABLE MACHINE", font=("arial", 20, "bold"), fg="black").place(x=10,y=100)
    heading = Label(root, text="PRIORITY DELAY PREDICTION", font=("arial", 20, "bold"), fg="black").place(x=750,y=100)


    check = Button(root, text="PREDICT", width=10, height=2, bg="lightgreen", fg="black",command=fun1).place(x=180, y=200)
    check = Button(root, text="PREDICT", width=10, height=2, bg="lightgreen", fg="black",command=fun2).place(x=900, y=200)

    root.mainloop()
 
    
    
root = Tk()
root["bg"] = "red"
root.geometry("1366x768")
#root["bg"] = "black"
#root.configure(bg="red")
background_image = tk.PhotoImage(file='Coats.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
root.title("PREDICTION")
heading = Label(root, text="MADURA COATS PRIVATE LIMITED ", font=("arial", 40, "bold"), fg="RED").pack()
heading = Label(root, text="PREDICTION APPLICATION", font=("arial", 30, "bold"), fg="BLUE").pack()
check = Button(root, text="PACKING MATERIAL", width=20, height=2, bg="lightblue", command=fun1).place(x=200, y=150)
check = Button(root, text="DELAY", width=10, height=2, bg="lightblue", command=fun2).place(x=380, y=150)


check = Button(root, text="PRIORITY", width=10, height=2, bg="lightblue", command=fun3).place(x=490, y=150)

check = Button(root, text="NOT COMPLETED ORDERS", width=22, height=2, bg="lightblue", command=fun4).place(x=600, y=150)

check = Button(root, text="THREAD TYPE", width=12, height=2, bg="lightblue", command=fun5).place(x=800, y=150)

check = Button(root, text="IDLE TIME/ORDER DELAY", width=20, height=2, bg="lightblue", command=fun6).place(x=930, y=150)

root.mainloop()
 