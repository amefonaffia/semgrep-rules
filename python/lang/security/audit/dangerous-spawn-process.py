import os
import shlex
from somewhere import something

# ok:dangerous-spawn-process
os.spawnlp(os.P_WAIT, "ls")

# ok:dangerous-spawn-process
os.spawnlpe(os.P_WAIT, "ls")

# ok:dangerous-spawn-process
os.spawnv(os.P_WAIT, "/bin/ls")

# ok:dangerous-spawn-process
os.spawnve(os.P_WAIT, "/bin/ls", ["-a"], os.environ)

# ruleid:dangerous-spawn-process
os.spawnlp(os.P_WAIT, something())

# ruleid:dangerous-spawn-process
os.spawnlpe(os.P_WAIT, something())

# ruleid:dangerous-spawn-process
os.spawnv(os.P_WAIT, something())

# ruleid:dangerous-spawn-process
os.spawnve(os.P_WAIT, something(), ["-a"], os.environ)

# ruleid:dangerous-spawn-process
os.spawnve(os.P_WAIT, "/bin/bash", ["-c", something()], os.environ)

# ruleid:dangerous-spawn-process
os.spawnl(os.P_WAIT, "/bin/bash", "-c", something())

def run_payload(shell_command: str) -> None:
    args = shlex.split(shell_command)
    path = args[0]
    # ruleid:dangerous-spawn-process
    pid = os.posix_spawn(path, args, os.environ)
    os.waitpid(pid, 0)
