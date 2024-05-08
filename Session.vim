let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/boot/static_site
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
if &shortmess =~ 'A'
  set shortmess=aoOA
else
  set shortmess=aoO
endif
badd +1 ~/boot/static_site
badd +9 src/main.py
badd +1 src/htmlnode.py
badd +11 src/textnode.py
badd +4 src/leafnode.py
badd +3 src/textnode_functions.py
badd +92 src/block_functions.py
badd +1 src/__init__.py
badd +1 public/newDit/something.txt
badd +1 public/file.txt
badd +2 .gitignore
badd +94 static/index.css
badd +1 static/rivendell.png
badd +2 static/folder1/file1.txt
badd +1 static/folder1/file2.txt
badd +1 static/folder2/folder2.txt
badd +1 public/folder1
badd +2 public/folder2
badd +1 public/folder1/file1.txt
badd +1 public/folder1/file2.txt
badd +2 src/parentnode.py
badd +35 src/generate_page.py
badd +2 main.sh
badd +18 template.html
badd +39 content/index.md
argglobal
%argdel
$argadd ~/boot/static_site
edit src/main.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 136 + 136) / 272)
exe 'vert 2resize ' . ((&columns * 135 + 136) / 272)
argglobal
balt src/block_functions.py
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 8 - ((7 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 8
normal! 0
lcd ~/boot/static_site
wincmd w
argglobal
if bufexists(fnamemodify("~/boot/static_site/src/generate_page.py", ":p")) | buffer ~/boot/static_site/src/generate_page.py | else | edit ~/boot/static_site/src/generate_page.py | endif
if &buftype ==# 'terminal'
  silent file ~/boot/static_site/src/generate_page.py
endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let &fdl = &fdl
let s:l = 35 - ((33 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 35
normal! 07|
lcd ~/boot/static_site
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 136 + 136) / 272)
exe 'vert 2resize ' . ((&columns * 135 + 136) / 272)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
