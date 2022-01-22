# Description
![image](https://user-images.githubusercontent.com/49471288/150625910-1b11d1a7-4fcf-4717-a3f8-389e3a6ddf92.png)
#### Since I'm not a big fan of MARVEL, the only thing I can understood was there are ciphertext and encryptor.
---

![image](https://user-images.githubusercontent.com/49471288/150625926-de6ced94-433b-434e-9687-e9840aaa2728.png)
#### Through the link below the description of challenge, There are two files.
#### "letter.txt" is the letter from villain named **Mandarin**
---

# Letter
```
Hey Actor,
You are doing great!
I didn't expect that you would be able to fool everybody as impressively you are doing the job!

By the way, you have something important to do now.
Go to our base in "6G:653" and launch all the normal missiles and set a timer of 4 hours for launching our "Fat Boy", I mean the nuclear one.
Take half of your army with you as you need to defend the launching site and send others after Tony and James.

I've already sent the password for activating the normal missiles.
And here are the clue keys for activating the Fat Boy:

- T3NR1NG$
- T3nR1ng$
- TenRings
- T3nR!ngs
- T3nR!ng$
- 73NR1GN$
- 73nRing$
- T3nR!nG$

I believe, you already know which one is the valid key. 
Just giving the clues to give you a simple recall.

So, get to the work! And don't forget to make a public broadcast 5 minutes before you launch the missile.

Announce a war against Tony and James.
If Tony surrenders, then stop the timer of Fat Boy.
Otherwise, let the destruction happen!

Hahahahahahaha!

Oh, the password for deactivating the nuclear missile is "IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"

The password is encrypted and I believe, you know how to decode that, my boy!

That's all for now.
Work according the instruction and then wait for my next instruction.

Regards,
Mandarin
```
There are some weird letters in text which is _"6G:653"_ in
~~~
By the way, you have something important to do now.
Go to our base in "6G:653" and launch all the normal missiles and set a timer of 4 hours for launching our "Fat Boy", I mean the nuclear one.
Take half of your army with you as you need to defend the launching site and send others after Tony and James.
~~~
and _"IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"_ in
~~~
Oh, the password for deactivating the nuclear missile is "IihsIb_7[^7is<inH][l_^D`Ib_;[n7iu"
~~~

Obviously, they are encrypted ciphertext and Since the description says that format of the flag is KCTF{NAMEOFTHEPLACE_PasswordForDeactivation}, I had to concatenated them after.

---

# Encryptor
Encryption process is written in python script and shown as below
```python
secret = input("Enter your string to encrypt: ")

key = input("Enter the key: ")

secarr = []

keyarr = []

x = 0
 
def keyfunc(key,keyarr,x):

    for character in key:

        keyarr.append(ord(character))

    for i in keyarr:

        x += i

def secretfucn(secret,secarr,key,x):

    for character in secret:

        secarr.append(ord(character))

    for i in range(len(secarr)):

        if 97 <= secarr[i] <= 122:
            
            secarr[i] = secarr[i]-6
        else:
            if 65 <= secarr[i] <= 90:
                
                secarr[i] = secarr[i]-11

    if len(key) % 2 == 0:

        x = x + 1

    else:

        x = x + 3

    if x % 2 == 0:

        secarr[i] = secarr[i] + 3

    else:

        secarr[i] = secarr[i] + 2

    encrypted = ""

    for val in secarr:

        encrypted = encrypted + chr(val)

    print("Encrypted Text: " + encrypted)

            
keyfunc(key,keyarr,x)

secretfucn(secret,secarr,key,x)
```

Description of Encryption process
1. Get a text(plaintext) for encryption
2. For each of character in plaintext, if the character is
    1. 'a' ~ 'z' : -6 to the character
    2. 'A' ~ 'Z' : -11 to the character
3. For the last character of the text, +3 or +2 based on the key

So, It's just a simple caesar cipher.
But the tricky part was step 3. (the last letter)

After I got a text from the decryptor(without step 3) I've coded, the server said my flag is incorrect.
![image](https://user-images.githubusercontent.com/49471288/150626585-2f44512d-b277-4155-b1c2-09507a2d51ba.png)

Then I guess that "Bou" should be "Boy", and include the step 3 to figure out the correct name of place.
In fact, there are only two possible result of step 3 (-2 or -3), so I put AREA51 and AREA50 one by one and got point
