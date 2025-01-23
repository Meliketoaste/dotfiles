-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
--
-- Add any additional autocmds here
-- with `vim.api.nvim_create_autocmd`
--
-- Or remove existing autocmds by their group name (which is prefixed with `lazyvim_` for the defaults)
-- e.g. vim.api.nvim_del_augroup_by_name("lazyvim_wrap_spell")
vim.wo.statuscolumn = ""
--
-- local projectFile = vim.fn.getcwd() .. "/project.godot"
-- if projectFile then
--   vim.fn.serverstart("./godothost")
-- local lspconfig = require("lspconfig")
-- local configs = require("lspconfig.configs")
--
-- -- Configure it
-- configs.blade = {
--   default_config = {
--     -- Path to the executable: laravel-dev-generators
--     cmd = { "laravel-dev-generators", "lsp" },
--     filetypes = { "blade" },
--     root_dir = function(fname)
--       return lspconfig.util.find_git_ancestor(fname)
--     end,
--     settings = {},
--   },
-- }
-- -- Set it up
-- lspconfig.blade.setup({
--   -- Capabilities is specific to my setup.
--   capabilities = capabilities,
-- })
