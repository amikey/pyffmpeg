from subprocess import Popen, PIPE


# we open the child process here
cmds = ['/usr/local/bin/ffmpeg', '-colors']
p = Popen(cmds, stdin=PIPE, stdout=PIPE,
          stderr=PIPE)


# ffmpeg passes some output to stdout, so we
# because it is considered as normal output,
# output which is not live, does not result
# in errors
def read_output():
    line = ''
    new_lines = ['\n', '\n\r', '\r']
    while True:
        chunk = p.stdout.read(1)
        line += chunk
        if chunk in new_lines:
            yield line  # generator
            line = ''

        if p.poll() is not None:
            break

# read lines from generator and
# print them to output
for line in read_output():
    print(line)
