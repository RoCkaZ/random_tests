import serial
import time


def run_test(set_timeout):
    for b in range(cycle_length):
        if set_timeout:
            port.timeout = 1
        port.write(b)


def s(num_str):
    return '' if num_str % 10 == 1 and num_str % 100 != 11 else 's'


with_timeout = []
without_timeout = []

# TODO: Change these to your needs, or at least the port name
com_port_name = 'COM12'
cycle_length = 100
cycle_count = 3


print(f'Opening port {com_port_name}...', end='')
try:
    port = serial.Serial(com_port_name, 115200, timeout=1)
except serial.serialutil.SerialException as e:
    print(f'ERROR:\n{str(e)}')
    exit()

if not port.isOpen():
    print(f'\nSomething went wrong, terminating.')
    exit()

print(f' success! \nRunning {cycle_count} cycle{s(cycle_count)}, each with {cycle_length} write() operation{s(cycle_length)}:')

for cycle in range(cycle_count):
    start_time = time.monotonic()
    run_test(False)
    without_timeout.append(time.monotonic() - start_time)
    start_time = time.monotonic()
    run_test(True)
    with_timeout.append(time.monotonic() - start_time)
    print(f'  .. cycle #{(cycle+1):03d}: {(without_timeout[-1]):.3f} secs vs. {(with_timeout[-1]):.3f} secs')

without_timeout = sum(without_timeout) / len(without_timeout)
with_timeout = sum(with_timeout) / len(with_timeout)

print(f'Total duration WITHOUT setting timeout: {without_timeout:.3f} seconds')
print(f'Total duration WITH setting timeout: {with_timeout:.3f} seconds ({(with_timeout/without_timeout):.1f}x slower)')
