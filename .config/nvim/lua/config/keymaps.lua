-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

vim.keymap.set("n", "<leader>fT", "<Cmd>!ls<CR>", { desc = "Terminal (cwd)" })
vim.keymap.set("n", "<leader>ft", "<Cmd>!echo unset for now<CR>", { desc = "Terminal (cwd)" })
