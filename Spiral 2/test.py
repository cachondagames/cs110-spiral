import PySimpleGUI as sg

layout = [[sg.Text('Please select the option you would like to play!')],      
                 [sg.B("2 Player", size = (50,1))]]      

window = sg.Window('CS110 Flight Simulator', layout)    

event, values = window.read()    
window.close()


if event == "2 Player":
    print("heloo")
