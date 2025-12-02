TestInput ← $ 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
            $ 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
            $ 824824821-824824827,2121212118-2121212124
Input     ← &fras "input"

Parse       ← ↯∞_2⊜⋕⊸∊"0123456789"
IsRepeated₂ ← ⨬(0|≍°⊟↯2_∞)(=0◿2⊸⧻)
CoolRange   ← +⇡⤚-°⊟⍜(⊡1|+1)
IsRepeatedN ← ⨬(0◌|≍⊸↻1) ⊃(=0◿⊙⧻)(↯[⊙∞]⊙∘)

AnyRepeats  ← /↥≡(IsRepeatedN ∩°□°⊟⇌)⍉⊟□⟜(↘2⇡+1⧻)
AnyRepeats′ ← ⨬(0◌|AnyRepeats)⊸(≠1⧻)

Part₁ ← /+≡(/+×⟜≡(IsRepeated₂ °⋕) CoolRange)
Part₂ ← /+≡(/+×⟜≡(AnyRepeats′ °⋕) CoolRange)
⊃Part₁ Part₂ Parse Input

┌─╴tests
  ˙⍤=⊃(IsRepeatedN 2)IsRepeated₂ [1 2 3 1 2 3]
  ˙⍤=⊃(IsRepeatedN 2)IsRepeated₂ [1 2 3 1]
  ˙⍤=⊃(IsRepeatedN 2)IsRepeated₂ [1 2]
  ˙⍤=1227775554 Part₁ Parse TestInput
  ˙⍤=4174379265 Part₂ Parse TestInput
└─╴
