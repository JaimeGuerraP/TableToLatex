#!/bin/bash

filename="LatexTableFile.tex"
PythonFile=$(readlink -f ~/.myPrograms/TableToLatex)
PythonFile=${PythonFile%TableToLatex.sh}
PythonFile=$PythonFile"TableLatex.py"

argument=$(cat);

if [ -n "$argument" ]
then
    LatexText=$($CONDA_PYTHON_EXE $PythonFile "$argument")
else
    echo 'The argument is missing.'
fi

echo "$LatexText" > $filename
