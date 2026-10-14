import pyautogui as pg 



pg.moveTo(100, 100, duration=0.5)
pg.moveTo(100, 300, duration=0.5)
pg.moveTo(300, 300, duration=0.5)
pg.moveTo(300, 100, duration=0.5)


pg.press("win")
pg.sleep(1)

pg.write("chrome", interval=0.5)

pg.press("enter")

pg.sleep(1)
pg.write("www.youtube.com", interval=0.5)

pg.press("enter")

pg.moveTo(745,112, duration=3.0)
pg.click()
pg.write("viros")
pg.press("enter")
pg.moveTo(765,566, duration=3.0)
pg.click()
#pg.mouseInfo()

