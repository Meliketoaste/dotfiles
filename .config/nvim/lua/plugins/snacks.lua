return {
  "snacks.nvim",

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
  opts = {
    animate = {
      -- enabled = 0,
    },
    indent = {
      chunk = { enabled = true },
      enabled = false,
    },
    input = { enabled = true },
    notifier = { enabled = true },
    scope = { enabled = true },
    scroll = { enabled = false },
    statuscolumn = { enabled = true },

    quickfile = { enabled = false },
    toggle = { map = LazyVim.safe_keymap_set },
    words = { enabled = true },
  },
}
