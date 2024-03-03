"""
Kangning Li
CS 5001 Spring 2024
emojini.py
"""

def batch_translate(emoji_file_name: str, directives_file_name: str):
    """
    Function -- batch_translate
        This function orchestrate the process of converting the text
        as specified. Using the converting rule in mapping file to 
        convert every target word in the target file.
    Parameters:
        emoji_file_name -- name of emoji mapping file
        directives_file_name -- directive file gives instruction + orchestrate
    """

    try:
        with open(emoji_file_name, 'r') as file:
            # using a list to store emoji sets name, a matrix to store data
            emoji_name = []
            data = []

            # read the first line then get emoji_name
            first_line = file.readline().split()
            if first_line[0] == "METADATA":
                emoji_name = first_line[1:]
            else:
                raise TypeError("Input file is not METADATA")
            
            # read the following construct the matrix
            for line in file:
                data.append(line.split())
            
            # change english words into lower case
            idx = emoji_name.index("ENGLISH")
            for i in range(len(data)):
                data[i][idx] = data[i][idx].lower()

        # take the order
        with open(directives_file_name, 'r') as file:
            for line in file:
                # specfic the order
                order = line.split()
                process_file(order, emoji_name, data)
            print("done")

    except FileNotFoundError as e:
        print(f"Error: {e}")
            
def process_file(order_detail: list[str], emoji_meta: list[str],
                 emoji_data: list[list[str]]):
    """
    Function -- process_file
        Translate every word in source_file according to the dictionary
        and modify the file and write another target_file
    Parameters:
        order_detail -- containing the details of converting order
        emoji_meta -- the header meta of emoji data
        emoji_data -- detailed data to construct dictionary
    """
    source_format, target_format, source_file, target_file = order_detail[:4]

    # get the index represent the source and target
    for i in range(len(emoji_meta)):
        if emoji_meta[i] == source_format.upper():
            source_idx = i
        if emoji_meta[i] == target_format.upper():
            target_idx = i
    
    # construct the translator dictionary
    translator = {}
    for line in emoji_data:
        translator[line[source_idx]] = line[target_idx]
    
    # read file
    print("Processing " + source_file + ": " + 
          source_format + " -> " + target_format)
    
    with open(source_file, 'r') as file:
        raw_data = []
        for line in file:
            raw_data.append(line.strip().split())
    
    # process file change critical words
    for key, value in translator.items():
        for sentence in raw_data:
            for i in range(len(sentence)):
                if sentence[i] == key:
                    sentence[i] = value
    
    # merge raw_data into output
    with open(target_file, 'w') as file:
        output = []
        
        for i in range(len(raw_data)):
            raw_data[i] = " ".join(raw_data[i])
            output.append(raw_data[i])

        output_str = "".join([s + "\n" for s in output])
        file.write(output_str)

def main():
    batch_translate("emojis.txt", "emoji_directives.txt")

if __name__ == "__main__":
    main()
