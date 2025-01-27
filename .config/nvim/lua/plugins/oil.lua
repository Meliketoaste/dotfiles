return {
  "stevearc/oil.nvim",
  dependencies = { "nvim-tree/nvim-web-devicons" },
  keys = {
    {
      "-",
      function()
        require("oil").open()
      end,
      desc = "Open parent directory with oil",
    },

    {
      "<leader>o",
      function()
        require("oil").toggle_float()
      end,
    },
    {
      "<leader>fo",
      function()
        vim.fn.jobstart({ "fd", "--type", "d", "-H", "--ignore", "-E", ".git" }, {
          stdout_buffered = true,
          on_stdout = function(_, data)
            Snacks.picker.select(data, {
              prompt = "Open Directory",
              kind = "dir",
            }, function(dir)
              require("oil").open_float(dir)
            end)

            --- @type snacks.picker.finder.Item[]
            -- local items = {}
            --
            -- for _, dir in ipairs(data) do
            -- 	table.insert(items, {
            -- 		--- @type snacks.picker.finder.Item
            -- 		text = dir,
            -- 	})
            -- end
            --
            -- Snacks.picker.pick({
            -- 	finder = function(opts, filter)
            -- 		return items
            -- 	end,
            -- 	-- cwd = vim.fn.getcwd(),
            -- 	confirm = function(_, item)
            -- 		require("oil").open_float(item.text)
            -- 	end,
            -- 	preview = function()
            -- 		return false
            -- 	end,
            -- })
          end,
        })
      end,
    },
  },
  opts = {

    columns = { "icon" },
    keymaps = {
      ["<C-h>"] = false,
      ["<M-h>"] = "actions.select_split",
    },
    view_options = {
      show_hidden = true,
    },

    -- vim.keymap.set("n", "-", "<CMD>Oil<CR>", { desc = "Open parent directory" })

    -- Open parent directory in floating window
    -- vim.keymap.set("n", "<leader>o", require("oil").toggle_float)
  },
}

-- local items = { "dir1", "dir2", "dir3", "dir4" }
--
--
-- -- Define the items manually
-- ---@type snacks.picker.finder.Item[]
-- local finder_items = {}
-- for idx, item in ipairs(items) do
-- 	local text = tostring(item) -- Just converting the item to string (or format it as needed)
-- 	table.insert(finder_items, {
-- 		formatted = text,
-- 		text = idx .. " " .. text,
-- 		item = item,
-- 		idx = idx,
-- 	})
-- end
--
-- local title = "Select a directory" -- Custom prompt (can be anything)
--
-- -- Calling Snacks.picker directly to display the selection prompt
-- Snacks.picker.pick({
-- 	source = "select",
-- 	items = finder_items,
-- 	main = { current = true },
-- 	format = Snacks.picker.format.ui_select("dir", #items),
-- 	layout = {
-- 		preset = "vscode",
-- 	},
-- 	actions = {
-- 		confirm = function(picker, item)
-- 			picker:close()
-- 			vim.schedule(function()
-- 				if item then
-- 					print("You selected: " .. item.item)
-- 					print("Index: " .. item.idx)
-- 				-- Handle the selected item (e.g., open the directory or do something with it)
-- 				else
-- 					print("No item selected.")
-- 				end
-- 			end)
-- 		end,
-- 	},
-- })
