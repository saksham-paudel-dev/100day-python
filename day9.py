
from collections import Counter, defaultdict

# 1. DICTIONARY COMPREHENSION
print("=== Dictionary Comprehension ===")

numbers = [1, 2, 3, 4, 5]

squares = {n: n ** 2 for n in numbers}

print("Squares:", squares)


# 2. SET COMPREHENSION
print("\n=== Set Comprehension ===")

values = [1, 2, 2, 3, 3, 4, 5, 5]

unique_squares = {n ** 2 for n in values}

print("Unique squares:", unique_squares)


# 3. COUNTER
print("\n=== Counter ===")

words = ["python", "java", "python", "sql", "java", "python"]

word_count = Counter(words)

print("Word counts:", word_count)
print("Python count:", word_count["python"])
print("Most common:", word_count.most_common(2))


# 4. DEFAULTDICT
print("\n=== Defaultdict ===")

student_marks = defaultdict(list)

student_marks["Saksham"].append(85)
student_marks["Saksham"].append(90)
student_marks["Ram"].append(78)

print("Student marks:", dict(student_marks))


# 5. GENERATORS
print("\n=== Generators ===")

def generate_squares(limit):
    for n in range(1, limit + 1):
        yield n ** 2


squares_generator = generate_squares(5)

for square in squares_generator:
    print(square)


# 6. PRACTICAL MINI PROJECT:
# Count words and group them by their first letter

print("\n=== Word Analysis ===")

sentence = "python programming is fun and python is powerful"

word_list = sentence.split()

# Dictionary comprehension
word_lengths = {word: len(word) for word in set(word_list)}
print("Word lengths:", word_lengths)

# Counter
frequency = Counter(word_list)
print("Frequency:", frequency)

# Defaultdict
words_by_letter = defaultdict(list)

for word in word_list:
    words_by_letter[word[0]].append(word)

print("Words by first letter:", dict(words_by_letter))

# Generator expression
long_words = (word for word in word_list if len(word) > 5)

print("Long words:", list(long_words))
