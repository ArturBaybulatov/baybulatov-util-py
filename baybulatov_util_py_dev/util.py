# Version: dev

from pydash import _
import datetime
import random
import string


def take(coll, n):
    chunk = coll[0:n]
    del coll[0:n]
    return chunk


def take_random(coll, n):
    if n == 0:
        return []

    chunk = _.sample_size(coll, n)

    for item in chunk:
        coll.remove(item)

    return chunk


def take_one_random(coll):
    if len(coll) == 0:
        return None

    return coll.pop(random.randint(0, len(coll) - 1))


def random_date():
    return datetime.date(
        random.random(1970, 2020),
        random.random(1, 12),
        random.random(1, 28),
    )


def visually_random_number():
    return random.choice((
        random.randint(1, 9),
        random.randint(10, 99),
        random.randint(100, 999),
        random.randint(1000, 9999),
        random.randint(10000, 99999),
        random.randint(100000, 999999),
    ))


def lorem(sentence_count=random.randint(1, 5), word_count=None):
    vocab = (
        'a ac adipiscing amet ante arcu at auctor augue bibendum commodo condimentum consectetur consequat convallis curabitur'
        'cursus diam dictum dignissim dolor donec duis efficitur eget eleifend elit enim erat et eu ex facilisis faucibus feugiat'
        'finibus gravida iaculis id imperdiet in integer ipsum lacinia lacus laoreet lectus leo libero ligula lobortis lorem'
        'luctus maecenas mauris metus mi mollis morbi nam nec neque nisi non nulla nullam nunc odio orci ornare pellentesque'
        'pharetra phasellus porta porttitor posuere pretium proin pulvinar purus quam quis rhoncus rutrum sapien sed sem semper'
        'sit sollicitudin tempor tempus tincidunt tortor turpis ullamcorper ultricies ut varius vehicula vel velit vestibulum'
        'vitae viverra volutpat vulputate'
    ).split(' ')

    def generate_sentence():
        current_word_count = random.randint(5, 30) if word_count is None else word_count
        return _(vocab).sample_size(current_word_count).join(' ').capitalize().value()

    return '. '.join(_.times(sentence_count, generate_sentence))


def random_ident(length=8):
    return ''.join(
        [random.choice(string.ascii_lowercase)] +
        _.times(length-1, lambda x_: random.choice(string.ascii_letters + string.digits))
    )


def morph(number, words):
    CHOICES = (2, 0, 1, 1, 1, 2)

    if 4 < number % 100 < 20:
        choice = 2
    else:
        choice = CHOICES[number % 10 if number % 10 < 5 else 5]

    return words[choice]
