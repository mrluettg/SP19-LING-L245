all:
	lt-comp lr apertium-hbs.hbs.dix hbs-eng.automorf.bin
	lt-comp rl apertium-eng.eng.dix hbs-eng.autogen.bin

	lt-comp lr apertium-eng.eng.dix eng-hbs.automorf.bin
	lt-comp rl apertium-hbs.hbs.dix eng-hbs.autogen.bin

	lt-comp lr apertium-hbs-eng.hbs-eng.dix hbs-eng.autobil.bin
	lt-comp rl apertium-hbs-eng.hbs-eng.dix eng-hbs.autobil.bin

	apertium-preprocess-transfer apertium-hbs-eng.hbs-eng.t1x hbs-eng.t1x.bin