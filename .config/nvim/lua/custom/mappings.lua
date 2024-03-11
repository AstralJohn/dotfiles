---@type MappingsTable
local M = {}

M.nvterm = {
  t = {
    -- toggle in terminal mode
    ["<leader>t"] = {
      function()
        require("nvterm.terminal").toggle "float"
      end,
      "Toggle floating term",
    },

    ["<leader>h"] = {
      function()
        require("nvterm.terminal").toggle "horizontal"
      end,
      "Toggle horizontal term",
    },

    ["<leader>v"] = {
      function()
        require("nvterm.terminal").toggle "vertical"
      end,
      "Toggle vertical term",
    },
  },

  n = {
    ["<leader>n"] = { ":noh<CR>", "Map ;n to :noh", opts = { noremap = true, silent = true } },
    -- toggle in normal mode
    ["<leader>t"] = {
      function()
        require("nvterm.terminal").toggle "float"
      end,
      "Toggle floating term",
    },

    ["<leader>h"] = {
      function()
        require("nvterm.terminal").toggle "horizontal"
      end,
      "Toggle horizontal term",
    },

    ["<leader>v"] = {
      function()
        require("nvterm.terminal").toggle "vertical"
      end,
      "Toggle vertical term",
    },
  },
}

M.general = {
  i = {
    ["<leader>q"] = { "<Esc>", "Map ;q to escape", opts = { noremap = true, silent = true } },
  },

  n = {
    ["<C-s>"] = { ":MarkdownPreview<CR>", "Markdown preview with ctrl-s", opts = { noremap = true, silent = true } },
    ["<leader>q"] = { "<Esc>", "Map ;q to escape", opts = { noremap = true, silent = true } },

    --  format with conform
    ["<leader>fm"] = {
      function()
        require("conform").format()
      end,
      "formatting",
    },
  },
  v = {
    [">"] = { ">gv", "indent" },
  },
}

M.comment = {
  -- toggle comment in both modes
  n = {
    ["<leader>cc"] = {
      function()
        require("Comment.api").toggle.linewise.current()
      end,
      "Toggle comment",
    },
  },

  v = {
    ["<leader>cc"] = {
      "<ESC><cmd>lua require('Comment.api').toggle.linewise(vim.fn.visualmode())<CR>",
      "Toggle comment",
    },
  },
}

-- more keybinds!

return M
