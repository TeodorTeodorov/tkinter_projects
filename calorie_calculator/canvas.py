import math
from tkinter import *
from PIL import ImageTk ,Image



def create_root():
    root = Tk()

    root.title("Calorie calculator")
    root.resizable(False, False)
    root.geometry("850x700")

    return root


def create_frame():
    frame = Canvas(root, width=850, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()


def create_picture():
    img = Image.open("pic1.png")
    image = img.resize((380,605) , Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(image)
    frame.create_image(630, 380, image=new_img)


    return new_img

img = create_picture()

def data():
    calculate_button = Button(
        root,
        text = "Изчисли",
        bg = "blue",
        fg='white',
        borderwidth=0,
        width=10,
        height=2,
        command=get_data
    )
    frame.create_text(440, 30,text="Внимание!\nРезултатите от този калкулатор са приблизителен ориентир",font=("arial", 15))
    frame.create_window(100, 600, window=calculate_button)


    frame.create_text(100, 90, text="Години",justify= RIGHT)
    frame.create_text(100, 140, text="Тегло в кг",justify= RIGHT)
    frame.create_text(100, 190, text="Височина в см",justify= RIGHT)
    frame.create_text(100, 240, text='Обиколка врат в см',justify= RIGHT)
    frame.create_text(100, 290, text="Обиколка 3 см над пъпа",justify= RIGHT)
    frame.create_text(100, 340, text="Обиколка през пъпа",justify= RIGHT)
    frame.create_text(100, 390, text="Обиколка ханш в см",justify= RIGHT)
    frame.create_text(100, 440, text="Тренировъчни дни седмично",justify= RIGHT)


def boxes():
    frame.create_window(300, 90, window=years_box)
    frame.create_window(300, 140, window=weight_box)
    frame.create_window(300, 190, window=height_box)
    frame.create_window(300, 240, window=tour_neck)
    frame.create_window(300, 290, window=tour_1_box)
    frame.create_window(300, 340, window=tour_2_box)
    frame.create_window(300, 390, window=tour_3_box)
    frame.create_window(300, 440, window=training_days_box)



def get_data():
    data_dict = {
        "years":years_box.get(),
        "weight": weight_box.get(),
        "height":height_box.get(),
        "tour_neck":tour_neck.get(),
        "tour_1":tour_1_box.get(),
        "tour_2":tour_2_box.get(),
        "tour_3":tour_3_box.get(),
        "training_days":training_days_box.get()
    }


    if check_data(data_dict):
        calculation(data_dict)


def check_data(info):
    frame.delete("done")
    for el in info.values():
        if not el.strip():
            frame.create_text(
                200,
                500,
                text="Всички полета трябва да са попълнени!",
                font=('Times New Roman', 15, 'bold'),
                fill="red",
                tags="error"
            )

            return False
        frame.delete("error")

        if not el.isdigit():
            frame.create_text(
                200,500,
                text="Данните трябва да съдъжат само числа",
                fill="red",
                font=('Times New Roman', 15, 'bold'),
                tags="error"
            )

            return False
        frame.delete("error")




        if info["years"] == el and (15 > int(el) or int(el) > 60):
            frame.create_text(
                200, 500,
                text="Смята само на хора между 16г и 60г",
                fill="red",
                font=('Times New Roman', 15, 'bold'),
                tags="error"
            )

            return False

        frame.delete("error")

        if info["weight"] == el and int(el) < 20:
            frame.create_text(
                200, 500,
                text="На скелети не смятам",
                fill="red",
                font=('Times New Roman', 15, 'bold'),
                tags="error"
            )
            return False
        frame.delete("error")

        if info["weight"] == el and int(el) > 220:
            frame.create_text(
                200, 500,
                text="На моржове не смятам",
                fill="red",
                font=('Times New Roman', 15, 'bold'),
                tags="error",

            )
            return False
        frame.delete("error")

    frame.delete("error")

    return True



def calculation(data_dict):
    frame.delete("done")
    calc_data = []
    for el in data_dict.values():
        calc_data.append(int(el))
    bmi_m = 66 + (13.7 * calc_data[1]) + (5 * calc_data[2]) - (6.8 * calc_data[0])
    if calc_data[7] <= 1:
        bmi_m *= 1.2
        down_weight = bmi_m * 0.90
        frame.create_text(200,500,
                        text=f"Вие имата нужда от {math.ceil(bmi_m)} калории дневно,\n за да поддържате това тегло"
                             f" и {down_weight} калории дневно, за да сваляте телесна маса.",
                        fill="black",
                        font=('Times New Roman', 12),
                        tags="done"
                        )
    elif calc_data[7] == 2 or calc_data[7] == 3:
        bmi_m *= 1.375
        down_weight = bmi_m * 0.90
        frame.create_text(200, 500,
                          text=f"Вие имата нужда от {math.ceil(bmi_m)} калории дневно,\nза да поддържате това тегло"
                               f" и {math.ceil(down_weight)} калории дневно,\nза да сваляте телесна маса.",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 4 <= calc_data[7] <= 5:
        bmi_m *= 1.55
        down_weight = bmi_m * 0.90
        frame.create_text(200, 500,
                          text=f"Вие имата нужда от {math.ceil(bmi_m)} калории дневно,\nза да поддържате това тегло"
                               f" и {math.ceil(down_weight)} калории дневно,\nза да сваляте телесна маса.",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 6 <= calc_data[7] <= 7:
        bmi_m *= 1.725
        down_weight = bmi_m * 0.90
        frame.create_text(200, 500,
                          text=f"Вие имата нужда от {math.ceil(bmi_m)} калории дневно,\nза да поддържате това тегло"
                               f" и {math.ceil(down_weight)} калории дневно,\nза да сваляте телесна маса.",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif calc_data[7] > 7:
        frame.create_text(200, 500,
                          text="Невизможно е да тренирате повече\n от 7 пъти в седмицата!",
                          fill="red",
                          font=('Times New Roman', 15, 'bold'),
                          tags="done"
                          )
    if 60 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 70:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 10%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 71 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 80:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 12.5%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 81 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 90:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 15%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 91 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 100:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 17.5%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 101 <= (calc_data[4] and calc_data[5] and calc_data[6]) <= 110:
        frame.create_text(200, 550,
                      text="Приблизителни теленси мазнини - 20%",
                      fill="black",
                      font=('Times New Roman', 12),
                      tags="done"
                      )
    elif 111 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 120:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 22.5%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 121 <= (calc_data[4]  and calc_data[5] and calc_data[6]) <= 130:
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - 25%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    elif 131 <= (calc_data[4]  and calc_data[5] and calc_data[6]):
        frame.create_text(200, 550,
                          text="Приблизителни теленси мазнини - над 30%",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )
    else:
        frame.create_text(200, 550,
                          text="Не може да изчислим подкожните ви мазнини",
                          fill="black",
                          font=('Times New Roman', 12),
                          tags="done"
                          )











years_box = Entry(root, bd=0)
weight_box = Entry(root, bd=0)
height_box = Entry(root, bd=0)
tour_neck = Entry(root, bd=0)
tour_1_box = Entry(root, bd=0)
tour_2_box = Entry(root, bd=0)
tour_3_box = Entry(root, bd=0)
training_days_box = Entry(root, bd=0)

