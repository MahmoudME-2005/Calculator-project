# from tkinter import *
# from random import *

# root = Tk()
# root.geometry("500x360")
# root.title("Simple calculator")
# root.configure(bg=("#1d3849"))
# global nums
# nums = []
# global out_bool
# out_bool = False


# def input_func(x):
#     nums.append(x)
#     global input
#     input = Label(anchor=NW, text=nums, width=70,
#                   height=3, bg="#142f44", fg="#a2bbcf", font=("TkDefaultFont", 20))
#     input.place(x=0, y=0)


# def deleter():
#     nums.pop()
#     input.config(text=nums)


# def output_func():
#     a = nums.count("+")
#     b = nums.count("-")
#     c = nums.count("x")
#     d = nums.count("/")
#     if a != 0:
#         a = nums.index("+")
#         g = "".join(nums[:a])
#         h = "".join(nums[a + 1:])
#         result = int(g) + int(h)
#     if b != 0:
#         b = nums.index("-")
#         g = "".join(nums[:b])
#         h = "".join(nums[b + 1:])
#         result = int(g) - int(h)
#     if c != 0:
#         c = nums.index("x")
#         g = "".join(nums[:c])
#         h = "".join(nums[c + 1:])
#         result = int(g) * int(h)
#     if d != 0:
#         d = nums.index("/")
#         g = "".join(nums[:d])
#         h = "".join(nums[d + 1:])
#         result = int(g)/int(h)
#     global output
#     output = Label(text=result, font=("TkDefaultFont", 20),
#                    bg="#142f44", fg="#a2bbcf")
#     output.place(x=250, y=35)
#     global out_bool
#     out_bool = True


# def clearer():
#     global out_bool
#     if out_bool == True:
#         output.place_forget()
#     global nums
#     nums = []
#     input.config(text=nums)
#     out_bool = False


# button1 = Button(command=lambda: input_func("1"), text="1",
#                  padx=40, pady=20).place(x=0, y=100)

# button2 = Button(command=lambda: input_func("2"), text="2",
#                  padx=40, pady=20).place(x=100, y=100)

# button3 = Button(command=lambda: input_func("3"), text="3",
#                  padx=40, pady=20).place(x=200, y=100)

# button4 = Button(command=lambda: input_func("4"), text="4",
#                  padx=40, pady=20).place(x=0, y=165)

# button5 = Button(command=lambda: input_func("5"), text="5",
#                  padx=40, pady=20).place(x=100, y=165)

# button6 = Button(command=lambda: input_func("6"), text="6",
#                  padx=40, pady=20).place(x=200, y=165)

# button7 = Button(command=lambda: input_func("7"), text="7",
#                  padx=40, pady=20).place(x=0, y=230)

# button8 = Button(command=lambda: input_func("8"), text="8",
#                  padx=40, pady=20).place(x=100, y=230)

# button9 = Button(command=lambda: input_func("9"), text="9",
#                  padx=40, pady=20).place(x=200, y=230)

# button0 = Button(command=lambda: input_func("0"), text="0",
#                  padx=40, pady=20).place(x=0, y=295)

# button00 = Button(command=lambda: input_func("00"), text="00",
#                   padx=40, pady=85).place(x=400, y=165)


# op_add = Button(text="+", command=lambda: input_func("+"),
#                 padx=39, pady=20).place(x=300, y=100)

# op_sub = Button(text="-", command=lambda: input_func("-"),
#                 padx=40, pady=20).place(x=300, y=165)

# op_multy = Button(text="x", command=lambda: input_func("x"),
#                   padx=40, pady=20).place(x=300, y=230)

# op_div = Button(text="/", command=lambda: input_func("/"),
#                 padx=41, pady=20).place(x=300, y=295)


# output_button = Button(text="=", command=output_func,
#                        padx=39, pady=20).place(x=100, y=295)

# back_space_button = Button(text="<-", command=deleter,
#                            padx=40, pady=20).place(x=400, y=100)

# ac_button = Button(text="AC", command=clearer, padx=35,
#                    pady=20).place(x=200, y=295)


# root.mainloop()
from tkinter import *
from random import *

root = Tk()
root.geometry("500x360")
root.title("Simple calculator")
img = PhotoImage(file="E:\Programming\Resources\calculator.png")
root.iconphoto(True,img)
root.configure(bg=("#1d3849"))
global nums
nums = []
global out_bool
global error_bool
out_bool = False
error_bool = False
global nums2
nums2 = []


def input_func(x):
    if x == "x":
        nums.append("*")
    else:
        nums.append(x)
    nums2.append(x)
    if nums2[-1] == "x" and nums2[-2] == "x":
        nums2.pop()
        nums2[-1] = nums2[-1].replace("x","^")
    global input
    input = Label(anchor=NW, text=nums2, width=32,
                  height=3, bg="#142f44", fg="#a2bbcf", font=("TkDefaultFont", 20))
    input.place(x=0, y=0)


def deleter():
    nums2.pop()
    nums.pop()
    input.config(text=nums2)


def output_func():
    try:
        a = ""
        num = a.join(nums)
        if num.find("++") == -1 and num.find("+-") == -1 and num.find("-+") == -1 and num.find("--") == -1:
            result = eval(num)
            global output
            output = Label(text= result, font=("TkDefaultFont", 20),
                        bg="#142f44", fg="#a2bbcf")
            output.place(x=300, y=35)
            out_bool = True
        else:
            global error
            error = Label(text="Syntax error", font=("TkDefaultFont",20),bg="#142f44", fg="#a2bbcf")
            error.place(x=300,y=35)
            error_bool = True
    except:
        error = Label(text="Syntax error", font=("TkDefaultFont",20),bg="#142f44", fg="#a2bbcf")
        error.place(x=300,y=35)
        error_bool = True





def clearer():
    global out_bool
    global error_bool
    if error_bool == True:
        error.place_forget()
    if out_bool == True:
        output.place_forget()
    global nums
    global nums2
    nums2 = []
    nums = []
    input.config(text=nums2)
    out_bool = False
    error_bool = False


button1 = Button(command=lambda: input_func("1"), text="1",
                 padx=40, pady=20).place(x=0, y=100)

button2 = Button(command=lambda: input_func("2"), text="2",
                 padx=40, pady=20).place(x=100, y=100)

button3 = Button(command=lambda: input_func("3"), text="3",
                 padx=40, pady=20).place(x=200, y=100)

button4 = Button(command=lambda: input_func("4"), text="4",
                 padx=40, pady=20).place(x=0, y=165)

button5 = Button(command=lambda: input_func("5"), text="5",
                 padx=40, pady=20).place(x=100, y=165)

button6 = Button(command=lambda: input_func("6"), text="6",
                 padx=40, pady=20).place(x=200, y=165)

button7 = Button(command=lambda: input_func("7"), text="7",
                 padx=40, pady=20).place(x=0, y=230)

button8 = Button(command=lambda: input_func("8"), text="8",
                 padx=40, pady=20).place(x=100, y=230)

button9 = Button(command=lambda: input_func("9"), text="9",
                 padx=40, pady=20).place(x=200, y=230)

button0 = Button(command=lambda: input_func("0"), text="0",
                 padx=40, pady=20).place(x=0, y=295)

button00 = Button(command=lambda: input_func("00"), text="00",
                  padx=40, pady=85).place(x=400, y=165)


op_add = Button(text="+", command=lambda: input_func("+"),
                padx=39, pady=20).place(x=300, y=100)

op_sub = Button(text="-", command=lambda: input_func("-"),
                padx=40, pady=20).place(x=300, y=165)

op_multy = Button(text="x", command=lambda: input_func("x"),
                  padx=40, pady=20).place(x=300, y=230)

op_div = Button(text="/", command=lambda: input_func("/"),
                padx=41, pady=20).place(x=300, y=295)


output_button = Button(text="=", command=output_func,
                       padx=39, pady=20).place(x=100, y=295)

back_space_button = Button(text="<-", command=deleter,
                           padx=40, pady=20).place(x=400, y=100)

ac_button = Button(text="AC", command=clearer, padx=35,
                   pady=20).place(x=200, y=295)


root.mainloop()