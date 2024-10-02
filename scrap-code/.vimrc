set number
set relativenumber
syntax on
set autoindent
set smartindent

au InsertEnter * set paste
au InsertLeave * set nopaste

set tabstop=4        
set shiftwidth=4     
set expandtab        

set hlsearch         
set incsearch        
set ignorecase      
set smartcase       
set wrap

set showmatch

colorscheme desert  
set wildmenu

set mouse=a

set ruler

set undofile

set cursorline

set noswapfile

set clipboard=unnamedplus

nnoremap <C-j> <C-W>j
nnoremap <C-k> <C-W>k
nnoremap <C-h> <C-W>h
nnoremap <C-l> <C-W>l

set laststatus=2
set statusline=%F%m%r%h%w\ [%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v]\ [%p%%]


set list
set listchars=tab:▸\ ,trail:·
set noerrorbells
set novisualbell
set t_vb=
set ttyfast

set nobackup
set nowritebackup

