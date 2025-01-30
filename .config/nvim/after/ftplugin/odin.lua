local set = vim.opt_local

set.shiftwidth = 4
set.tabstop = 4
set.softtabstop = 4
set.expandtab = false
set.autoindent = false
set.smartindent = false
set.cindent = false

-- Auto-indent Odin files before saving
-- vim.api.nvim_create_autocmd("BufWritePre", {
--   pattern = "*.odin", -- Trigger only for Odin files
--   callback = function()
--     -- Function to indent the entire file without polluting the jump list
--     local current_line = vim.fn.line(".")
--     local current_col = vim.fn.col(".")
--
--     -- Indent the entire file without moving the cursor
--     vim.api.nvim_command("keepjumps normal! gg=G")
--
--     -- Restore the cursor position
--     vim.fn.cursor(current_line, current_col)
--   end,
-- })
