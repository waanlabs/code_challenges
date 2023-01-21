⍝ Answer 1
cal ← ⍎¨¨((×≢¨)⊆⊢)⊃⎕NGET 'cal.txt' 1

⍝ Part 1
⌈/+/¨cal

⍝ Part 2
+/3↑(⊂⍤⍒⌷⊢)+/¨cal


⍝ Answer 2
c←+/¨⍎¨¨(×≢¨c)⊆c←⊃⎕NGET 'cal.txt' 1

⍝ Part 1
⌈/p

⍝ Part 2
+/3↑{⍵[⍒⍵]}p
