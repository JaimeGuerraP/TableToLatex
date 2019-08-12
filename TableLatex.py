#------------------------------------------------------------------
#This program makes a Latex table from a txt string
#Author: Jaime Guerra
#------------------------------------------------------------------
import sys


String = sys.argv[1]
lineas  = String.split('\n')
HeaderLatexTable = '\\begin{table}[!h]\n\centering\n\\begin{tabular}{|c |c |c |c |c |c |c |c |}\n'
HorLine = '\hline'
EndLatexTable = '\end{tabular}\n\end{table}'
DocumentHeader = '\documentclass[11pt]{book} \n\\usepackage[letterpaper, left=4 cm, right=4 cm, top=4 cm, bottom=4 cm]{geometry} \n\\usepackage[utf8]{inputenc} \n\n\\begin{document} \n'
EndDocument = '\\end{document}'
ColumnSeparator = ' & '
LineSeparator = ' \\'
LatexText = ''
Cadena = ''
ps = 1
flag = False
for linea in lineas:
    if ps == 1:
        if linea == '':
            if flag == False:
                continue
        else:
            Cadena = linea + '\n' + HeaderLatexTable
            ps += 1
    else:
        
        ps += 1
        if linea == '' and flag == True:
            Cadena += HorLine + '\n'
            Cadena += '\n'
            Cadena += EndLatexTable + '\n' + '\n'
            LatexText += Cadena
            Cadena = ''
            ps = 1
            flag = False
        else:
            Cadena += HorLine + ' ' + linea.replace('\t', ColumnSeparator ) + ' \\'+ '\\' +'\n'
            flag = True

LatexText = LatexText.replace('#','')
LatexText = DocumentHeader + LatexText + EndDocument
print(LatexText)
