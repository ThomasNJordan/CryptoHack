from pwn import *
import binascii
import itertools
import string

def repeating_key_xor(plaintext, key):
    if len(key) == 0 or len(key) > len(plaintext):
        raise "KEY LENGTH EXCEPTION!"
  
def single_byte_xor(plaintext, key):
    if len(key) != 1:
      raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"
    return xor(plaintext, key*len(plaintext))

    ciphertext_bytes = bytearray()
    plaintext_bytes = bytearray(plaintext)
    key_bytes = bytearray(key)
  
    # XOR every byte of the plaintext with the corresponding byte from the key  
    for i in range( len(plaintext) ):
        k = key_bytes[i % len(key)]
        c = plaintext_bytes[i] ^ k
        ciphertext_bytes.append(c)
      
    return str(ciphertext_bytes)


def has_nonprintable_characters( text ):
    for char in text:
        if char not in string.printable:
            return True
    return False

def has_vowels( text ):
    vowels = list("eyuioa")
    for char in vowels:
        if char in text:
            return True
    return False

def has_forbidden_digraphs( text ):
    forbidden_digraphs = ['cj','fq','gx','hx','jf','jq','jx','jz','qb','qc','qj','qk','qx','qz','sx','vf','vj','vq','vx','wx','xj','zx']
    for digraph in forbidden_digraphs:
        if digraph in text:
            return True
    return False

def has_necessary_percentage_frequent_characters( text, p=38 ):
    most_frequent_characters = list("etaoin")
  
    cnt = 0
    for char in most_frequent_characters:
        cnt += text.count(char)
      
    percent_characters =  float(cnt)*100/len(text)
  
    # The most_frequent_characters shoud be more than 38% of the text.
    # For short messages this value may need to be lowered.
    if (percent_characters < p):
        return False
    return True
  
def has_necessary_percentage_punctuation( text, p=10 ):
    cnt = 0
    for char in string.punctuation:
        cnt += text.count(char)
  
    # Punctuation characters should be no more than 10% of the text.
    punctuation = float(cnt)*100/len(text)  
    if punctuation > 10:
        return False
    return True

def has_english_words( text ):
    most_frequent_words = ['the', 'and', 'have', 'that', 'for',
    'you', 'with', 'say', 'this', 'they', 'but', 'his', 'from',
    'that', 'not', "n't", 'she', 'what', 'their', 'can', 'who',
    'get', 'would', 'her', 'make', 'about', 'know', 'will',
    'one', 'time', 'there', 'year', 'think', 'when', 'which',
    'them', 'some', 'people', 'take', 'out', 'into','just', 'see',
    'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other',
    'how', 'then', 'its', 'out', 'two', 'more ,these', 'want',
    'way', 'look', 'first', 'also', 'new', 'because', 'day',
    'more', 'use', 'man', 'find', 'here', 'thing', 'give', 'many']
  
    for word in most_frequent_words:
        if word in text:
            return True
    return False
  
  
def is_english( input_text ):    
    text = input_text.lower()
  
    if has_nonprintable_characters( text ):
        return False

    # If the text contains one of the most frequent english words
    # it is very likely that it's an english text  
    if has_english_words( text ):
        return True

    if not has_vowels( text ):
        return False
 
    if has_forbidden_digraphs( text ):
        return False

    if not has_necessary_percentage_frequent_characters( text ):
        return False

    if not has_necessary_percentage_punctuation( text ):
        return False
 
    return True


def divide_text_by_blocks(text, block_size):
    blocks = []
    num_blocks = len(text)/block_size
    for i in range(num_blocks):
        blocks.append( text[i*block_size : (i+1)*block_size] )
    
    return blocks

def transpose( blocks ):
    transposed = []
    block_size = len(blocks[0])
    num_blocks = len(blocks)
    for i in range(block_size):
        tmp = [] 
        for j in range(num_blocks):
            # tmp is composed of the i-th character of every block
            tmp.append( blocks[j][i] )
        transposed.append( ''.join(tmp) )  
    return transposed
    
def has_necessary_percentage_letters( text,p=80 ):
    characters = string.letters + ' '
  
    cnt = 0
    for char in characters:
        cnt += text.count(char)
      
    percent_characters =  float(cnt)*100/len(text)
  
    # The characters shoud be more than 38% of the text.
    if (percent_characters < p):
        return False
    return True

def is_printable_text( text ):
    text = text.lower()
    if has_nonprintable_characters(text):
        return False
    if not has_necessary_percentage_punctuation( text ):
        return False
    if not has_necessary_percentage_letters( text ):
        return False
    if not has_vowels( text ):
        return False
    return True

def hamming_distance(str1, str2):
    result = xor(str1, str2)
  
    return bin( int( result.encode('hex'), 16) ).count('1')

def find_xor_keysize( ciphertext, hamming_blocks, minsize=2, maxsize=10 ):
    hamming_dict = {} # <keysize> : <hamming distance>
  
    if (hamming_blocks*maxsize) > len(ciphertext):
        raise "OUT OF BOUND EXCEPTION! Lower the hamming_blocks or the key maxsize!"
  
    for key_length in range(minsize, maxsize):
        # Take the first 'hamming_blocks' blocks
        # with size key_length bytes
        blocks = []
        for i in range(hamming_blocks):
            blocks.append( ciphertext[i*key_length : (i+1)*key_length] )
    
        # Calculate the hamming distance between the blocks
        # (first,second) ; (first,third) ; (first,fourth)
        # (second, third) ; (second, fourth)
        # (third, fourth) ; There are sum(1,hamming_blocks-1) combinations
        hd = [] # hamming distance
        for i in range( hamming_blocks - 1 ):
            for j in range( i+1, hamming_blocks ):
                hd.append( hamming_distance(blocks[i], blocks[j] ))

        hd_average = float(sum(hd))/len(hd)
        hd_normalized = hd_average/key_length

        hamming_dict[key_length] = hd_normalized
  
    # Get sorted (ascending order) list of tuples. Sorted by dictionary value (i.e. hamming distance)
    sorted_list_tuples = sorted(hamming_dict.items(), key=lambda x: x[1])
  
    # One of the three keys that produced the lowest hamming distance
    # is likely the actual size
    return [ sorted_list_tuples[0][0], sorted_list_tuples[1][0], sorted_list_tuples[2][0] ]

def break_repeat_key_xor( ciphertext ):
    # Tweaking this is useful. Lower value (0.03-0.05) helps find longer keys
    # Higher value (0.1 - 0.15) helps find shorter keys
    hamming_blocks = int(len(ciphertext)*0.06)
    key_sizes = find_xor_keysize(ciphertext, hamming_blocks , 2)
    print("Key sizes: ", key_sizes)
  
    for ks in key_sizes:
        print("Current key size: ", ks)
        blocks = divide_text_by_blocks(ciphertext, ks)
    
        transposed = transpose(blocks)
    
        all_keys = [] # list of lists. One list for every block. The list has all possible one-byte keys for the block.
        for block in transposed:  
            block_keys = [] # store all possible one-byte keys for a single block
            for key in range(256):
                text = single_byte_xor( block , chr(key))
                if is_printable_text(text):
                    block_keys.append(chr(key))
                print (block_keys)
                all_keys.append(block_keys)
 
        real_keys = [] # Stores keys with size ks. Generated from all possible combinations of one-byte keys contained in all_keys    
        for key in itertools.product(*all_keys):
            real_keys.append( ''.join(key) )
    
        print("Keys to try: ", len(real_keys))
        # Try every possible multy-byte key.
        for key in real_keys:
            text = repeating_key_xor(ciphertext,key)
            if is_english(text):
                print ("Plaintext: " ,text)
                print ("Key: ", key)
                raw_input()
                print ("==================")

bytestring = binascii.unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

msgs = []
for i in bytestring:
    q = chr(i)
    msgs.append(q)
msg = "".join(msgs)
print(msg)

key = "myXORkey"
c = repeating_key_xor(msg, key)

break_repeat_key_xor(c)