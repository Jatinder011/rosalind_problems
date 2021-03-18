# dna = "GATGGAACTTGACTACGTAAATT"

dna = input('Enter your DNA seq: ')

# function to transcribe DNA to RNA
def transcription(dna):
    return dna.replace("T", "U")

print("Transcribed RNA:", transcription(dna), sep="\n")



