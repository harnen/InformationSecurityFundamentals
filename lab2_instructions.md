# Week 2 - Malware and Buffer Overflow

## Challenge 1

Disable ALSR on your machine using `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`

Compile `challenge1.c` using `gcc challenge1.c -o challenge1 -m32 -fno-stack-protector -z execstack -g`

Run the file with an input that will change the value of modified to something other than 0.

Add a `printf` statements to your code that will print the pointer values for buffer and modified variables.

Run the program several times and observe the pointer values.

Recompile the program without the `-fno-stack-protector`. What changed? Is your attack still possible?

Enable ALSR on your machine and run the program again (modify the command from the beginning of this task). What changed? How ALSR protects against buffer overflow attacks? 

## Challenge 2

Disable ALSR on your machine using `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`

Compile `challenge2.c` using `gcc challenge2.c -o challenge2 -m32 -fno-stack-protector -z exe<cstack -g`

Run the file with an input that will change the value of modified to 0x0d0a0d0a. 

```
$./challenge2 `python2 -c 'print "A"*64 + "\x0b\x0d\x0b\x0d"'`
```

## Challenge 3

Analyze the code of `challenge3.c`. The compiled version of the file is already present in the zip file. Do not recompile the file yourself (recompiling may make the challenge much more difficult to solve).

Run the file with an input that will cause the winner function to be called. 
