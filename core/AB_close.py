import subprocess
import re

# Process name to search
process_name = "LM Studio.exe"

try:
    # Get the list of LM Studio processes with PID and WorkingSetSize (memory in bytes)
    result = subprocess.check_output(
        f'wmic process where "Name=\'{process_name}\'" get ProcessId,WorkingSetSize',
        shell=True,
        text=True
    )

    lines = result.strip().splitlines()
    max_memory = 0
    target_pid = None

    for line in lines[1:]:  # Skip header
        parts = re.findall(r'\d+', line)
        if len(parts) == 2:
            pid, mem = map(int, parts)
            if mem > max_memory:
                max_memory = mem
                target_pid = pid

    if target_pid:
        # Terminate the process and suppress all output
        subprocess.run(
            ["taskkill", "/PID", str(target_pid), "/F"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

except subprocess.CalledProcessError:
    # Suppress error output silently
    pass

except Exception:
    # Suppress any other exceptions silently
    pass
