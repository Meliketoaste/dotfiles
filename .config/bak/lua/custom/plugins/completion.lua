return {
  {
    'saghen/blink.cmp',
    dependencies = 'rafamadriz/friendly-snippets',

    version = 'v0.*',

    opts = {
      keymap = { preset = 'default' },

      appearance = {

        use_nvim_cmp_as_default = true,
        nerd_font_variant = 'mono',
      },
      -- sources = { cmdline = {} }, -- Disable cmdline for now (buggy)
      completion = {
        -- list = { selection = "manual" },
        -- list = { selection = 'auto_insert' },
        -- accept = {
        --   create_undo_point = true,
        --   auto_brackets = { enabled = true },
        -- },
        -- menu = {
        --   draw = {
        --     treesitter = { 'lsp' },
        --   },
        -- },
        -- documentation = {
        --   auto_show = true,
        --   auto_show_delay_ms = 100,
        -- },
        ghost_text = { enabled = false },
      },

      signature = { enabled = true },
    },
  },
}
