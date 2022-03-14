print('''
               _ ___                /^^\ /^\  /^^\_
    _          _@)@) \            ,,/ '` ~ `'~~ ', `\.
  _/o\_ _ _ _/~`.`...'~\        ./~~..,'`','',.,' '  ~:
 / `,'.~,~.~  .   , . , ~|,   ,/ .,' , ,. .. ,,.   `,  ~\_
( ' _' _ '_` _  '  .    , `\_/ .' ..' '  `  `   `..  `,   \_
 ~V~ V~ V~ V~ ~\ `   ' .  '    , ' .,.,''`.,.''`.,.``. ',   \_
  _/\ /\ /\ /\_/, . ' ,   `_/~\_ .' .,. ,, , _/~\_ `. `. '.,  \_
 < ~ ~ '~`'~'`, .,  .   `_: ::: \_ '      `_/ ::: \_ `.,' . ',  \_
  \ ' `_  '`_    _    ',/ _::_::_ \ _    _/ _::_::_ \   `.,'.,`., \-,-,-,_,_,
   `'~~ `'~~ `'~~ `'~~  \(_)(_)(_)/  `~~' \(_)(_)(_)/ ~'`\_.._,._,'_;_;_;_;_;
       ''')
print("Welcome to dragon kingdom!")
print("Good luck!")


a1 = input("You are at a fork do you go left or right? l for left, r for right: \n").lower()
if a1 == "r":
  a2 = input("You made it to the castle!\n Do you use the drawbridge or do you swim? b for bridge, s for swim: \n").lower()
elif a1 == "l":
  print("Game over! You fell into a hole")

if a2 == "s":
  a3 = input("You made it across! \n so you climb over the wall, or dig your way in? c for climb, d for dig?\n").lower()
elif a2 == "b":
  print("game over! ")
if a3 == "d":
  a4 = input("You fell into a cave do climb back out, go down the tonnel or hide? c, t or h?\n").lower()
elif a3 == "c":
  print("Game over! A dragon spotted you smoltered! ")

if a4 == "c":
  print("game overrrrr!")
elif a4 == "t":
  print("game over you fell on lava!!")
elif a4 == "h":
  print("yayy you won!")
