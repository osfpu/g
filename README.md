# g - Goto directories quickly with a record.

## DESCRIPTION

## INSTALL
Clone the repo:
```
git clone https://github.com/osfpu/g.git
```
Add the following in your ~/.bashrc (.zshrc): *ATTENTION : change path with yours*
```
export G_HOME=path/to/g
```
Also add the following in your ~/.bashrc (.zshrc):
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
Reload the change:
```
source ~/.bachrc
```

## USAGE

g -r || --remove [dir name]
g --clear
g -l || --list
g -h || --help

## LICENSE
