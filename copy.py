import pyscreenshot as ImageGrab
path="1_try.png"

#image = ImageGrab.grabclipboard()
im = ImageGrab.grab()
im.save(path,'PNG')


