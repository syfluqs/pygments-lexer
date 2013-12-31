#input=~/electronic-design-pattern/spice/power-supply/simple-rectifier/flattened-model.cir
input=~/electronic-design-pattern/spice/power-supply/simple-rectifier/simple-rectifier.cir

pygmentize -O full -f html -o /tmp/example.html $input
firefox /tmp/example.html
