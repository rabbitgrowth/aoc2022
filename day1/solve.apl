#!/usr/local/bin/dyalogscript
⎕←⍪1 3+/⍤↑¨⊂{⍵[⍒⍵]}(+/⍎¨)¨((×≢¨)⊆⊢)⊃⎕NGET'input.txt'1
