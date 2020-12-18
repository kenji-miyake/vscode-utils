# vscode-utils

Utils for vscode

## [repos2workspace.py](https://raw.githubusercontent.com/kenji-miyake/vscode-utils/main/repos2workspace.py)

### Overview

This generates a VSCode workspace file(`.code-workspace`) from colcon workspace file(`.repos`).

### Prerequisites

- Python 3.6+
- pyyaml

#### Ubuntu

```sh
sudo apt install python3
pip3 install pyyaml
```

### Usage

```sh
# Create .code-workspace
wget -P /tmp https://raw.githubusercontent.com/kenji-miyake/vscode-utils/main/repos2workspace.py
python3 /tmp/repos2workspace.py YOUR_COLCON_WORKSPACE/YOUR_REPOS_FILE.repos

# Open .code-workspace with VSCode
code YOUR_COLCON_WORKSPACE.code-workspace
```

## [c_cpp_properties.json](https://raw.githubusercontent.com/kenji-miyake/vscode-utils/main/c_cpp_properties.json)

### Overview

This is a recommended config of [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) for colcon users.

### Usage

```sh
cd YOUR_COLCON_WORKSPACE/.vscode
mv c_cpp_properties.json c_cpp_properties.json.old
wget https://raw.githubusercontent.com/kenji-miyake/vscode-utils/main/c_cpp_properties.json -O c_cpp_properties.json
```
