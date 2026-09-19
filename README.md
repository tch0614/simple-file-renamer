# simple-file-renamer
# simple-file-renamer
A lightweight CLI tool to batch rename local files, support custom prefix/suffix and regex rules.

## Features
- Batch rename files in selected folder
- Add custom prefix and suffix
- Regex pattern support for filename matching
- Dry-run mode to preview changes before applying
- Cross-platform (Windows / macOS / Linux)

## Quick Start
```bash
# install
pip install simple-file-renamer

# example: add prefix "processed_" to all txt files
sfr --path ./docs --prefix processed_ --pattern *.txt --dry-run
```

## Usage
```
sfr [OPTIONS]
Options:
  --path TEXT       Target directory path
  --prefix TEXT     Add prefix to filename
  --suffix TEXT     Add suffix to filename
  --pattern TEXT    File filter pattern
  --dry-run         Preview only, no real modification
```

## Maintainer
Maintained by [tch0614]

## License
MIT License
