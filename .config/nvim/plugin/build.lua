local user_input = "" -- Store the user input globally

-- Set the command with <leader>cs

-- vim.keymap.set("n", "<leader>cb", function()
--   ---@module "snacks"
--   ---@diagnostic disable-next-line: missing-fields
--   require("snacks.input").input({
--     prompt = "Set command (e.g., !odin run .): ",
--     default = user_input, -- Default to the previous value
--   }, function(value)
--     if value then
--       user_input = value -- Store the input
--       print("Command set to: " .. user_input)
--     end
--   end)
-- end)
--
-- -- Run the set command with <leader>r
-- vim.keymap.set("n", "<leader>r", function()
--   if user_input == "" then
--     print("No command set yet. Use <leader>cs to set it.")
--     return
--   end
--
--   -- Execute the command like it was typed in the command line (using <Cmd>!)
--   vim.cmd("!" .. user_input) -- This executes the user_input as a command in Neovim
-- end)
