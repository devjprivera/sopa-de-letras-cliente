# AlphabetSoup Solver

def soupSolver(soup, words, size=14):
    soup_matrix = []
    soup_rows = []
    transposed_soup = []
    size_NxN = size
    word_state = {}

    # Formatting
    soup = soup.replace(",", "").split(" ")
    for i in range(size_NxN):
        row = []
        for j in range(size_NxN):
            letter = soup.pop(0)
            row.append(letter)
        soup_matrix.append(row) # For diagonal search
        row = "".join(row)
        soup_rows.append(row) # For horizontal search
    words = words.split(", ")
    for word in words:
        word_state[word] = False
    transposed_soup = list(zip(*soup_matrix)) # For vertical search
    transposed_soup = ["".join(col) for col in transposed_soup]

    # Words search
    for word in words:
        for row in soup_rows: # Check Horizontally
            reverse_word = word[::-1]
            if word in row:
                word_state[word] = True
                break
            elif reverse_word in row:
                word_state[word] = True
                break
  
        for col in transposed_soup: # Check Vertically
            reverse_word = word[::-1]
            if word in col:
                word_state[word] = True
                break
            elif reverse_word in col:
                word_state[word] = True
                break

    word_len = len(word)
    for row in range(size_NxN):
        for col in range(size_NxN):
            if soup_matrix[row][col] == word[0]:  # Check if first character of word in cell
                for d in range(word_len): # Check diagonally top-left to bottom-right
                    if (row + d) >= size_NxN or (col + d) >= size_NxN: # Out of bounds
                        break
                    elif word[d] != soup_matrix[row + d][col + d]:
                        break
                    if d == word_len - 1:
                        word_state[word] = True
                if word_state[word]: # Break if word found
                    break
                for d in range(word_len): # Check diagonally top-right to bottom-left
                    if (row + d) >= size_NxN or (col - d) < 1: # Out of bounds
                        break
                    elif word[d] != soup_matrix[row + d][col - d]:
                        break
                    if d == word_len - 1:
                        word_state[word] = True
                if word_state[word]:
                    break
                for d in range(word_len): # Check diagonally bottom-left to top-right
                    if (row - d) < 1 or (col + d) >= size_NxN: # Out of bounds
                        break
                    elif word[d] != soup_matrix[row - d][col + d]:
                        break
                    if d == word_len - 1:
                        word_state[word] = True
                if word_state[word]:
                    break
                for d in range(word_len): # Check diagonally bottom-right to top-left
                    if (row - d) < 1 or (col - d) < 1: # Out of bounds
                        break
                    elif word[d] != soup_matrix[row - d][col - d]:
                        break
                    if d == word_len - 1:
                        word_state[word] = True
                if word_state[word]:
                    break

    return word_state