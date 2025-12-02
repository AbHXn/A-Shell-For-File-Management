A lightweight, custom DSL (Domain Specific Language) for managing and executing filesystem operations in Python. It supports creating, copying, moving, deleting files and folders, listing directory contents, and accepting user input with a small, scriptable command language.

---

## Features

* **Custom DSL commands** for filesystem operations.
* Execute scripts with expressions (`{}`) and lists (`[]`).
* Supports regex-based file matching.
* Handles both files and folders.
* Interactive input mode for writing files.
* Colorful console output using `termcolor`.
* Cross-platform support (Windows, Linux).

---

## Supported Commands

| Symbol | Action                                |
| ------ | ------------------------------------- |
| `+`    | Create file or folder                 |
| `-`    | Remove file or folder                 |
| `+=`   | Copy file or folder                   |
| `-=`   | Move (cut) file or folder             |
| `*`    | Change folder / display file contents |
| `#`    | Input content to a file               |
| `{}`   | Expression / regex match              |
| `[]`   | List of files or folders              |
| `!`    | List contents of folder               |
| `"`    | Quoted string                         |

---

## Usage

1. **Run the script:**

```bash
python Fshell.py
```

2. **Interactive command prompt:**

```
2025-12-02::$ [command]
```

3. **Example commands:**

* Read all `.txt` files in current directory:

```
{.txt} !
```

* Create a folder `new_folder`:

```
+ new_folder/
```

* Move a file `file1.txt` to `backup/`:

```
file1.txt -= backup/
```

* Copy multiple files using a list:

```
[file1.txt file2.txt] += backup/
```

* Input content into a file:

```
# new_file.txt
```

---

## Notes

* File operations are **destructive** — use caution with remove or move commands.
* Regex patterns are applied to filenames for filtering.
* Nested lists and expressions are supported but complex scripts may require careful formatting.
* Works best in a dedicated project folder to avoid accidental file changes.

---

## Requirements

* Python 3.8+
* [termcolor](https://pypi.org/project/termcolor/) for colored output

Install dependencies:

```bash
pip install termcolor
```

---

## Limitations

* No sandboxing for destructive commands — files can be overwritten or deleted.
* Global working directory changes (`chdir`) can affect the process.
* Parser is basic and may fail with malformed expressions or deeply nested structures.
* Regex patterns should be simple to avoid performance issues.

---

## License

This project is provided as-is, for educational and prototyping purposes. Use at your own risk.

---

Would you like me to also **add a small diagram showing command flow and handler classes**? It will make the README more visual and easier to understand.
