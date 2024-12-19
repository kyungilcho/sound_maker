from utils import *
from measures import *
from measures_refactored import *
from measures_for_christmas import *

    
# Generate and save the Mario theme melody
sequence1 = create_sequence([MEASURE_1, MEASURE_2])

sequence2 = create_sequence([
    MEASURE_3, MEASURE_4, MEASURE_5, MEASURE_6,
])

sequence3 = create_sequence([
    MEASURE_7, MEASURE_8, MEASURE_7, MEASURE_9, MEASURE_7, MEASURE_8, MEASURE_10, MEASURE_11,
])

play_sequence(sequence1)
play_sequence(sequence2)
play_sequence(sequence2)
play_sequence(sequence3)
play_sequence(sequence3)



#########################################################


sequence1_refactored = create_sequence_refactored([MEASURE_1_REFACTORED, MEASURE_2_REFACTORED])
sequence2_refactored = create_sequence_refactored([MEASURE_3_REFACTORED, MEASURE_4_REFACTORED, MEASURE_5_REFACTORED, MEASURE_6_REFACTORED])
sequence3_refactored = create_sequence_refactored([MEASURE_7_REFACTORED, MEASURE_8_REFACTORED, MEASURE_7_REFACTORED, MEASURE_9_REFACTORED, MEASURE_7_REFACTORED, MEASURE_8_REFACTORED, MEASURE_10_REFACTORED, MEASURE_11_REFACTORED])
sequence4_refactored = create_sequence_refactored([
    MEASURE_12_REFACTORED, MEASURE_13_REFACTORED, MEASURE_14_REFACTORED, MEASURE_REST_REFACTORED, MEASURE_12_REFACTORED, MEASURE_13_REFACTORED
])

# play_sequence_refactored(sequence1_refactored)
# play_sequence_refactored(sequence2_refactored)
# play_sequence_refactored(sequence2_refactored)
# play_sequence_refactored(sequence3_refactored)
# play_sequence_refactored(sequence3_refactored)
# play_sequence_refactored(sequence4_refactored)
# play_sequence_refactored(sequence1_refactored)
# play_sequence_refactored(sequence2_refactored)
# play_sequence_refactored(sequence2_refactored)


#########################################################


# play_sequence_with_envelope(sequence1_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence3_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence3_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence4_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence1_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.PIANO)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.PIANO)


#########################################################



# play_sequence_with_envelope(sequence1_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence3_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence3_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence4_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence1_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.VIOLIN)
# play_sequence_with_envelope(sequence2_refactored, instrument=Instrument.VIOLIN)



#########################################################



# christmas_sequence = create_sequence([MEASURE_1_CHRISTMAS, MEASURE_2_CHRISTMAS, MEASURE_3_CHRISTMAS, MEASURE_4_CHRISTMAS, MEASURE_5_CHRISTMAS, MEASURE_6_CHRISTMAS, MEASURE_7_CHRISTMAS, MEASURE_8_CHRISTMAS])

# play_sequence_with_envelope(christmas_sequence, instrument=Instrument.VIOLIN)



print("Super Mario Bros. Main Theme has been generated and saved!")








#########################################################





# add merry christmas message to README.md

f = open("README.md", "a")
f.write("\n\nMerry Christmas!")
f.close()