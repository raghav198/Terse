section .text
global _start

_start:
  mov edx,len
  mov ecx,msg
  mov ebx,1
  mov eax,4
  int 80h
  mob eax,1
  int 80h

section .data
  msg db 'Hello, world!",0xa
  len equ $-msg
