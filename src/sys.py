import subprocess

class Sys:
  def __init__(self):
    self.spinup = "qemu -m 2048 -hda ./alpine-first.img -m 1g"

  def spinInstance(self):
    retval = subprocess.run(["sudo chmod 777 ./file.img"], shell=True).returncode
    if retval == 0:
      retval = subprocess.run(["qemu-system-x86_64 -nographic -display curses -hda ./file.img -m 1G -vnc 0.0.0.0:0"], shell=True).returncode
    return retval
