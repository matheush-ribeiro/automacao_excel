#Ler dados da planilha
#Inserir cada célula de cada linha em um campo do sistema

import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    #["Murilo Barros","Cadeira","343","Esportes"]
    pyautogui.click(1208,494,duration=1.5)
    pyautogui.write(linha[0].value)
    pyautogui.click(1210,518,duration=1.5)
    pyautogui.write(linha[1].value)
    pyautogui.click(1215,543,duration=1.5)
    pyautogui.write(str(linha[2].value))
    pyautogui.click(1212,565,duration=1.5)
    pyautogui.write(linha[3].value)
    pyautogui.click(1245,591,duration=1.5)
    pyautogui.write(linha[4].value)