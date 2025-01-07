from music21 import stream, note

def transpose_part_handle_sharp_and_flat(part, n):
    transposed_part = stream.Part()
    for element in part:
        if isinstance(element, note.Note):

            transposed_note = note.Note()
            transposed_note.pitch.midi = element.pitch.midi + n
            
            if '#' in transposed_note.pitch.name:
                transposed_note.pitch.midi += 1 
                transposed_note.pitch.name = transposed_note.pitch.name.replace('#', '')

            if '-' in transposed_note.pitch.name:
                transposed_note.pitch.name = transposed_note.pitch.name.replace('-', '')

            transposed_note.quarterLength = element.quarterLength
            transposed_part.append(transposed_note)
        elif isinstance(element, note.Rest):
            transposed_part.append(element)
        
        elif isinstance(element, stream.Measure):
            transposed_measure = stream.Measure()
            for sub_element in element:
                if isinstance(sub_element, note.Note):
                    transposed_note = note.Note()
                    transposed_note.pitch.midi = sub_element.pitch.midi + n
                    if '#' in transposed_note.pitch.name:
                        transposed_note.pitch.midi += 1
                        transposed_note.pitch.name = transposed_note.pitch.name.replace('#', '')
                    if '-' in transposed_note.pitch.name:
                        transposed_note.pitch.name = transposed_note.pitch.name.replace('-', '')
                    transposed_note.quarterLength = sub_element.quarterLength
                    transposed_measure.append(transposed_note)
                elif isinstance(sub_element, note.Rest):
                    transposed_measure.append(sub_element)
            transposed_part.append(transposed_measure)

        elif isinstance(element, stream.Stream):
            transposed_stream = transpose_part_handle_sharp_and_flat(element, n)
            transposed_part.append(transposed_stream)
        
    return transposed_part
