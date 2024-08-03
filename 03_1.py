from pathlib import Path
import shutil
import sys


# if file with the same name exists add index to it's name
def check_name(path: Path, add: int = 0) -> Path:
    origin = path
    if add != 0:
        path = path.with_stem(f"{path.stem}_{str(add)}")
    if path.exists():
        return check_name(origin, add + 1)
    else:
        return path


def sorted_copy(src_path: Path, dest_path: Path) -> None:
    if src_path.is_dir():  # check if dir then go deeper
        for child in src_path.iterdir():
            sorted_copy(child, dest_path)
    else:
        # make new folder from file extention
        file_ext = src_path.suffix.removeprefix(".")  
        new_dir = Path(f"{dest_path}/{file_ext}")
        new_dir.mkdir(parents=True, exist_ok=True)

        # check filename recursively
        new_file = check_name(Path(f"{new_dir}/{src_path.name}")) 

        shutil.copy(src_path, new_file)  # just copy
        print(f"copied from \033[96m{src_path}\x1b[0m to --> \033[93m{new_file}\x1b[0m")


def main():
    args = sys.argv  # parsing args and check them
    if len(args) < 3 or str(args[1]) == "?":
        print(
            "\nUse with 2 arguments \033[96m[source folder] [destination folder]\x1b[0m\n"
        )
        return
    else:
        src_path = Path(args[1])
        dest_path = Path(args[2])

    try:  # try to make new folder and copy files
        dest_path.mkdir(parents=True, exist_ok=True)
        sorted_copy(src_path, dest_path)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
