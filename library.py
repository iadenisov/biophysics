#!/usr/bin/python
LIB = open("/usr/share/texlive/texmf-dist/bibtex/bib/mylib/diaZoteroLib.bib")

AUX = open("tutorial.aux")

lib = set()


for line in AUX:
	if line[:9] == "\\citation":
		for item in line.split("{")[1].split("}")[0].split(","):
			lib.add(item)
			print item

#print lib
RES = open("library.bib", "w")

write = False

# & (line[:3] != "doi")

for line in LIB:
	if write:
		if (line[:3] != "url") & (line[:6] != "annote") & (line[:8] != "abstract") & (line[1:5] != "file")  & (line[1:5] != "iccn") & (line[1:5] != "note"):
			print >> RES, line,
		if line.strip() == "},":
			write = False
	
	if line[:1] == "@":
		if line.split("{")[1].split(",")[0] in lib:
			print >> RES, line,
			write = True
				


#for j in range(1,i):
#	print lib[j]
		
