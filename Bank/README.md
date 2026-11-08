# Bank Simulator

Hi. This is a small Python program I made to practice programming.

It is a fake bank. You can put money in, take money out and 
look at your balance. Everything happens in the terminal.

I am a beginner. I made this to learn. It is not perfect.

## How to use

You need Python 3 installed.

First install two things:
pip install rich pwinput


Then run it:
python main.py



## What happens when you run it

The program asks for:
- your name
- your ID
- a password (minimum 5 characters)

Then you see a menu:
1 - Deposit
2 - Withdraw
3 - See your balance
0 - Leave



If you pick option 2 or 3, it asks for your password again.
If the password is wrong, nothing happens.

## What is in the code

There are two files:

- `bank.py` - the bank logic
- `main.py` - the menu

In `bank.py` I made a class called `Bank`. Inside there is a 
private balance that only the class can change. That is called 
encapsulation (I think). The password is not saved as text, 
only as a SHA-256 hash. I learned that from a YouTube video.

## What I learned

- how to make a class in Python
- how `@property` works
- how to hash a password with `hashlib`
- how to handle wrong input with `try` and `except`

## What is missing

- the balance is not saved when you close the program
- no GUI, only terminal
- only one account
- the password check is not safe for a real bank

I want to add the saving part later. Maybe with a file or SQLite.

## Why I made this

I want to become an "Anwendungsentwickler" in Germany and I am 
applying for an apprenticeship. So I built this to have something 
to show.

If you have tips, I am happy to hear them.

GitHub: [MyguelTech134](https://github.com/MyguelTech134)