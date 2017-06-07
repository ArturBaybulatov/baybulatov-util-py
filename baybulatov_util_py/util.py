# Version 0.2

from pprint import pprint, pformat
import datetime
import pydash as _
import random
import string


def take(coll, n):
    chunk = coll[0:n]
    del coll[0:n]
    return chunk


def take_random(coll, n):
    if n == 0:
        return []

    chunk = _.sample(coll, n)

    for item in chunk:
        coll.remove(item)

    return chunk


def take_one_random(coll):
    if len(coll) == 0:
        return None

    return coll.pop(_.random(0, len(coll)-1))


def random_phone():
    return '+7' + str(_.sample((917, 964, 965, 987, 912, 935))) + str(_.random(1000000, 9999999))


def random_date():
    #return timezone.utc.localize(timezone.datetime(_.random(2010, 2020), _.random(1, 12), _.random(1, 28)))
    return datetime.date(_.random(2010, 2020), _.random(1, 12), _.random(1, 28))


def random_amount():
    return random.random() * random.choice((100, 1000, 10000))


def lorem(words=None, sentences=5):
    vocab = _.split((
        'a ac adipiscing amet ante arcu at auctor augue bibendum commodo condimentum consectetur consequat convallis curabitur'
        'cursus diam dictum dignissim dolor donec duis efficitur eget eleifend elit enim erat et eu ex facilisis faucibus feugiat'
        'finibus gravida iaculis id imperdiet in integer ipsum lacinia lacus laoreet lectus leo libero ligula lobortis lorem'
        'luctus maecenas mauris metus mi mollis morbi nam nec neque nisi non nulla nullam nunc odio orci ornare pellentesque'
        'pharetra phasellus porta porttitor posuere pretium proin pulvinar purus quam quis rhoncus rutrum sapien sed sem semper'
        'sit sollicitudin tempor tempus tincidunt tortor turpis ullamcorper ultricies ut varius vehicula vel velit vestibulum'
        'vitae viverra volutpat vulputate'
    ), ' ')

    return _.join(_.times(sentences, lambda i_: _.capitalize(_.join(_.sample(vocab, words or _.random(5, 30)), ' '))), '. ')


def decap(s):
    if not isinstance(s, str):
        raise TypeError('String expected')

    return s[0].lower() + s[1:] if len(s) > 0 else s


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

# # Example:
#
# words = ['ÑÐ±Ð»Ð¾ÐºÐ¾', 'ÑÐ±Ð»Ð¾ÐºÐ°', 'ÑÐ±Ð»Ð¾Ðº']
#
# for i in range(0, 30):
#     print(i, morph(i, words))
