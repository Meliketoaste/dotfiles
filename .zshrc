# Stolen from dreamsofcode

# Set the GPG_TTY to be the same as the TTY, either via the env var
# or via the tty command.
if [ -n "$TTY" ]; then
  export GPG_TTY=$(tty)
else
  export GPG_TTY="$TTY"
fi

export EDITOR=nvim

# SSH_AUTH_SOCK set to GPG to enable using gpgagent as the ssh agent.
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
gpgconf --launch gpg-agent

# Set the directory we want to store zinit and plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"

# Download Zinit, if it's not there yet
if [ ! -d "$ZINIT_HOME" ]; then
   mkdir -p "$(dirname $ZINIT_HOME)"
   git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
fi

# Source/Load zinit
source "${ZINIT_HOME}/zinit.zsh"

# Add in zsh plugins
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-completions
zinit light zsh-users/zsh-autosuggestions
zinit light Aloxaf/fzf-tab

# Load starship theme
# line 1: `starship` binary as command, from github release
# line 2: starship setup at clone(create init.zsh, completion)
# line 3: pull behavior same as clone, source init.zsh
zinit ice as"command" from"gh-r" \
          atclone"./starship init zsh > init.zsh; ./starship completions zsh > _starship" \
          atpull"%atclone" src"init.zsh"
zinit light starship/starship

# Add in snippets
zinit snippet OMZP::git
zinit snippet OMZP::archlinux

# Load completions
autoload -Uz compinit && compinit

zinit cdreplay -q

# Keybindings
bindkey -e
bindkey '^p' history-search-backward
bindkey '^n' history-search-forward
bindkey '^[w' kill-region

zle_highlight+=(paste:none)

# History
HISTSIZE=5000
HISTFILE=~/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups


bindkey -v
export KEYTIMEOUT=1

function zle-keymap-select {
  if [[ ''${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[2 q'
  elif [[ ''${KEYMAP} == main ]] ||
       [[ ''${KEYMAP} == viins ]] ||
       [[ ''${KEYMAP} = "" ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
zle-line-init() {
  zle -K viins
  echo -ne '\e[6 q'
}
zle -N zle-line-init
echo -ne '\e[6 q' # use beam shape cursor on startup
preexec() { echo -ne '\e[6 q' ;} # use beam shape cursor for each new prompt


# Completion styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*:descriptions' format '[%d]'# set list-colors to enable filename colorizing
zstyle ':completion:*' list-colors ''${(s.:.)LS_COLORS}
zstyle ':completion:*' menu no

zstyle ':fzf-tab:*' fzf-command ftb-tmux-popup



# Aliases
alias ls='ls --color'
#alias vim='nvim'
alias n='nvim'
alias cd='z'

# Shell integrations
eval "$(fzf --zsh)"
eval "$(zoxide init zsh)"
#eval "$(zoxide init --cmd cd zsh)"

. "$HOME/.atuin/bin/env"

eval "$(atuin init zsh)"

export XDG_DATA_HOME="$HOME/.local/share"

export ODIN_ROOT="/home/main/Odin"

export PATH=$PATH:/home/main/Downloads/laravel-dev-tools

# pnpm
export PNPM_HOME="/home/main/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end
