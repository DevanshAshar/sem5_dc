FACT MACRO F
    UP:
    MUL F
    DEC F
    JNZ UP
ENDM
DATA SEGMENT
    NUM DW 06H
    RESULT DW ?
ENDS
CODE SEGMENT
    START:
    MOV AX, DATA
    MOV DS,AX
    MOV CX,NUM
    MOV AX,0001H
    FACT NUM
    MOV RESULT,AX
ENDS
END START
