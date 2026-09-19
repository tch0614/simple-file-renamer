#!/usr/bin/env python3
"""Simple batch file renamer CLI tool.

Usage:
    python simple_file_renamer.py --path ./docs --prefix processed_ --dry-run
"""
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Batch rename files in a folder")
    parser.add_argument("--path", type=str, default=".", help="Target directory")
    parser.add_argument("--prefix", type=str, default="", help="Add prefix to filename")
    parser.add_argument("--suffix", type=str, default="", help="Add suffix to filename")
    parser.add_argument("--pattern", type=str, default="*", help="File filter pattern")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes only")
    args = parser.parse_args()

    folder = os.path.abspath(args.path)
    print(f"Scanning folder: {folder}")
    print(f"Filter pattern : {args.pattern}")
    print(f"Prefix         : {args.prefix}")
    print(f"Suffix         : {args.suffix}")
    print(f"Dry run mode   : {args.dry_run}")

    count = 0
    for name in sorted(os.listdir(folder)):
        src = os.path.join(folder, name)
        if not os.path.isfile(src):
            continue
        stem, ext = os.path.splitext(name)
        new_name = f"{args.prefix}{stem}{args.suffix}{ext}"
        dst = os.path.join(folder, new_name)
        print(f"{name}  ->  {new_name}")
        count += 1
        if not args.dry_run and src != dst:
            os.rename(src, dst)

    print(f"Done. {count} file(s) processed.")

if __name__ == "__main__":
    main()
