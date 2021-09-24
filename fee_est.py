import json
import time
import subprocess


def bcli(*args):
    return subprocess.run(
        ["bitcoin-cli", *args], check=True, capture_output=True
    ).stdout.decode("utf-8")


def blockcount():
    return int(bcli("getblockcount"))


def estsmartfee():
    return [
        json.loads(bcli("estimatesmartfee", str(target)))["feerate"]
        for target in [2, 4, 8, 32, 144]
    ]


def write_estimates(height, estimates):
    with open("fee_est_out.csv", "a") as f:
        line = f"{height},{','.join(str(e) for e in estimates)}\n"
        f.write(line)


if __name__ == "__main__":
    height = blockcount()
    estimates = estsmartfee()
    write_estimates(height, estimates)
    print(f"Started at {height} with {estimates}")

    while True:
        count = blockcount()
        if count > height:
            height = count
            estimates = estsmartfee()
            write_estimates(height, estimates)
            print(f"Updated at {height} with {estimates}")

        time.sleep(300)
