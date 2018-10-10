import time
import subprocess

phrase = "I would like to change my brightness, but I also hate myself."
word_count = len(phrase.split())

start_txt = raw_input("Please type the below phrase to change the screen brightness. Your WPM will determine the resulting brightness.\n\n\tPhrase: {}\n\nPress enter to start, and enter again when finished...".format(phrase))

# Record time to type phrase
t_start = time.time()
in_text = str(raw_input())
t_end = time.time()

# Calculate accuracy
in_words = in_text.split()
corr_words = phrase.split()
if not in_words:
    acc = 0
elif len(in_words) < word_count:
    acc = len(in_words)
else:
    acc = word_count
for word in in_words:
    if word not in corr_words:
        acc -= 1
acc = float(acc)/float(word_count)

# Calculate WPM and resulting brightness
wpm = ((word_count*acc)/(t_end - t_start))*60
brightness = float(wpm)/100.00

# Run AppleScript to change brightness 
print 'Setting screen brightness to {}%'.format(format(brightness, '.2f'))
subprocess.check_output(['osascript', 'set-brightness.scpt', str(int(brightness*16))])