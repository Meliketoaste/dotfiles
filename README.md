# My non NixOS dotfiles
NixOS if really awesome I've used it more than most. But i want sometimes just be able to `make install` stuff or whatever. And It would be beneficial to not just know one niche distro.

## Trying to be distro agnostic
The idea here is using `metapac` and declaring all the packages I need. And all i need i just need to declare the necessary packages for each distro i need to use. And i will have one group for each distro.

# Installation
`./setup_packages.sh` should setup `Metapac` hopefully and then you just do `metapac sync` or whatever.

also using stow. Tried chezmoi but it didnt really benefit me much.
