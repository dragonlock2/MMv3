# Sanity

This lab provides code to test all aspects of your mouse and identify any hardware defects. If at any point in this lab a test is not passed, ask an instructor for help debugging.

1. Upload the contents of [sanity/](../labs/sanity/) to the CircuitPython drive that shows up when you plug your mouse into your computer.
2. Find the associated serial port for your mouse.
    <details>
    <summary>Windows</summary>

    Open up `Device Manager` and check the `Ports (COM & LPT)` dropdown. Your serial (COM) port is one of those. If it's hard to identify, try unplugging and replugging your mouse and see which COM port disappears.

    </details>
    <details>
    <summary>MacOS</summary>

    Run `ls  /dev/tty.*` in Terminal. The correct port is one of those. If it's hard to identify, try unplugging and replugging your mouse and see which port disappears.

    </details>
    <details>
    <summary>Linux</summary>

    Hello there! A fellow power user you are. Your distro may be different, but chances are it's under something like `/dev/ttyACM0`.

    </details>
3. Bring up a serial monitor on that serial port (baud rate doesn't matter). There are many options of software to use, but the following are what I personally use.
    * **Windows** - [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
    * **MacOS** - [SerialTools](https://apps.apple.com/us/app/serialtools/id611021963?mt=12) and [screen](https://en.wikipedia.org/wiki/GNU_Screen)
    * **Linux** - [screen](https://en.wikipedia.org/wiki/GNU_Screen)
4. Follow the instructions printed to the serial monitor. You may have to press CTRL-C and CTRL-D to reset if you don't see anything.
    * IR sensor readings should be 40,000-60,000 without a surface in front of them and under 2,000 with your hand over it.
    * Encoders should be \~217 ticks per revolution.