return {
  "saghen/blink.cmp",

  -- optional: provides snippets for the snippet source
  dependencies = {
    "rafamadriz/friendly-snippets",
  },

  -- use a release tag to download pre-built binaries
  version = "*",
  -- AND/OR build from source, requires nightly: https://rust-lang.github.io/rustup/concepts/channels.html#working-with-nightly-rust
  -- build = 'cargo build --release',
  -- If you use nix, you can build from source using latest nightly rust with:
  -- build = 'nix run .#build-plugin',
  opts = {
    keymap = {
      preset = "default",
    },
    -- 'default' for mappings similar to built-in completion
    -- 'super-tab' for mappings similar to vscode (tab to accept, arrow keys to navigate)
    -- 'enter' for mappings similar to 'super-tab' but with 'enter' to accept
    -- See the full "keymap" documentation for information on defining your own keymap.

    -- Default list of enabled providers defined so that you can extend it
    -- elsewhere in your config, without redefining it, due to `opts_extend`
    sources = {

      default = { "lsp", "path", "snippets", "buffer" },
      cmdline = function()
        local type = vim.fn.getcmdtype()
        if type == "/" or type == "?" then
          return { "buffer" }
        end
        --                                           -- Commands
        if type == ":" then
          return { "cmdline", "path" }
        end
        return {}
      end,
      -- cmdline = { "buffer", "cmdline" },
    },
  },
}
