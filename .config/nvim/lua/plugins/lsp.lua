return {

  {
    "neovim/nvim-lspconfig",

    config = function()
      local lspconfig = require("lspconfig")
      local configs = require("lspconfig.configs")

      -- Configure it
      configs.blade = {
        default_config = {
          -- Path to the executable: laravel-dev-generators
          cmd = { "laravel-dev-tools", "lsp" },
          filetypes = { "blade" },
          root_dir = function(fname)
            return lspconfig.util.find_git_ancestor(fname)
          end,
          settings = {},
        },
      }
      -- Set it up
      lspconfig.blade.setup({
        -- Capabilities is specific to my setup.
        capabilities = capabilities,
      })
    end,
    opts = {
      setup = {
        godot = function(_, opts)
          local lspconfig = require("lspconfig")
          lspconfig.gdscript.setup({})
          local dap = require("dap")
          dap.adapters.godot = {
            type = "server",
            host = "127.0.0.1",
            port = 6006,
          }
          dap.configurations.gdscript = {
            {
              type = "godot",
              request = "launch",
              name = "Launch scene",
              project = "${workspaceFolder}",
              launch_scene = true,
            },
          }
        end,
      },
    },
  },

  {
    "habamax/vim-godot",
    ft = "gdscript",
    keys = {
      { "<F4>", "<cmd>:GodotRunLast<cr>", ft = "gdscript" },
      { "<F5>", "<cmd>:GodotRun<cr>", ft = "gdscript" },
      { "<F6>", "<cmd>:GodotRunCurrent<cr>", ft = "gdscript" },
      { "<F7>", "<cmd>:GodotRunFZF<cr>", ft = "gdscript" },
    },
    config = function()
      vim.g.godot_executable = "/usr/bin/env godot"
    end,
  },

  -- require("lspconfig")["gdscript"].setup({
  --   name = "godot",
  --   cmd = vim.lsp.rpc.connect("127.0.0.1", 6005),
  -- }),
}
