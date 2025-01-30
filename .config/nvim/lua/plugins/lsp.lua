local prettier = { "prettierd", "prettier", stop_after_first = true }
return {

  {
    "neovim/nvim-lspconfig",

    -- config = function()
    --   local lspconfig = require("lspconfig")
    --   local configs = require("lspconfig.configs")
    --
    --   -- -- Configure it
    --   -- configs.blade = {
    --   --   default_config = {
    --   --     -- Path to the executable: laravel-dev-generators
    --   --     cmd = { "laravel-dev-tools", "lsp" },
    --   --     filetypes = { "blade" },
    --   --     root_dir = function(fname)
    --   --       return lspconfig.util.find_git_ancestor(fname)
    --   --     end,
    --   --     settings = {},
    --   --   },
    --   -- }
    --   -- -- Set it up
    --   -- lspconfig.blade.setup({
    --   --   -- Capabilities is specific to my setup.
    --   --   capabilities = capabilities,
    --   -- })
    -- end,

    opts = {

      servers = {

        gdscript = {
          name = "godot",
          cmd = vim.lsp.rpc.connect("127.0.0.1", 6005),
        },
        ols = {

          name = "odin",
          cmd = { "/home/main/ols/ols" },
          -- root_dir = function(path)
          --   local lspUtil = require("lspconfig.util")
          --   local root
          --   root = lspUtil.root_pattern("ols.json", ".git")(path)
          --   root = root
          --     or (function(p)
          --       return (vim.fs.dirname(p or vim.fn.expand("%:p"))) .. "/"
          --     end)(path)
          --   return root
          -- end,
          -- settings = {
          --   odin = {
          --     completion_support_md = true,
          --     hover_support_md = true,
          --     signature_offset_support = true,
          --     collections = {},
          --     -- running=true,
          --     tabs = false,
          --     newline_limit = 2,
          --     verbose = true,
          --     enable_format = false,
          --     enable_hover = true,
          --     enable_symantic_tokens = true,
          --     enable_document_symbols = true,
          --     enable_inlay_hints = true,
          --     enable_procedure_context = true,
          --     enable_snippets = true,
          --     enable_references = true,
          --     enable_rename = true,
          --     enable_label_details = true,
          --     enable_std_references = true,
          --     enable_import_fixer = true,
          --     disable_parser_errors = true,
          --     thread_count = 0,
          --     file_log = true,
          --     -- odin_command = "",
          --     checker_args = "",
          --   },
          -- },
          filetypes = { "odin" },
          -- single_file_support = false,
          -- autostart = true,
        },
      },
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

  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed = {
        "prettierd",
      },
    },
  },
  {
    "stevearc/conform.nvim",
    optional = true,
    opts = {
      formatters_by_ft = {
        ["javascript"] = prettier,
        ["javascriptreact"] = prettier,
        ["typescript"] = prettier,
        ["typescriptreact"] = prettier,
        ["vue"] = prettier,
        ["css"] = prettier,
        ["scss"] = prettier,
        ["less"] = prettier,
        ["html"] = prettier,
        ["json"] = prettier,
        ["jsonc"] = prettier,
        ["yaml"] = prettier,
        ["markdown"] = prettier,
        ["markdown.mdx"] = prettier,
        ["graphql"] = prettier,
        -- ["svelte"] = prettier,
        ["handlebars"] = prettier,
      },
    },
  },
  {
    "luckasRanarison/nvim-devdocs",
    optional = true,
    opts = {
      ensure_installed = {
        "prettier",
      },
    },
  },
  -- require("lspconfig")["gdscript"].setup({
  --   name = "godot",
  --   cmd = vim.lsp.rpc.connect("127.0.0.1", 6005),
  -- }),
}
