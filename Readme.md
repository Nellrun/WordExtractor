This application, wrote in python, parsing sub files and extracting english words, that adding your dictionary


BNF:
<subtitles> = <block> "\n" | <block> "\n" <subtitles>
<block> = <num> "\n" <timeLine> <speeches>
<num> = 1 | 2 | 3 ...
<timeLine> = <time> <arrow> <time> "\n"
<time> = <num> ":" <num> ":" <num> "," <num>
<arrow> = "-" "-" ">"
<speeches> = <sentence> "\n" | <sentence> <speeches>
<sentence> = <sign> "\n" | <word> "\n" | <sign> <sentence> | <word> <sentence>
<sign> = "-" | "," | "." | "!" | "?" | ":"
<word> = "a", "b" ... "z", "'", "aa", "ab", ...