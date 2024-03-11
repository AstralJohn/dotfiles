local map = vim.keymap.set

map("n", "<leader>n", ":noh<CR>", { silent = true, noremap = true, desc = "Map ;n to :noh" })

map("t", "<leader>t", function()
	require("nvterm.terminal").toggle("float")
end, { desc = "Toggle floating term" })

map("t", "<leader>h", function()
	require("nvterm.terminal").toggle("horizontal")
end, { desc = "Toggle horizontal term" })

map("t", "<leader>v", function()
	require("nvterm.terminal").toggle("vertical")
end, { desc = "Toggle vertical term" })

map("n", "<leader>t", function()
	require("nvterm.terminal").toggle("float")
end, { desc = "Toggle floating term" })

map("n", "<leader>h", function()
	require("nvterm.terminal").toggle("horizontal")
end, { desc = "Toggle horizontal term" })

map("n", "<leader>v", function()
	require("nvterm.terminal").toggle("vertical")
end, { desc = "Toggle vertical term" })

map("n", "<C-s>", ":MarkdownPreview<CR>", { noremap = true, silent = true, desc = "Markdown preview with ctrl-s" })

map("n", "<leader>fm", function()
	require("conform").format()
end, { desc = "Formatting" })

map("n", "<leader>cc", function()
	require("Comment.api").toggle.linewise.current()
end, { desc = "Toggle Comment" })

map("v", "<leader>cc", function()
	require("Comment.api").toggle.linewise.current()
end, { desc = "Toggle Comment" })
