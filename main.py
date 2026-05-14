import os
import hashlib
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_FILE = os.path.expanduser("~/.integrity_shield_snapshot.json")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\n𝙋𝙧𝙚𝙨𝙨 𝙀𝙣𝙩𝙚𝙧 𝙏𝙤 𝘾𝙤𝙣𝙩𝙞𝙣𝙪𝙚...")

def hash_file(path):
    sha = hashlib.sha256()

    try:
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                sha.update(chunk)
        return sha.hexdigest()
    except PermissionError:
        print(f"[SKIP] Permission denied:{path}")
        return None

    except Exception as e:
        print(f"[ERROR] {path}: {e}")
        return None

def scan_folder(folder):
    data = {}

    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)

            file_hash = hash_file(path)

            if file_hash is not None:
                data[path] = file_hash

    return data

def save_snapshot(folder):
    data = scan_folder(folder)

    with open(SNAPSHOT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("𝙎𝙣𝙖𝙥𝙨𝙝𝙤𝙩 𝙎𝙖𝙫𝙚𝙙 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙏𝙤: ~/.integrity_shield_snapshot.json")

def verify_snapshot(folder):
    with open(SNAPSHOT_FILE, "r") as f:
        old = json.load(f)

    new = scan_folder(folder)

    changes_found = False

    for file in old:
        if file not in new:
            print("❌𝙈𝙞𝙨𝙨𝙞𝙣𝙜:", file)
            changes_found = True

        elif old[file] != new[file]:
            print("⚠️ 𝙈𝙤𝙙𝙞𝙛𝙞𝙚𝙙:", file)
            changes_found = True

    for file in new:
        if file not in old:
            print("⚠️ 𝙉𝙚𝙬 𝙁𝙞𝙡𝙚:", file)
            changes_found = True

    if not changes_found:
        print("𝙉𝙤 𝘾𝙝𝙖𝙣𝙜𝙚𝙨 𝘿𝙚𝙩𝙚𝙘𝙩𝙚𝙙. 𝙁𝙞𝙡𝙚 𝙄𝙣𝙩𝙚𝙜𝙧𝙞𝙩𝙮 𝙑𝙚𝙧𝙞𝙛𝙞𝙚𝙙.✅")
def show_menu():
    print("  ▄▄▄▄▄▄                                          ▄▄▄▄▄                 ▄▄               ")
    print(" █▀ ██         █▄                     █▄         ██▀▀▀▀█▄ █▄             ██    █▄        ")
    print("    ██   ▄    ▄██▄         ▄▄ ▄    ▀▀▄██▄        ▀██▄  ▄▀ ██    ▀▀       ██    ██        ")
    print("    ██   ████▄ ██ ▄█▀█▄ ▄████ ████▄██ ██ ██ ██     ▀██▄▄  ████▄ ██ ▄█▀█▄ ██ ▄████        ")
    print("    ██   ██ ██ ██ ██▄█▀ ██ ██ ██   ██ ██ ██▄██   ▄   ▀██▄ ██ ██ ██ ██▄█▀ ██ ██ ██        ")
    print("  ▄▄██▄▄▄██ ▀█▄██▄▀█▄▄▄▄▀████▄█▀  ▄██▄██▄▄▀██▀   ▀██████▀▄██ ██▄██▄▀█▄▄▄▄██▄█▀███ ██     ")
    print("                           ██              ██                                            ")
    print("                         ▀▀▀             ▀▀▀                                             ")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   ")
    print("                                                                                         ")
    print(" [𝟭] 𝙎𝙖𝙫𝙚 𝙎𝙣𝙖𝙥𝙨𝙝𝙤𝙩                                                                       ")
    print(" [𝟮] 𝘾𝙝𝙚𝙘𝙠 𝙎𝙣𝙖𝙥𝙨𝙝𝙤𝙩                                                                      ")
    print(" [𝟯] 𝙀𝙭𝙞𝙩                                                                                ")


def get_choice():
    return input("\n𝘾𝙝𝙤𝙤𝙨𝙚 𝙊𝙥𝙩𝙞𝙤𝙣: ")


def main():
    while True:
        clear()
        show_menu()
        choice = get_choice()

        if choice == "1":
            folder = os.path.abspath(os.path.expanduser(input("Folder Path: ").strip()))
            print("[DEBUG PATH]:", repr(folder))
            save_snapshot(folder)
            pause()
            clear()

        elif choice == "2":
            folder = os.path.abspath(os.path.expanduser(input("Folder Path: ").strip()))
            verify_snapshot(folder)
            pause()
            clear()
 
        elif choice == "3":
            print("𝙏𝙝𝙖𝙣𝙠𝙨 𝙁𝙤𝙧 𝙐𝙨𝙞𝙣𝙜 𝙄𝙣𝙩𝙚𝙜𝙧𝙞𝙩𝙮 𝙎𝙝𝙞𝙚𝙡𝙙, 𝙃𝙖𝙫𝙚 𝘼 𝙂𝙧𝙚𝙖𝙩 𝘿𝙖𝙮!")
            break

        else:
           print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙, 𝙀𝙣𝙩𝙚𝙧 𝙑𝙖𝙡𝙞𝙙 𝙉𝙪𝙢𝙗𝙚𝙧 1-3")

if __name__ == "__main__":
    main()
