#!/bin/sh

#usage: "pull.sh dir1 dir2 ...",if no arg,default to "pull.sh ."

set -e

pull() {
    echo -e "\033[32mpull $1\033[0m"
    cd $1
    git pull || echo -e "\033[31mpull $1 error\033[0m"
    cd - > /dev/null
}

pullDir() {
    dir=`echo $1|xargs`
    #remove / if the last character of dir is /
    if [[ ${dir: -1} == '/' ]]; then
        dir=${dir:0:${#dir}-1}
    fi

    # pull all repos in the dir
    for repo in ${dir}/*/; do
        if [[ -d  ${repo}.git ]]; then
            #statements
            pull ${repo}
        fi
    done
}

if [[ $# -gt 0 ]]; then
    for dir in "$@"
    do
        pullDir $dir
    done
else
    dir=$( dirname "${BASH_SOURCE[0]}" )
    pullDir $dir
fi
