import argparse
import subprocess

from dotenv import load_dotenv
from os import system, getenv


def run_mongosh_command(uri: str, file_path: str, clear_flag: bool) -> None:
    cmd = ["mongosh", uri, "--quiet"]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    commands = ""
    try:
        while True:
            with open(file_path) as f:
                commands = f.read()
                commands = commands.split(";")

            for cmd in commands:
                cmd = cmd.strip()
                if not cmd or cmd.startswith("//"):
                    continue
                print(LIGHT_BLUE_COLOR_CODE + cmd + RESET_COLOR_CODE)
                cmd = cmd + "\nprint('===END===')"
                process.stdin.write(cmd + "\n")
                process.stdin.flush()

                while True:
                    output_line = process.stdout.readline()
                    if "===END===" in output_line:
                        print()
                        break
                    if output_line.startswith("\n"):
                        output_line = output_line[1:]
                    if output_line.endswith("\n"):
                        output_line = output_line[: len(output_line)]
                    print(output_line, end="")
            if input() == "q":
                exit(0)
            if clear_flag:
                system("cls")

    except Exception as err:
        print(f"{RED_COLOR_CODE}Error: {err}{RESET_COLOR_CODE}")
    finally:
        process.stdin.close()
        process.wait()


RED_COLOR_CODE = "\033[31m"
LIGHT_BLUE_COLOR_CODE = "\033[94m"
RESET_COLOR_CODE = "\033[0m"

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Mongo Playground, Run & Test MongoDB Shell Commands from a file with Live Reload."
    )

    parser.add_argument(
        "--clusterlink",
        type=str,
        default=getenv("CLUSTER_LINK"),
        help="MongoDB Cluster Link(mongodb+srv://user:pass@cluster0.xxxxxxx.mongodb.net)",
    )
    parser.add_argument(
        "--dbname",
        type=str,
        default=getenv("DB_NAME"),
        help="DataBase Name(Practice_DB)",
    )
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="MongoDB Query Script File Path",
    )
    parser.add_argument(
        "--clear",
        action="store_true",
        help="Clears Terminal before each re-run",
    )

    args = parser.parse_args()
    if args.clear:
        system("cls")

    uri = f"{args.clusterlink}/{args.dbname}?retryWrites=true&w=majority"
    run_mongosh_command(uri, args.file, args.clear)
