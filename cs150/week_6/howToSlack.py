# share code with slack

mouse = 'click'
one = 1
button = 'plus sign'
text = 'code or text snippet'
snek = 'python'


def howTo(click):
    if click == 1:
        print('{} the {} next to the text box.'.format(mouse, button))
        print('Next, select "{}"'.format(text))
        print('Then copy and paste your code to share. Slack can recognize {}, but you can select the language yourself with the dropdown\n'.format(snek))


howTo(one)
