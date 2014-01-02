define(AUTHOR, William Shakespeare)dnl

A Midsummer Night's Dream
by AUTHOR

`AUTHOR' is AUTHOR
 `#' AUTHOR
 ``AUTHOR'' is AUTHOR

 define(newline,`line
  break')
  a newline here

 `AUTHOR
  ' is AUTHOR.''

define(PARENS, ())

define(LPAREN,`(')
define(RPAREN,`)')

.PS
cct_init(SIdefaults) # initialise and use metric unit
linethick_(.5) # line thickness
define(`dimen_', 10) # component size
elen = dimen_*3/2
Origin: Here
  # go up and draw the source and the in label
  source(up_ elen, AC); llabel(,V_{in},); dot; "in" above
  # turn right and draw the diode
  diode(right_ elen); llabel(,D,)
  # draw the out label
  dot; "out" above
  { # save the current position
    # go down and draw the capacitor
    capacitor(down_ to (Here,Origin)); rlabel(,C_{load},)
    # draw the 0 label
    dot; "0" below
  }
  # draw a forward horizontal line
  line right_ elen*1/2
  # go down and draw the resistor
  resistor(down_ Here.y-Origin.y,,E); llabel(,R_{load},)
  # draw a backward horizontal segment
  line to Origin
.PE

.PS
cct_init(SIdefaults)
linethick_(.5)
define(`dimen_', 10)
elen = dimen_*3/2
epsilon = 1e-3
define(`bigdiode',
  `resized(2., `diode', $1)')
Origin: Here
  source(up_ elen, AC); llabel(,V_{in},); dot; "in" above
  bigdiode(right_ elen); llabel(,D,)
  dot; "out" above
  {
    capacitor(down_ to (Here,Origin)); rlabel(,C_{load},)
    dot; "0" below
  }
  line right_ elen*1/2 then down epsilon
  resistor(down_ Here.y-Origin.y,,E); llabel(,R_{load},)
  line down epsilon then to Origin then up epsilon
.PE
