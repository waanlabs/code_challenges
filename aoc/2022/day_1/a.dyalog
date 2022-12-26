⍝ Answer 1
cal ← ⍎¨¨((×≢¨)⊆⊢)⊃⎕NGET 'D:\calories.txt' 1

⍝ Part 1
⌈/+/¨cal

⍝ Part 2
+/3↑(⊂⍤⍒⌷⊢)+/¨cal
