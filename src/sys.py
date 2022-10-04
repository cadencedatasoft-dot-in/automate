import subprocess
from subprocess import Popen
DETACHED_PROCESS = 0x00000008

class Sys:
  def __init__(self):
    self.spinup = "qemu -m 2048 -hda ./alpine-first.img -m 1g"

  def spinInstanceOld(self):
    retval = subprocess.run(["sudo chmod 777 ./file.img"], shell=True).returncode
    if retval == 0:
      retval = subprocess.run(["qemu-system-x86_64 -nographic -display curses -hda ./file.img -m 1G -vnc 0.0.0.0:0"], shell=True).returncode
    return retval

  def spinInstance(self):
    retval = subprocess.run(["sudo chmod 777 ./file.img"], shell=True).returncode
    if retval == 0:
      cmd = ["qemu-system-x86_64 -hda ./file.img -m 1G -vnc 0.0.0.0:0 -daemonize"]
      p = Popen(
          cmd, shell=False, stdin=None, stdout=None, stderr=None,
          close_fds=True, creationflags=DETACHED_PROCESS )
      if p:
        return 0
    
    return retval