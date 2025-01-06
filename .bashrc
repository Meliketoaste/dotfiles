#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '


export XDG_CONFIG_HOME=$HOME/.config
export PATH=$PATH:/usr/local/bin:/usr/bin

# Wayland Fix
# export QT_QPA_PLATFORM="wayland"
#  
# export XDG_CURRENT_DESKTOP=river
# export XDG_SESSION_DESKTOP=river
# export XDG_CURRENT_SESION_TYPE=wayland
# export GDK_BACKEND="wayland,x11"
# export MOZ_ENABLE_WAYLAND=1
#
#[[ -f ~/.bash-preexec.sh ]] && source ~/.bash-preexec.sh
#eval "$(atuin init bash)"
