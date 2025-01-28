return {
  -- add gruvbox
  { "ellisonleao/gruvbox.nvim" },
  { "rebelot/kanagawa.nvim" },
  {
    "ccxnu/rosebones",
    lazy = false,
    priority = 1000,
    opts = {},
  },
  {
    "vague2k/vague.nvim",
    config = function()
      require("vague").setup({
        -- optional configuration here
      })
    end,
  },
  {
    "rose-pine/neovim",
    name = "rose-pine",
  },

  { "blazkowolf/gruber-darker.nvim" },
  {
    "aktersnurra/no-clown-fiesta.nvim",
  },
  {
    "gmr458/cold.nvim",
  },

  { "datsfilipe/vesper.nvim" },
  -- Using lazy.nvim
  {
    "cdmill/neomodern.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      require("neomodern").setup({
        -- optional configuration here
      })
      -- require("neomodern").load()
    end,
  },

  -- Configure LazyVim to load gruvbox
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "cold",
    },
  },
}
