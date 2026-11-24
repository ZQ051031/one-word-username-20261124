"""One Word, One Username, One Reward — entry program.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt. Standard library only.

Revision note: the entry is the bare username "zq051031", exactly 8 bytes.
No "@" prefix — the rules ask for the username itself, one word, with no
gloss tacked on, and "@" is display chrome, not part of the handle. No
trailing newline — the file must be the word alone. Binary write is used
so the output is byte-exact on any platform.
"""

import os

USERNAME = "zq051031"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(USERNAME.encode("utf-8"))


if __name__ == "__main__":
    main()
