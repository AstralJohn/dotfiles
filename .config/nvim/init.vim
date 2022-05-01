" Sets ";" key to be the leader
let mapleader=";"
inoremap ;q <Esc> " Map ';q' to Esc key

" Specify a directory for plugins
call plug#begin('~/.local/share/nvim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'arcticicestudio/nord-vim'
Plug 'itchyny/lightline.vim'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'airblade/vim-gitgutter'
Plug 'preservim/nerdtree'
Plug 'ctrlpvim/ctrlp.vim'
Plug 'christoomey/vim-tmux-navigator'
Plug 'preservim/nerdcommenter'
Plug 'dense-analysis/ale'
Plug 'maximbaz/lightline-ale'
call plug#end()

let g:coc_global_extensions = [
  \ 'coc-git',
  \ 'coc-pairs',
  \ 'coc-emmet',
  "\ 'coc-eslint',
  \ 'coc-snippets',
  \ 'coc-vetur',
  \ 'coc-json',
  \ 'coc-yaml',
  \ 'coc-tsserver',
  \ 'coc-html',
  \ 'coc-pyright',
  \ 'coc-css',
  \ 'coc-go',
  \ 'coc-prettier',
  \ 'coc-docker'
  \ ]

colorscheme nord

let g:lightline = {
  \ 'colorscheme': 'nord',
  \ }


let b:ale_linter_aliases = ['javascript', 'vue']
let b:ale_linters = ['eslint', 'vls']
let g:ale_fixers = ['eslint']

nmap <silent> [l <Plug>(ale_previous_wrap)
nmap <silent> ]l <Plug>(ale_next_wrap)"

let g:ale_linters = {
    \ 'javascript': ['eslint']
    \ }
 
let g:ale_sign_error = '❌'
let g:ale_sign_warning = '⚠️'

function! Format()
  " silent call CocAction('runCommand', 'editor.action.organizeImport')
  ":execute "normal \<Plug>(coc-format)"
  :execute ":ALEFix"
endfunction

function! FormatImports()
  silent call CocAction('runCommand', 'editor.action.organizeImport')
endfunction

" Formatting selected code.
"xmap <silent> <leader>f  :call FormatImports()<CR>
"nmap <silent> <leader>f  :call FormatImports()<CR>
" xmap <leader>f  <Plug>(coc-format-selected)
" nmap <leader>f  <Plug>(coc-format-selected)
xmap <silent> <leader>F  :call Format()<CR>
nmap <silent> <leader>F  :call Format()<CR>
"xmap <silent> <leader>F  :ALEFix<CR>
"nmap <silent> <leader>F  :ALEFix<CR>

let g:ctrlp_working_path_mode = 'ra'
let g:ctrlp_custom_ignore = 'node_modules\|DS_Store\|git'

"-- Tabs Shortcuts
nnoremap tn :tabnew<Space>
nnoremap tk :tabnext<CR>
nnoremap tj :tabprev<CR>
nnoremap th :tabfirst<CR>
nnoremap tl :tablast<CR>

nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <leader>f :NERDTreeFind<CR>
let g:NERDTreeIgnore = ['^node_modules$']

" =========================
" == Indentation Options ==
" =========================

set autoindent "New lines inherit the indentation of previous lines
set expandtab "Convert tabs to spaces
set shiftwidth=2 "When shifting, indent using four spaces
set tabstop=2 "Indent using 4 spaces
set smarttab " Insert 'tabstop' number of paces with the \t key is pressed

" ========================
" ==   Search Options   ==
" ========================

set hlsearch "Enable search highlighting
set ignorecase "Ignore case when searching
set smartcase "Switch to case sensitive query when uppercase letter is detected

" =========================
" == Performance Options ==
" =========================

set complete-=i " Limit the files searched for auto-completes
set lazyredraw " Don't update screen during macro and script execution

" ============================
" == Text Rendering Options ==
" ============================

set display+=lastline " Always try to show a paragraph's last line
set encoding=utf-8 " Use an encoding that supports unicode
set linebreak " Avoid wrapping a line in the middle of a word
syntax enable " Enable syntax highlighting
set wrap "Enable line wrapping

" ============================
" == User Interface Options ==
" ============================
set number " Show line numbers
set cc=80 " Set an 80 column border for good coding style
set noerrorbells " Disable beep on errors

" ============================
" ==  Code Folding Options  ==
" ============================
" set foldmethod=indent "Fold based on indention levels
set foldmethod=syntax
map <leader>m :set foldmethod=manual<CR>
map <leader>i :set foldmethod=indent<CR>
map <leader>s :set foldmethod=syntax<CR>
augroup remember_folds
  autocmd!
  autocmd BufWinLeave * mkview
  autocmd BufWinEnter * silent! loadview
augroup END

" ===========================
" == Miscellaneous Options ==
" ===========================
set hidden " TextEdit might fail if hidden is not set
" hides highlighting
map <leader>n :noh<CR>

" Requires xclip, shared clipboard in vim
set clipboard=unnamedplus

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Make <CR> auto-select the first completion item and notify coc.nvim to
" format on enter, <cr> could be remapped by other vim plugin
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list.
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if CocAction('hasProvider', 'hover')
    call CocActionAsync('doHover')
  else
    call feedkeys('K', 'in')
  endif
endfunction

" Remap <C-f> and <C-b> for scroll float windows/popups.
if has('nvim-0.4.0') || has('patch-8.2.0750')
  nnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  nnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
  inoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
  inoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"
  vnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  vnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
endif

" Add `:Format` command to format current buffer.
command! -nargs=0 Format :call CocActionAsync('format')

" Add `:Fold` command to fold current buffer.
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer.
command! -nargs=0 OR   :call     CocActionAsync('runCommand', 'editor.action.organizeImport')
