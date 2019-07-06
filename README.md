# noVNCbot
Send keystrokes to a noVNC session.
## Usage
This is most useful for appending to the commandline of an initial OS install in OpenStack
## Example
First, Boot from an install ISO. The following will connect via noVNC and append to the boot arguments
```python
#!/usr/bin/env python3
from novncbot import NoVNCbot

console_url = "<noVNC URL>"
bot = NoVNCbot()
bot.connect(console_url)

# Add args to the default entry
bot.sendKeys(Keys.TAB)
bot.sendKeys(" biosdevname=1")
bot.sendKeys(Keys.ENTER)

bot.disconnect()
```
