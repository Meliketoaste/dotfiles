return {
  { "nvim-neo-tree/neo-tree.nvim", enabled = false },
  { "folke/flash.nvim", enabled = false },
  -- { "folke/noice.nvim", enabled = false },
  -- {"Saghen/blink.cmp", enabled = fasle}

  -- {
  --   "gbprod/stay-in-place.nvim",
  --   config = function()
  --     require("stay-in-place").setup({
  --       -- your configuration comes here
  --       -- or leave it empty to use the default settings
  --       -- refer to the configuration section below
  --     })
  --   end,
  -- },
  {
    "snacks.nvim",
    opts = {

      animate = {
        enabled = false,
      },
      indent = {
        chunk = { enabled = true },
      },
      input = { enabled = true },
      notifier = { enabled = true },
      scope = { enabled = true },
      scroll = { enabled = false },
      statuscolumn = { enabled = true },

      quickfile = { enabled = true },
      toggle = { map = LazyVim.safe_keymap_set },
      terminal = { enabled = false },
      words = { enabled = true },
    },
    keys = {
      {
        "<leader>n",
        function()
          Snacks.notifier.show_history()
        end,
        desc = "Notification History",
      },
      {
        "<leader>un",
        function()
          Snacks.notifier.hide()
        end,
        desc = "Dismiss All Notifications",
      },
      {
        "<leader>Z",
        function()
          Snacks.zen()
        end,
        desc = "[Z]en Mode",
      },
    },
  },
  {
    "echasnovski/mini.pairs",
    enabled = false,
    event = "VeryLazy",
    opts = {},
  },
}
