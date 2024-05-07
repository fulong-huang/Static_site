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
badd +3 src/main.py
badd +1 src/htmlnode.py
badd +1 src/textnode.py
badd +2 src/leafnode.py
badd +129 src/textnode_functions.py
badd +2 src/block_functions.py
badd +1 src/__init__.py
argglobal
%argdel
$argadd ~/boot/static_site
edit src/main.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd w
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
exe '1resize ' . ((&lines * 36 + 29) / 59)
exe 'vert 1resize ' . ((&columns * 135 + 136) / 272)
exe '2resize ' . ((&lines * 36 + 29) / 59)
exe 'vert 2resize ' . ((&columns * 136 + 136) / 272)
exe '3resize ' . ((&lines * 18 + 29) / 59)
exe 'vert 3resize ' . ((&columns * 136 + 136) / 272)
exe '4resize ' . ((&lines * 18 + 29) / 59)
exe 'vert 4resize ' . ((&columns * 135 + 136) / 272)
argglobal
balt src/textnode.py
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
let s:l = 4 - ((3 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 0
lcd ~/boot/static_site
wincmd w
argglobal
if bufexists(fnamemodify("~/boot/static_site/src", ":p")) | buffer ~/boot/static_site/src | else | edit ~/boot/static_site/src | endif
if &buftype ==# 'terminal'
  silent file ~/boot/static_site/src
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
let s:l = 11 - ((10 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
normal! 011|
lcd ~/boot/static_site
wincmd w
argglobal
if bufexists(fnamemodify("~/boot/static_site/src/leafnode.py", ":p")) | buffer ~/boot/static_site/src/leafnode.py | else | edit ~/boot/static_site/src/leafnode.py | endif
if &buftype ==# 'terminal'
  silent file ~/boot/static_site/src/leafnode.py
endif
balt ~/boot/static_site/src/textnode.py
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
let s:l = 4 - ((3 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 0
lcd ~/boot/static_site
wincmd w
argglobal
if bufexists(fnamemodify("~/boot/static_site/src/textnode.py", ":p")) | buffer ~/boot/static_site/src/textnode.py | else | edit ~/boot/static_site/src/textnode.py | endif
if &buftype ==# 'terminal'
  silent file ~/boot/static_site/src/textnode.py
endif
balt ~/boot/static_site/src/htmlnode.py
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
let s:l = 1 - ((0 * winheight(0) + 9) / 18)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 07|
lcd ~/boot/static_site
wincmd w
2wincmd w
exe '1resize ' . ((&lines * 36 + 29) / 59)
exe 'vert 1resize ' . ((&columns * 135 + 136) / 272)
exe '2resize ' . ((&lines * 36 + 29) / 59)
exe 'vert 2resize ' . ((&columns * 136 + 136) / 272)
exe '3resize ' . ((&lines * 18 + 29) / 59)
exe 'vert 3resize ' . ((&columns * 136 + 136) / 272)
exe '4resize ' . ((&lines * 18 + 29) / 59)
exe 'vert 4resize ' . ((&columns * 135 + 136) / 272)
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
