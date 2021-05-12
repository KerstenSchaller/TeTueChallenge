from fingerprint_invalid import TestAlgo
import fingerprint_invalid 
import helbaco
import korbi_korb  
import s1cc3sT
import technik_tueftler

# Kurze Erklärung, ich habe alles zusammengemerged und falls notwendig kleine Änderungen
# gemacht damit der testcode für TestAlgo aufrufbar ist, zB entweder ne Funktion um den Code gebastelt 
# oder nen Parameter bzw Rückgabewert hinzugefügt

# Am besten einen Test nach dem anderen einkommentieren und laufen lassen 

performanceListSize = 1000
numberOfTestRepetitions = 10

# Korbis Lösung ist zu schnell für nur 1000 Einträge, damit kommt immer 0ms raus. bei 10000 gibts eher Ergebnisse != 0 ;D
TestAlgo(korbi_korb.sort_player_list, performanceListSize*10, numberOfTestRepetitions)

# s1cc3sT genauso
#TestAlgo(s1cc3sT.sort, performanceListSize*10, numberOfTestRepetitions) 

# tetüs Lösung1 ist nicht so schnell da reichen 1000
#TestAlgo(technik_tueftler.sort_highscore_list_concept_1, performanceListSize, numberOfTestRepetitions)
#TestAlgo(technik_tueftler.sort_highscore_list_concept_2, performanceListSize, numberOfTestRepetitions)
#TestAlgo(technik_tueftler.sort_highscore_list_concept_3, performanceListSize, numberOfTestRepetitions)
#TestAlgo(technik_tueftler.sort_highscore_list_concept_4, performanceListSize, numberOfTestRepetitions)
#TestAlgo(technik_tueftler.sort_highscore_list_concept_5, performanceListSize, numberOfTestRepetitions)

# fingerprints Lösung ist nicht so schnell da reichen 1000
#TestAlgo(fingerprint_invalid.sortGames, performanceListSize, numberOfTestRepetitions)
#TestAlgo(fingerprint_invalid.sortGamesShort, performanceListSize, numberOfTestRepetitions)

# helbacos Lösung gibt die Liste selbstständig aus, daher dauert der performance test ewig
#fingerprint_invalid.TestAlgo(helbaco.main, performanceListSize, numberOfTestRepetitions) 