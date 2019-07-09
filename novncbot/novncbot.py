#!/usr/bin/env python3
from enum import IntEnum
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import logging

log = logging.getLogger(__name__)

class Keys(IntEnum):
  TAB		= 0xff09
  ENTER	= 0xff0d
  LEFT	= 0xff51
  UP		= 0xff52
  RIGHT	= 0xff53
  DOWN	= 0xff54

class NoVNCbot(object):

  def __init__(self):
    options = Options()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)

  def __sendKey(self, keycode):
    log.debug("pressing %s" % hex(keycode))
    self.__sendKeyDown(keycode)
    self.__sendKeyUp(keycode)

  def sendKeys(self, str):
    # Convert int to string
    #if type(str) == int:
    #  self.sendKeys(format(str))
    if isinstance(str, Keys):
      self.__sendKey(str.value)
    # Send char by char
    else:
      for x in range(len(str)):
        self.__sendKey(ord(str[x]))

  def __sendKeyDown(self, keycode):
    self.driver.execute_script("rfb.sendKey(%s,1);" % (keycode))

  def __sendKeyUp(self, keycode):
    self.driver.execute_script("rfb.sendKey(%s,0);" % (keycode))
  
  class __rfb_is_ready(object):
    def __call__(self, driver):
      out = driver.execute_script("return rfb._rfb_state")
      log.debug("Busy waiting for %s == normal" % out)
      if out == "failed":
        raise Exception("RFB failed to connect. Invalid/Expired URL?")
      if out == "normal":
        return True
      else:
        return False

  def connect(self, url):
    self.driver.get(url)

    # Wait until novnc is connected
    WebDriverWait(self.driver, 5).until(self.__rfb_is_ready())

  def disconnect(self):
    self.driver.quit()

if __name__ == "__main__":
  import sys

  console_url = sys.argv[1]

  bot = NoVNCbot()
  bot.connect(console_url)

  bot.sendKeys("d")
  bot.sendKeys(Keys.TAB)
  bot.sendKeys(" TEST123")
  bot.sendKeys(Keys.ENTER)

  bot.disconnect()

