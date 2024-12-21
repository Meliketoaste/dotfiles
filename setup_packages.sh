#!/usr/bin/env bash

export PATH="$HOME/.cargo/bin$PATH"
# Check if rustup is installed

if ! command -v  rustup &> /dev/null; then

	echo "Rustup is not installed. Installing rustup..."

	curl --proto  '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


	source "$HOME/.cargo/env"
else
	echo "Rustup is already installed."
fi


if ! command metapac -v &> /dev/null; then
	echo "Metapac is not installed. Installing metapac using cargo"
        cargo install metapac

fi
