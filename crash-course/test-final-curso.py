# Hello World program in Python
    
print ("Hello World!");

a = """Epales que mas verga como {} epales esta la i a verga como de la madre [] epales Epales verga verga verga epales"""

puntuaciones = "{}[]"
palabras = ['que', 'la', 'de', 'la', 'i', 'a']
nube_palabras = {}

# Lower case characters
a = a.lower()

# clear punctuations signs
for signo in puntuaciones:
    a = a.replace(signo, '')

# clear punctuations words
for palabra in palabras:
    a = a.replace(palabra,'')

# array and count words
a = a.split()

for palabra in a:
    nube_palabras[palabra] = a.count(palabra)

print(nube_palabras)


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"”\,<>./?@#$%^&*_~—'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    file_contents = file_contents.lower()
    cloud_word_dic = {}
    # clear punctuations signs
    for sign in punctuations:
        file_contents = file_contents.replace(sign, '')
    
    # clear punctuations words
    for word in uninteresting_words:
        file_contents = file_contents.replace(word,'')
    
    file_contents = file_contents.split()
    for words in file_contents:
        cloud_word_dic[words] = file_contents.count(words)
    
    print(file_contents)
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(cloud_word_dic)
    return cloud.to_array()