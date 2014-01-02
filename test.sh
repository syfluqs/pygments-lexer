#input=~/electronic-design-pattern/spice/power-supply/simple-rectifier/flattened-model.cir
#input=~/electronic-design-pattern/spice/power-supply/simple-rectifier/simple-rectifier.cir
#input=~/page-perso/orange/source/_literal_includes/circuit_diagram/simple-rectifier.m4
#input=~/page-perso/orange/source/_literal_includes/circuit_diagram/simple-rectifier-enhanced.m4
input=test.m4

pygmentize -O full -f html -o /tmp/example.html $input
firefox /tmp/example.html
