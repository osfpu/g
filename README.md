# g - Goto directories quickly with a record.

## Description
It's boring when switching between different directories, especially with long path. This tool can release you by giving your path a nickname or a number.

![image](https://blog.osfpu.com/images/G_Flow.gif?v=1)

## Requirement
You need install python

## Install
1. Clone the repo:
```
git clone https://github.com/osfpu/g.git
```
2. Add the following in your ~/.bashrc (.zshrc): **ATTENTION : Change path with yours**
```
export G_HOME=path/to/g
```
3. Also add the following in your ~/.bashrc (.zshrc):
```
alias goto=${G_HOME}/g.py
g () {
    if [[ ${1} = -* ]] && [[ ${1} != "--" ]]
    then
        goto ${@}
        return
    fi
    setopt localoptions noautonamedirs
    local output="$(goto ${@})"
    if [[ -d "${output}" ]]
    then
        if [ -t 1 ]
        then
            echo -e "\\033[31m${output}\\033[0m"
        else
            echo -e "${output}"
        fi
        cd "${output}"
    else
        echo "Cannot not found record \`${@}\`. You can use \`g -a ${@}\` to add a record for your current path."
        echo "Try \`g --help\` for more information."
        false
    fi
}
```
4. Reload the change:
```
source ~/.bachrc
```

5. Open a new terminal, enter `g --help` and you can see help information if the installation was successful.

## User Case

1. Goto a directory you want to record. For example `cd /etc`.
2. Add a alias name for your current path. Use `g -a 1` to add alias name "1" to current path.
3. Use `g -l` to view all Record.
4. Use `g 1` whenever you want to goto `/etc`.
5. Use `g -r 1` to delete the record.

## Usage
```
    g [option] [value]
        -h or --help
        -l or --list        List all records.
        -r or --remove      Remove a record by key.
        -a or --add         Add a record to your current path. For example, use
                            `g -a 1` record the current path and you can use
                            `g 1` go back the path next time.
        --clear             Remove all records.
```

## Something You Need Know

1. If you use oh-my-zsh, please comment `plugins=(git)`. If you use git plugin, alias `g` will be in conflict！

2. You can edit `~/path_record_file.json` where all your records saved.

## License

[MIT](https://github.com/osfpu/g/blob/master/LICENSE)
