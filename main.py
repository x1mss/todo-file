import PySimpleGUI as sg
import time

sg.theme("Topanga")

shedule_file = open("todo.txt", "r" , encoding="utf-8")

todo_list = shedule_file.readlines()

clock = sg.Text("Часы",key='clock')
label = sg.Text("План на день:")
imput_shudele = sg.InputText(key='todo')
add = sg.Button("Добавить")
shudele_list = sg.Listbox(values=todo_list,key='todos_f', size=[50,20])
edit = sg.Button("Изменить")
del_ = sg.Button("Удалить")
exit = sg.Button("Выход")

window = sg.Window("Shedule", layout=[
    [clock],
    [label, imput_shudele ],
    [add],
    [shudele_list , edit , del_],
    [exit]],
    font=("Segoe Print", 15)
)

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime('%a %d %B %H:%M:%S'))
    if event == "Изменить":
        todo_edit = values['todos_f'][0]
        index = todo_list.index(todo_edit)
        todo_list[index] = values["todo"] + '\n'
        window['todos_f'].update(values=todo_list)
        with open("todo.txt", "w", encoding="utf-8") as file:
            file.writelines(todo_list)
    if event == "Добавить":
        todo_list.append(values['todo'] + '\n')
        window['todos_f'].update(values=todo_list)
        with open("todo.txt", "w", encoding="utf-8") as file:
            file.writelines(todo_list)
    if event == "Удалить":
        todo = values['todos_f'][0]
        todo_list.remove(todo)
        window['todos_f'].update(values=todo_list)
        with open("todo.txt", "w", encoding="utf-8") as file:
            file.writelines(todo_list)
    if event == "Выход":
        print("Вы можете выйти.")
    if event == sg.WIN_CLOSED:
            break

window.close()